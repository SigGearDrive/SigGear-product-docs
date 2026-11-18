#!/usr/bin/env node
"use strict";
const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");
const source=fs.readFileSync("docs/assets/javascripts/motor-quick-downloads.js","utf8");
const callbacks={};
const input={value:"",addEventListener:(name,callback)=>{callbacks[name]=callback;}};
const status={textContent:""};
function createLink(name, title){return {textContent:name,hidden:false,getAttribute:key=>key==="title"?title:null};}
function row(diameter,type,links){
  return {hidden:false,cells:[{textContent:diameter},{textContent:type},{textContent:""},{textContent:"Draft V0.9"}],links,
    querySelectorAll:selector=>selector==="td"?this.cells:[],
  };
}
function makeRow(diameter,type,links){
 const out={hidden:false,cells:[{textContent:diameter},{textContent:type},{textContent:""},{textContent:"Draft V0.9"}],links};
 out.querySelectorAll=sel=>sel==="td"?out.cells:sel==="a.siggear-motor-file"?out.links:[];
 return out;
}
const rows=[
 makeRow("Ø8 mm","DC",[createLink("Set A PDF","Models: 030330"),createLink("Set B PDF","Models: 024139")]),
 makeRow("Ø16 mm","DC",[createLink("060127-240127 PDF","Models: 120132 090127"),createLink("060128-240128 PDF","Models: 120132 090131")]),
 makeRow("Ø24 mm","BLDC",[createLink("HR-BL2453 PDF","Models: HR-BL2453-Q240150100-12-55")]),
];
const table={dataset:{},querySelectorAll:selector=>selector==="tbody tr"?rows:[]};
const document={
 readyState:"loading",
 getElementById:id=>({"siggear-motor-filter":input,"siggear-motor-quick-table":table,"siggear-motor-results":status}[id]||null),
 addEventListener:(name,fn)=>{callbacks[name]=fn;}
};
vm.runInNewContext(source,{document},{filename:"motor-quick-downloads.js"});
assert.equal(typeof callbacks.DOMContentLoaded,"function");
callbacks.DOMContentLoaded();
assert.equal(status.textContent,"3 diameter groups · 5 of 5 direct PDFs");
assert.equal(rows.every(r=>!r.hidden),"true"===String(rows.every(r=>!r.hidden)));
input.value="120132";callbacks.input();
assert.equal(rows[1].links.filter(x=>!x.hidden).length,2);
assert.equal(rows.filter(r=>!r.hidden).length,1);
assert.equal(status.textContent,"1 diameter group · 2 of 5 direct PDFs");
input.value="16 mm";callbacks.input();
assert.equal(rows[1].links.filter(x=>!x.hidden).length,2);
input.value="BLDC";callbacks.input();
assert.equal(rows.filter(r=>!r.hidden).length,1);
assert.equal(rows[2].hidden,false);
input.value="NoSuchWinding";callbacks.input();
assert.match(status.textContent,/No matching motor PDFs/);
assert.equal(rows.filter(r=>!r.hidden).length,0);
input.value="";callbacks.input();
assert.equal(rows.filter(r=>!r.hidden).length,3);
assert.equal(rows.flatMap(r=>r.links).every(x=>!x.hidden),true);
callbacks.DOMContentLoaded(); // guard against duplicate binding
console.log("PASS motor PDF quick search by diameter, winding code and motor type");
