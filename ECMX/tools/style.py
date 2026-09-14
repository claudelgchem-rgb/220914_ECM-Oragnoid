# -*- coding: utf-8 -*-
"""ECMX 보고서 CSS (§9-1). 전부 인라인. 외부 폰트·스타일시트·CDN 일절 사용하지 않음."""

CSS = r"""
:root{
  --bg:#FBFAF8; --surface:#FFFFFF; --ink:#1F2933; --mut:#5A6672; --faint:#8B96A1;
  --line:#E2E6EA; --line2:#CFD6DC; --acc:#2C5F8D; --acc-soft:#EAF1F7;
  --e0:#B3261E; --e1:#C25A08; --e2:#8A6D08; --e3:#6B7785;
  --e0bg:#FCEBEA; --e1bg:#FDF0E4; --e2bg:#FBF5DF; --e3bg:#EFF1F3;
  --ok:#1E6B45; --okbg:#E7F3EC; --warn:#8A5A00; --warnbg:#FCF3E2; --bad:#9B2226; --badbg:#FBEAEA;
  --maxw:78ch; --radius:10px;
  color-scheme:light dark;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --bg:#14181C; --surface:#1B2126; --ink:#E6EAEE; --mut:#A8B3BD; --faint:#7E8B96;
    --line:#2C343B; --line2:#3C464F; --acc:#7FB2E0; --acc-soft:#1E2A35;
    --e0:#FF9B93; --e1:#FFB870; --e2:#E8CE6A; --e3:#A8B3BD;
    --e0bg:#3A1F1E; --e1bg:#38271A; --e2bg:#33301C; --e3bg:#252C32;
    --ok:#8FD6AE; --okbg:#1B2E24; --warn:#E8C177; --warnbg:#332918; --bad:#FF9B93; --badbg:#3A1F1E;
  }
}
:root[data-theme="dark"]{
  --bg:#14181C; --surface:#1B2126; --ink:#E6EAEE; --mut:#A8B3BD; --faint:#7E8B96;
  --line:#2C343B; --line2:#3C464F; --acc:#7FB2E0; --acc-soft:#1E2A35;
  --e0:#FF9B93; --e1:#FFB870; --e2:#E8CE6A; --e3:#A8B3BD;
  --e0bg:#3A1F1E; --e1bg:#38271A; --e2bg:#33301C; --e3bg:#252C32;
  --ok:#8FD6AE; --okbg:#1B2E24; --warn:#E8C177; --warnbg:#332918; --bad:#FF9B93; --badbg:#3A1F1E;
}

*{box-sizing:border-box}
body{
  margin:0; background:var(--bg); color:var(--ink);
  font-family:system-ui,-apple-system,"Apple SD Gothic Neo","Malgun Gothic","Noto Sans KR",sans-serif;
  font-size:16.5px; line-height:1.78; -webkit-text-size-adjust:100%;
}
.wrap{display:flex; align-items:flex-start; gap:0}

/* ---------- 목차 ---------- */
#toc{
  position:sticky; top:0; flex:0 0 274px; height:100vh; overflow-y:auto;
  border-right:1px solid var(--line); background:var(--surface); padding:20px 14px 40px;
}
#toc h2{font-size:12px; letter-spacing:.12em; text-transform:uppercase; color:var(--faint); margin:0 0 10px 6px}
#toc a{display:block; padding:4px 8px; font-size:13.2px; color:var(--mut); text-decoration:none;
  border-radius:6px; line-height:1.45; border-left:2px solid transparent}
#toc a:hover{background:var(--acc-soft); color:var(--acc)}
#toc a.lv2{padding-left:19px; font-size:12.4px; color:var(--faint)}
#toc a.cur{color:var(--acc); background:var(--acc-soft); border-left-color:var(--acc); font-weight:600}
#tocBtn{display:none}

main{flex:1 1 auto; min-width:0; max-width:calc(var(--maxw) + 190px);
  padding-inline:26px; padding-block:0 90px; margin:0 auto; overflow-x:clip}

/* ---------- 표지 ---------- */
.cover{padding:54px 0 30px; border-bottom:2px solid var(--line2); margin-bottom:34px}
.cover .kicker{font-size:12px; letter-spacing:.18em; text-transform:uppercase; color:var(--acc); font-weight:700}
.cover h1{font-size:2.15rem; line-height:1.26; margin:.34em 0 .2em; letter-spacing:-.015em}
.cover .sub{font-size:1.06rem; color:var(--mut); margin:0 0 20px; line-height:1.6}
.meta{display:flex; flex-wrap:wrap; gap:7px 9px; margin:16px 0 22px}
.meta span{font-size:12.3px; background:var(--surface); border:1px solid var(--line);
  padding:4px 11px; border-radius:999px; color:var(--mut)}
.lede{font-size:1.04rem; line-height:1.82; background:var(--surface); border:1px solid var(--line);
  border-left:4px solid var(--acc); padding:18px 22px; border-radius:var(--radius); color:var(--ink)}

/* ---------- 본문 ---------- */
h2{font-size:1.52rem; margin:2.6em 0 .55em; padding-bottom:.3em; border-bottom:1px solid var(--line2);
   letter-spacing:-.01em; scroll-margin-top:16px}
h3{font-size:1.16rem; margin:2em 0 .45em; color:var(--ink); scroll-margin-top:16px}
h4{font-size:1.0rem; margin:1.5em 0 .35em; color:var(--mut); font-weight:700}
p{margin:0 0 1.05em; max-width:var(--maxw)}
ul,ol{max-width:var(--maxw); padding-left:1.35em; margin:0 0 1.05em}
li{margin:.3em 0}
strong{font-weight:700}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:.88em;
  background:var(--acc-soft); padding:.1em .38em; border-radius:4px}
a{color:var(--acc)}
hr{border:0; border-top:1px solid var(--line); margin:2.4em 0}

/* ---------- 신뢰도 배지 ---------- */
.b{display:inline-block; font-size:11px; font-weight:700; padding:1px 7px; border-radius:5px;
   vertical-align:.08em; white-space:nowrap; cursor:help; border:1px solid transparent; line-height:1.55}
.b-상{color:var(--ok); background:var(--okbg); border-color:var(--ok)}
.b-중{color:var(--warn); background:var(--warnbg); border-color:var(--warn)}
.b-하{color:var(--bad); background:var(--badbg); border-color:var(--bad)}
.t{display:inline-block; font-size:11px; font-weight:800; padding:1px 7px; border-radius:5px;
   border:1px solid; white-space:nowrap; line-height:1.55}
.t-E0{color:var(--e0); background:var(--e0bg); border-color:var(--e0)}
.t-E1{color:var(--e1); background:var(--e1bg); border-color:var(--e1)}
.t-E2{color:var(--e2); background:var(--e2bg); border-color:var(--e2)}
.t-E3{color:var(--e3); background:var(--e3bg); border-color:var(--e3)}

/* ---------- 각주 ---------- */
sup.fn{font-size:.68em; vertical-align:super; line-height:0}
sup.fn a{text-decoration:none; color:var(--acc); font-weight:700; padding:0 1px}
sup.fn a:hover{text-decoration:underline}
li.ref{font-size:13.4px; line-height:1.6; margin:.5em 0; color:var(--mut); scroll-margin-top:20px}
li.ref:target{background:var(--acc-soft); border-radius:6px; padding:5px 8px; margin-left:-8px}
.back{font-size:11.5px; text-decoration:none; color:var(--acc); margin-left:5px; white-space:nowrap}

/* ---------- 표 ---------- */
.tw{overflow-x:auto; margin:0 0 .5em; border:1px solid var(--line); border-radius:var(--radius);
    background:var(--surface); -webkit-overflow-scrolling:touch}
table{border-collapse:collapse; width:100%; font-size:13.6px; min-width:520px}
th,td{border-bottom:1px solid var(--line); padding:8px 11px; text-align:left; vertical-align:top; line-height:1.55}
thead th{background:var(--acc-soft); color:var(--ink); font-weight:700; font-size:12.6px;
  position:sticky; top:0; border-bottom:2px solid var(--line2); white-space:nowrap}
tbody tr:last-child td{border-bottom:0}
tbody tr:hover{background:var(--acc-soft)}
caption,.cap{caption-side:bottom; text-align:left; font-size:12.4px; color:var(--faint);
  padding:8px 2px 0; line-height:1.6}
td.num{text-align:right; font-variant-numeric:tabular-nums; white-space:nowrap}
.nw{white-space:nowrap}

/* ---------- 그림 ---------- */
figure{margin:1.7em 0 1.9em; background:var(--surface); border:1px solid var(--line);
  border-radius:var(--radius); padding:16px 16px 12px; overflow:hidden}
figure svg{display:block; margin:0 auto}
figcaption{font-size:12.7px; color:var(--mut); margin-top:11px; padding-top:10px;
  border-top:1px solid var(--line); line-height:1.66}
figcaption b{color:var(--ink)}

/* ---------- 강조 박스 ---------- */
.box{border:1px solid var(--line); border-left:4px solid var(--acc); background:var(--surface);
  padding:15px 19px; border-radius:var(--radius); margin:1.5em 0; font-size:15.2px; line-height:1.74}
.box.warn{border-left-color:var(--bad); background:var(--badbg)}
.box.note{border-left-color:var(--warn); background:var(--warnbg)}
.box.ok{border-left-color:var(--ok); background:var(--okbg)}
.box p:last-child{margin-bottom:0}
.box h4{margin-top:0}
.disc{font-size:14px; line-height:1.76; color:var(--mut); background:var(--surface);
  border:1px dashed var(--line2); padding:17px 20px; border-radius:var(--radius); margin:2em 0}

details{border:1px solid var(--line); border-radius:var(--radius); padding:11px 16px;
  margin:1.3em 0; background:var(--surface);
  /* 접힌 상태의 details가 내부 표의 고유 폭을 바깥으로 흘려 문서에 가로 스크롤을
     만드는 것을 막는다. 표 자체는 .tw 안에서 따로 가로 스크롤된다. */
  min-width:0; overflow-x:clip}
details>summary{cursor:pointer; font-weight:700; font-size:14.6px; color:var(--acc); list-style:revert}
details[open]>summary{margin-bottom:12px; padding-bottom:9px; border-bottom:1px solid var(--line)}

.grid{display:grid; gap:13px; grid-template-columns:repeat(auto-fit,minmax(215px,1fr)); margin:1.4em 0}
.card{border:1px solid var(--line); border-radius:var(--radius); padding:14px 16px; background:var(--surface)}
.card .k{font-size:11.4px; letter-spacing:.09em; text-transform:uppercase; color:var(--faint); font-weight:700}
.card .v{font-size:1.55rem; font-weight:800; margin:.16em 0 .1em; letter-spacing:-.02em; line-height:1.2}
.card .d{font-size:12.4px; color:var(--mut); line-height:1.55}

/* ---------- 반응형 ---------- */
@media (max-width:980px){
  body{font-size:16px}
  .wrap{display:block}
  #toc{position:static; height:auto; width:auto; flex:none; border-right:0;
    border-bottom:1px solid var(--line); padding:12px 16px; max-height:none}
  #toc[data-collapsed="1"] .toclist{display:none}
  #tocBtn{display:block; width:100%; text-align:left; background:transparent; border:0;
    color:var(--acc); font-weight:700; font-size:14px; padding:6px 2px; cursor:pointer;
    font-family:inherit}
  main{padding-inline:16px; padding-block:0 70px; max-width:none}
  .cover{padding:28px 0 22px}
  .cover h1{font-size:1.6rem}
  h2{font-size:1.3rem}
  table{font-size:13px}
}
@media (max-width:430px){
  body{font-size:15.6px}
  .cover h1{font-size:1.4rem}
  figure{padding:11px 10px 9px}
  th,td{padding:7px 8px}
}

/* ---------- 인쇄 ---------- */
@media print{
  :root{--bg:#fff; --surface:#fff; --ink:#000; --mut:#333; --line:#bbb; --line2:#888; --acc:#000;
         --acc-soft:#f2f2f2}
  body{font-size:10.5pt; line-height:1.5; background:#fff}
  #toc,#tocBtn,.noprint{display:none !important}
  main{padding:0; max-width:none}
  .wrap{display:block}
  h2{page-break-after:avoid; break-after:avoid; font-size:14pt}
  h3,h4{page-break-after:avoid; break-after:avoid}
  figure,table,.tw,.box,.card{page-break-inside:avoid; break-inside:avoid}
  thead{display:table-header-group}
  tr{page-break-inside:avoid}
  a{color:#000; text-decoration:none}
  main a[href^="http"]::after{content:" (" attr(href) ")"; font-size:8pt; color:#555; word-break:break-all}
  sup.fn a::after{content:none}
  .b,.t{border:1px solid #666 !important; background:#fff !important; color:#000 !important}
  figure{border:1px solid #999}
  details{border:1px solid #999}
  details>summary{color:#000}
  details:not([open])>*:not(summary){display:revert}
}
"""

