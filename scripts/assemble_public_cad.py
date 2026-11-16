#!/usr/bin/env python3
"""Assemble public full-assembly STEP downloads from uploaded text chunks."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PART_ROOT = ROOT / ".github" / "cad_upload_parts"
DOWNLOAD_ROOT = ROOT / "docs" / "assets" / "downloads"

RELEASES = {
    "8P": {"slug":"8p","parts":18,"lines":86772,"source_name":"08P_asm.stp","header_name":"8PC000_ASM","source_sha256":"80f57dc8707d0a3d262efaf5eb330101d45eb89dda13c97ac3b7595eb44c873a"},
    "10P": {"slug":"10p","parts":24,"lines":117908,"source_name":"10P_asm.stp","header_name":"10000_ASM","source_sha256":"83cb86783736b6264e64d5fdb84c9700b63a0665d98eee5852a642db61d62226"},
    "12P": {"slug":"12p","parts":18,"lines":85649,"source_name":"12P_asm.stp","header_name":"12000_ASM","source_sha256":"6c0445373c880c80e4600e5ef7eb365c885cbdced9a8387af487c743436075a8"},
    "14P": {"slug":"14p","parts":18,"lines":88555,"source_name":"14P_asm.stp","header_name":"14000_ASM","source_sha256":"4bbcea93bdb0872a05df8ac31323d9a373da24a1d4cffbf4b58473f8e082feef"},
}


def assemble(model: str, spec: dict) -> dict:
    slug = spec["slug"]
    part_dir = PART_ROOT / slug
    target_dir = DOWNLOAD_ROOT / slug
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / f"{model}_Full_Assembly.step"

    with target.open("wb") as output:
        for number in range(1, spec["parts"] + 1):
            part = part_dir / f"part-{number:03d}.txt"
            if not part.is_file():
                raise FileNotFoundError(f"{model}: missing upload part {part.relative_to(ROOT)}")
            payload = part.read_bytes()
            if not payload:
                raise ValueError(f"{model}: empty upload part {part.name}")
            output.write(payload)

    payload = target.read_bytes()
    if not payload.startswith(b"ISO-10303-21;"):
        raise ValueError(f"{model}: invalid STEP file header")
    if not payload.rstrip().endswith(b"END-ISO-10303-21;"):
        raise ValueError(f"{model}: missing END-ISO-10303-21 terminator")
    if spec["header_name"].encode("ascii") not in payload[:1024]:
        raise ValueError(f"{model}: STEP FILE_NAME does not match expected source assembly")
    line_count = len(payload.splitlines())
    if line_count != spec["lines"]:
        raise ValueError(f"{model}: line count mismatch: {line_count} != {spec['lines']}")
    if len(payload) < 1_000_000:
        raise ValueError(f"{model}: assembled file is unexpectedly small ({len(payload)} bytes)")

    return {
        "model": model,
        "source_filename": spec["source_name"],
        "published_path": str(target.relative_to(ROOT / "docs")),
        "source_sha256": spec["source_sha256"],
        "published_sha256": hashlib.sha256(payload).hexdigest(),
        "bytes": len(payload),
        "lines": line_count,
        "line_endings": "LF-normalized during text transfer",
        "status": "assembled_and_validated",
    }


def main() -> None:
    manifest = [assemble(model, spec) for model, spec in RELEASES.items()]
    for item in manifest:
        print(f"PASS {item['model']}: {item['bytes']:,} bytes, {item['lines']:,} lines, SHA256 {item['published_sha256']}")
    manifest_path = DOWNLOAD_ROOT / "full-assembly-release-manifest.json"
    manifest_path.write_text(
        json.dumps({"release":"SigGear 8P–14P Full Assembly STEP","format":"STEP text assembly from Creo export","models":manifest}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"PASS release manifest: {manifest_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
