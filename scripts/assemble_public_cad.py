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
    "8P": {"slug":"8p","parts":18,"lines":86772,"source_name":"08P_asm.stp","header_name":"8PC000_ASM","source_sha256":"80f57dc8707d0a3d262efaf5eb330101d45eb89dda13c97ac3b7595eb44c873a","published_sha256":"2daf7fa0c09c1e47575f769e88282500c841194cac8bd326b78845cc50f20a85"},
    "10P": {"slug":"10p","parts":24,"lines":117908,"source_name":"10P_asm.stp","header_name":"10000_ASM","source_sha256":"83cb86783736b6264e64d5fdb84c9700b63a0665d98eee5852a642db61d62226","published_sha256":"cda8c55dc84e906d655f5ff9317899edc772db27aeaae657897d3d48eea801c6"},
    "12P": {"slug":"12p","parts":18,"lines":85649,"source_name":"12P_asm.stp","header_name":"12000_ASM","source_sha256":"6c0445373c880c80e4600e5ef7eb365c885cbdced9a8387af487c743436075a8","published_sha256":"98b73d444df0aa90504ab2b03ffa0d18a78728a16183d076120ad3874770c4a4"},
    "14P": {"slug":"14p","parts":18,"lines":88555,"source_name":"14P_asm.stp","header_name":"14000_ASM","source_sha256":"4bbcea93bdb0872a05df8ac31323d9a373da24a1d4cffbf4b58473f8e082feef","published_sha256":"3304276a0269ab6ad6fac074fa11caf1b816d8b38e462378cc173c44f806ae93"},
    "16P": {"slug":"16p","parts":14,"lines":77661,"source_name":"16P_asm(1).stp","header_name":"16000_ASM","source_sha256":"56925025d4f3aa00a978da58637adc21ade88e398d79b6be5b29b08ef01390be","published_sha256":"231a85a9543c08e281da1437c7aa6658a1183cf24b4332a4f6dc5482408df880"},
    "20P": {"slug":"20p","parts":13,"lines":71319,"source_name":"20P_asm(1).stp","header_name":"20000_ASM","source_sha256":"20dccb14c872568b1dfed915f65d624c7451ee5b4209220a1228786e66bf1f60","published_sha256":"545ad33aa5432350b38f540216035ceb576c35ab6a771b9d89504ce8889efee1"},
    "22P": {"slug":"22p","parts":15,"lines":82552,"source_name":"22P_asm(1).stp","header_name":"22000_ASM","source_sha256":"fe143796c617035e3d894399f0cf931546c483bfc2fde845ae255d721205c603","published_sha256":"1a2080b3b8bb8ebdc4fddfa1ab589acc31002c47f49aa064620cdeda0807ce83"},
    "24P": {"slug":"24p","parts":16,"lines":85423,"source_name":"24P_asm(1).stp","header_name":"24000_ASM","source_sha256":"aef0cc285399ec8246d85577337d425a75138d73c3acb3940af122857dab1818","published_sha256":"15a8959522ea16f7ec61b9f3978339340b83524122f426a4eb7a86a393cde643"},
    "28P": {"slug":"28p","parts":17,"lines":92590,"source_name":"28P_asm.stp","header_name":"28000_ASM","source_sha256":"916fbef7c44f58ece4387821564d35cefae4f62200c88b7e078c132309e460f0","published_sha256":"3b900ed577087cae782a50349fe7f558315052f5cc018b63db64c9e5267d2407"},
    "32P": {"slug":"32p","parts":16,"lines":89167,"source_name":"32P_asm.stp","header_name":"32000_ASM","source_sha256":"fd3b89a33e92424d4766b283b482312b66f69a173516d046ef9aeeb392fb5c30","published_sha256":"f2856a0e5ca06a6c0bc031b19b6362c51ef699397b949404e646c9bd2c4b9da4"},
    "36P": {"slug":"36p","parts":15,"lines":85160,"source_name":"36P_asm.stp","header_name":"36000_ASM","source_sha256":"dc5d23f0c98cc427c51b789ee76b400cb2179a5a4e41ce2f12cd2f14f78661df","published_sha256":"9d4488c20e7e858868f99c39cf6fce3cb7323a263f8aac6584cba3b8d5ed9d04"},
    "42P": {"slug":"42p","parts":18,"lines":99764,"source_name":"42P_asm.stp","header_name":"42000_ASM","source_sha256":"4987e46c5f3fd9c453f45ea3ad3f33eb98585bbe979f6fd8e99ef87706c4429","published_sha256":"a07ce4a44476df520de43f0ca0eace1f62d72d7e6176076be13ebe8b614a7da1"},
}


def pending(model: str, spec: dict) -> dict:
    return {
        "model": model,
        "source_filename": spec["source_name"],
        "published_path": f"assets/downloads/{spec['slug']}/{model}_Full_Assembly.step",
        "source_sha256": spec["source_sha256"],
        "expected_published_sha256": spec["published_sha256"],
        "parts_required": spec["parts"],
        "lines_expected": spec["lines"],
        "status": "pending_upload_parts",
    }


def assemble(model: str, spec: dict) -> dict:
    slug = spec["slug"]
    part_dir = PART_ROOT / slug
    target_dir = DOWNLOAD_ROOT / slug
    target = target_dir / f"{model}_Full_Assembly.step"

    if not part_dir.exists():
        return pending(model, spec)

    part_paths = [part_dir / f"part-{number:03d}.txt" for number in range(1, spec["parts"] + 1)]
    missing = [part for part in part_paths if not part.is_file()]
    if missing:
        names = ", ".join(str(part.relative_to(ROOT)) for part in missing[:5])
        raise FileNotFoundError(f"{model}: incomplete upload parts; missing {names}")

    target_dir.mkdir(parents=True, exist_ok=True)
    with target.open("wb") as output:
        for part in part_paths:
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

    published_sha256 = hashlib.sha256(payload).hexdigest()
    if published_sha256 != spec["published_sha256"]:
        raise ValueError(f"{model}: assembled SHA-256 mismatch: {published_sha256}")

    return {
        "model": model,
        "source_filename": spec["source_name"],
        "published_path": str(target.relative_to(ROOT / "docs")),
        "source_sha256": spec["source_sha256"],
        "published_sha256": published_sha256,
        "bytes": len(payload),
        "lines": line_count,
        "line_endings": "LF-normalized during text transfer",
        "status": "assembled_and_validated",
    }


def main() -> None:
    manifest = [assemble(model, spec) for model, spec in RELEASES.items()]
    for item in manifest:
        if item["status"] == "assembled_and_validated":
            print(f"PASS {item['model']}: {item['bytes']:,} bytes, {item['lines']:,} lines, SHA256 {item['published_sha256']}")
        else:
            print(f"PENDING {item['model']}: {item['parts_required']} upload parts not present yet")

    manifest_path = DOWNLOAD_ROOT / "full-assembly-release-manifest.json"
    manifest_path.write_text(
        json.dumps({
            "release": "SigGear 8P–42P Full Assembly STEP",
            "format": "STEP text assembly from Creo export",
            "models": manifest,
        }, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"PASS release manifest: {manifest_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