JS = r"""
(function(){
  // 목차 현재 위치 표시
  var links=[].slice.call(document.querySelectorAll('#toc a[href^="#"]'));
  var map={};
  links.forEach(function(a){
    var t=document.getElementById(a.getAttribute('href').slice(1));
    if(t) map[a.getAttribute('href').slice(1)]=a;
  });
  if('IntersectionObserver' in window){
    var seen={};
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){ seen[e.target.id]=e.isIntersecting; });
      var cur=null;
      Object.keys(map).forEach(function(id){ if(seen[id]&&!cur) cur=id; });
      if(cur){ links.forEach(function(a){a.classList.remove('cur');});
               if(map[cur]) map[cur].classList.add('cur'); }
    },{rootMargin:'-8% 0px -80% 0px',threshold:0});
    Object.keys(map).forEach(function(id){ var el=document.getElementById(id); if(el) io.observe(el); });
  }
  // 좁은 화면 목차 접기
  var btn=document.getElementById('tocBtn'), toc=document.getElementById('toc');
  function narrow(){ return window.matchMedia('(max-width:980px)').matches; }
  function setC(v){ toc.setAttribute('data-collapsed', v?'1':'0');
    btn.textContent=(v?'▸ 목차 펼치기':'▾ 목차 접기'); btn.setAttribute('aria-expanded', v?'false':'true'); }
  if(btn&&toc){
    setC(narrow());
    btn.addEventListener('click',function(){ setC(toc.getAttribute('data-collapsed')!=='1'); });
    toc.addEventListener('click',function(e){ if(e.target.tagName==='A'&&narrow()) setC(true); });
    window.addEventListener('resize',function(){ if(!narrow()) setC(false); });
  }
})();
"""
