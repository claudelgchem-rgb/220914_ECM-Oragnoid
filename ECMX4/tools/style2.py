# -*- coding: utf-8 -*-
"""ECMX-003 보고서 CSS.

설계 의도 — 이 문서는 논증문이 아니라 **제조 명세서(BOM)** 다.
이 분야에서 가장 흔한 오류가 '배지 성분'과 '매트릭스 성분'을 섞어 적는 것이므로,
두 계통에 서로 다른 색 계열을 주어 한눈에 갈리게 한다. 그것이 이 페이지의 정보 설계다.
  · 지지체(매트릭스) 계통 — 청록(teal)
  · 배지 계통 — 자주(plum)
필수도는 색의 농도가 아니라 **글자로** 표시한다(필수/조건부/선택/미사용).
"""

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=IBM+Plex+Mono:wght@400;500;600&'
         'family=IBM+Plex+Sans+KR:wght@300;400;500;600;700&display=swap">')

CSS = r"""
:root{
  /* 지면 — 실험대 위의 종이. 미색이 아니라 한기 도는 흰색 */
  --bg:#FBFCFD; --surface:#FFFFFF; --sunk:#F3F6F8;
  --ink:#121A20; --mut:#4E5C68; --faint:#8494A1;
  --line:#E3E9ED; --line2:#C6D0D7; --rule:#0E6B5E;

  /* 두 계통 */
  --mx:#0E6B5E; --mx-bg:#E6F2EF; --mx-ln:#9CCcC2;
  --md:#6B3FA0; --md-bg:#F0EAF8; --md-ln:#C3AEE0;

  /* 필수도 */
  --req:#0B5E52; --req-bg:#DFEFEB;
  --cnd:#9A6410; --cnd-bg:#FBF1DF;
  --opt:#5B6B78; --opt-bg:#EDF1F4;
  --non:#8494A1; --non-bg:#F4F6F8;

  --ok:#1B6B47; --ok-bg:#E5F2EB;
  --warn:#8A5A00; --warn-bg:#FBF2E0;
  --bad:#9B2226; --bad-bg:#FBEAEA;

  --maxw:76ch; --r:9px;
  color-scheme:light dark;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --bg:#10161B; --surface:#171F26; --sunk:#1C252C;
    --ink:#E4EAEF; --mut:#A6B4C0; --faint:#7C8B98;
    --line:#26313A; --line2:#3A4751; --rule:#5FC3B2;
    --mx:#5FC3B2; --mx-bg:#12302B; --mx-ln:#2E6A60;
    --md:#BFA0E8; --md-bg:#251A36; --md-ln:#53406E;
    --req:#74D3BE; --req-bg:#123028; --cnd:#E5BE66; --cnd-bg:#332818;
    --opt:#9FB0BC; --opt-bg:#212A31; --non:#7C8B98; --non-bg:#1B2229;
    --ok:#7FD4A6; --ok-bg:#15291F; --warn:#E3BE78; --warn-bg:#2F2717; --bad:#F0938F; --bad-bg:#331C1C;
  }
}
:root[data-theme="dark"]{
  --bg:#10161B; --surface:#171F26; --sunk:#1C252C;
  --ink:#E4EAEF; --mut:#A6B4C0; --faint:#7C8B98;
  --line:#26313A; --line2:#3A4751; --rule:#5FC3B2;
  --mx:#5FC3B2; --mx-bg:#12302B; --mx-ln:#2E6A60;
  --md:#BFA0E8; --md-bg:#251A36; --md-ln:#53406E;
  --req:#74D3BE; --req-bg:#123028; --cnd:#E5BE66; --cnd-bg:#332818;
  --opt:#9FB0BC; --opt-bg:#212A31; --non:#7C8B98; --non-bg:#1B2229;
  --ok:#7FD4A6; --ok-bg:#15291F; --warn:#E3BE78; --warn-bg:#2F2717; --bad:#F0938F; --bad-bg:#331C1C;
}

*{box-sizing:border-box}
body{
  margin:0; background:var(--bg); color:var(--ink);
  font-family:"IBM Plex Sans KR",system-ui,-apple-system,"Apple SD Gothic Neo",sans-serif;
  font-size:16.5px; line-height:1.78; letter-spacing:-.004em;
  -webkit-text-size-adjust:100%; -webkit-font-smoothing:antialiased;
}
.wrap{display:flex; align-items:flex-start}

/* ── 목차 ── */
#toc{position:sticky; top:0; flex:0 0 268px; height:100vh; overflow-y:auto;
  border-right:1px solid var(--line); background:var(--surface); padding:18px 12px 40px}
#toc h2{font-family:"IBM Plex Mono",monospace; font-size:11px; letter-spacing:.14em;
  text-transform:uppercase; color:var(--faint); margin:0 0 10px 6px; border:0; padding:0}
#toc a{display:block; padding:4px 9px; font-size:13px; color:var(--mut); text-decoration:none;
  border-radius:6px; line-height:1.45; border-left:2px solid transparent}
#toc a:hover{background:var(--sunk); color:var(--ink)}
#toc a.lv2{padding-left:20px; font-size:12.3px; color:var(--faint)}
#toc a.cur{color:var(--rule); background:var(--sunk); border-left-color:var(--rule); font-weight:600}
#toc a.sMX.cur{border-left-color:var(--mx); color:var(--mx)}
#toc a.sMD.cur{border-left-color:var(--md); color:var(--md)}
#tocBtn{display:none}

main{flex:1 1 auto; min-width:0; max-width:calc(var(--maxw) + 210px);
  padding-inline:28px; padding-block:0 110px; margin:0 auto; overflow-x:clip}

/* ── 표지 ── */
.cover{padding:56px 0 30px; border-bottom:2px solid var(--line2); margin-bottom:32px}
.kicker{font-family:"IBM Plex Mono",monospace; font-size:11.5px; letter-spacing:.16em;
  text-transform:uppercase; color:var(--rule); font-weight:600}
.cover h1{font-size:2.1rem; line-height:1.24; margin:.32em 0 .18em; letter-spacing:-.025em;
  font-weight:700; text-wrap:balance}
.cover .sub{font-size:1.04rem; color:var(--mut); margin:0 0 20px; line-height:1.62; max-width:62ch}
.meta{display:flex; flex-wrap:wrap; gap:7px 8px; margin:16px 0 22px}
.meta span{font-family:"IBM Plex Mono",monospace; font-size:11.6px; background:var(--surface);
  border:1px solid var(--line); padding:4px 10px; border-radius:5px; color:var(--mut);
  font-variant-numeric:tabular-nums}
.lede{font-size:1.03rem; line-height:1.8; background:var(--surface); border:1px solid var(--line);
  border-left:4px solid var(--rule); padding:18px 22px; border-radius:var(--r)}
.lede p:last-child{margin-bottom:0}

/* ── 본문 ── */
h2{font-size:1.46rem; margin:2.8em 0 .5em; padding-bottom:.28em; font-weight:700;
  border-bottom:1px solid var(--line2); letter-spacing:-.02em; scroll-margin-top:14px}
h2.mx{border-bottom-color:var(--mx-ln)} h2.mx .tag{color:var(--mx)}
h2.md{border-bottom-color:var(--md-ln)} h2.md .tag{color:var(--md)}
h2 .tag{font-family:"IBM Plex Mono",monospace; font-size:.58em; letter-spacing:.1em;
  text-transform:uppercase; font-weight:600; display:block; margin-bottom:.25em; color:var(--faint)}
h3{font-size:1.13rem; margin:1.9em 0 .42em; font-weight:600; scroll-margin-top:14px; letter-spacing:-.012em}
h4{font-size:.99rem; margin:1.45em 0 .32em; color:var(--mut); font-weight:600}
p{margin:0 0 1.02em; max-width:var(--maxw)}
ul,ol{max-width:var(--maxw); padding-left:1.3em; margin:0 0 1.02em}
li{margin:.28em 0}
a{color:var(--rule)}
code{font-family:"IBM Plex Mono",monospace; font-size:.87em; background:var(--sunk);
  padding:.1em .38em; border-radius:4px; font-variant-numeric:tabular-nums}
hr{border:0; border-top:1px solid var(--line); margin:2.3em 0}

/* ── 필수도 배지 ── */
.n{display:inline-block; font-family:"IBM Plex Mono",monospace; font-size:11px; font-weight:600;
  padding:1.5px 7px; border-radius:4px; border:1px solid; white-space:nowrap; line-height:1.5}
.n-필수{color:var(--req); background:var(--req-bg); border-color:var(--req)}
.n-조건부{color:var(--cnd); background:var(--cnd-bg); border-color:var(--cnd)}
.n-선택{color:var(--opt); background:var(--opt-bg); border-color:var(--opt)}
.n-미사용{color:var(--non); background:var(--non-bg); border-color:var(--non); opacity:.85}
/* 계통 표시 */
.sys{display:inline-block; font-family:"IBM Plex Mono",monospace; font-size:10.5px; font-weight:600;
  padding:1px 6px; border-radius:3px; letter-spacing:.04em}
.sys-mx{color:var(--mx); background:var(--mx-bg)}
.sys-md{color:var(--md); background:var(--md-bg)}
/* 신뢰도 */
.b{display:inline-block; font-family:"IBM Plex Mono",monospace; font-size:10.5px; font-weight:600;
  padding:1px 6px; border-radius:4px; border:1px solid; cursor:help; white-space:nowrap}
.b-상{color:var(--ok); background:var(--ok-bg); border-color:var(--ok)}
.b-중{color:var(--warn); background:var(--warn-bg); border-color:var(--warn)}
.b-하{color:var(--bad); background:var(--bad-bg); border-color:var(--bad)}
/* 근거 등급 — 필수도 판정의 사유로만 따라붙는다 */
.b-E0{color:var(--bad); background:var(--bad-bg); border-color:var(--bad)}
.b-E1{color:var(--warn); background:var(--warn-bg); border-color:var(--warn)}
.b-E2{color:var(--mut); background:var(--sunk); border-color:var(--line2)}
.b-E3{color:var(--faint); background:var(--non-bg); border-color:var(--line2)}

/* ── 각주 ── */
sup.fn{font-size:.66em; vertical-align:super; line-height:0}
sup.fn a{text-decoration:none; color:var(--rule); font-weight:600;
  font-family:"IBM Plex Mono",monospace; padding:0 1px}
li.ref{font-size:13.2px; line-height:1.58; margin:.45em 0; color:var(--mut); scroll-margin-top:20px}
li.ref:target{background:var(--sunk); border-radius:6px; padding:5px 8px; margin-left:-8px}
li.ref .nw{font-family:"IBM Plex Mono",monospace; font-size:12.2px; white-space:nowrap}
.back{font-size:11px; text-decoration:none; color:var(--rule); margin-left:5px}

/* ── 표 ── */
.tw{overflow-x:auto; margin:0 0 .4em; border:1px solid var(--line); border-radius:var(--r);
  background:var(--surface); -webkit-overflow-scrolling:touch}
.tw.mx{border-color:var(--mx-ln)} .tw.md{border-color:var(--md-ln)}
table{border-collapse:collapse; width:100%; font-size:13.4px; min-width:540px;
  font-variant-numeric:tabular-nums}
th,td{border-bottom:1px solid var(--line); padding:7.5px 10px; text-align:left;
  vertical-align:top; line-height:1.52}
thead th{background:var(--sunk); font-weight:600; font-size:12.3px; white-space:nowrap;
  position:sticky; top:0; border-bottom:2px solid var(--line2)}
.tw.mx thead th{background:var(--mx-bg)} .tw.md thead th{background:var(--md-bg)}
tbody tr:last-child td{border-bottom:0}
tbody tr:hover{background:var(--sunk)}
td.q{font-family:"IBM Plex Mono",monospace; font-size:12.4px; white-space:nowrap}
.q{font-family:"IBM Plex Mono",monospace; font-size:.93em; white-space:nowrap;
  font-variant-numeric:tabular-nums}
.na{color:var(--faint)}
td.num{text-align:right; font-family:"IBM Plex Mono",monospace; font-size:12.4px; white-space:nowrap}
.nw{white-space:nowrap}
.cap{font-size:12.2px; color:var(--faint); padding:7px 2px 0; line-height:1.58}

/* ── 그림 ── */
figure{margin:1.6em 0 1.8em; background:var(--surface); border:1px solid var(--line);
  border-radius:var(--r); padding:15px 15px 11px; overflow:hidden}
figure svg{display:block; margin:0 auto}
figcaption{font-size:12.4px; color:var(--mut); margin-top:10px; padding-top:9px;
  border-top:1px solid var(--line); line-height:1.62}
figcaption b{color:var(--ink)}
.fnote{font-size:11.8px; color:var(--faint)}
.figbox{min-width:0; overflow-x:auto; -webkit-overflow-scrolling:touch}
.reflist{padding-left:2.1em; margin:1em 0}

/* ── 박스 ── */
.box{border:1px solid var(--line); border-left:4px solid var(--rule); background:var(--surface);
  padding:14px 18px; border-radius:var(--r); margin:1.4em 0; font-size:15px; line-height:1.72}
.box.mx{border-left-color:var(--mx)} .box.md{border-left-color:var(--md)}
.box.warn{border-left-color:var(--bad); background:var(--bad-bg)}
.box.note{border-left-color:var(--warn); background:var(--warn-bg)}
.box.ok{border-left-color:var(--ok); background:var(--ok-bg)}
.box p:last-child{margin-bottom:0}
.box h4{margin-top:0; color:var(--ink)}
.disc{font-size:13.8px; line-height:1.74; color:var(--mut); background:var(--surface);
  border:1px dashed var(--line2); padding:16px 19px; border-radius:var(--r); margin:2em 0}

details{border:1px solid var(--line); border-radius:var(--r); padding:10px 15px;
  margin:1.2em 0; background:var(--surface); min-width:0; overflow-x:clip}
details>summary{cursor:pointer; font-weight:600; font-size:14.3px; color:var(--rule); list-style:revert}
details[open]>summary{margin-bottom:11px; padding-bottom:8px; border-bottom:1px solid var(--line)}

/* ── 레시피 단계 ── */
.steps{counter-reset:s; list-style:none; padding:0; margin:1.3em 0; max-width:var(--maxw)}
.steps>li{counter-increment:s; position:relative; padding:11px 14px 11px 46px; margin:0 0 8px;
  background:var(--surface); border:1px solid var(--line); border-radius:var(--r); font-size:14.8px}
.steps>li::before{content:counter(s); position:absolute; left:13px; top:11px;
  font-family:"IBM Plex Mono",monospace; font-size:12px; font-weight:600; color:#fff;
  background:var(--rule); width:21px; height:21px; border-radius:5px;
  display:grid; place-items:center}
.steps>li b{font-weight:600}
.steps>li .q{font-family:"IBM Plex Mono",monospace; font-size:13.4px; color:var(--rule)}

.grid{display:grid; gap:12px; grid-template-columns:repeat(auto-fit,minmax(210px,1fr)); margin:1.3em 0}
.card{border:1px solid var(--line); border-radius:var(--r); padding:13px 15px; background:var(--surface)}
.card .k{font-family:"IBM Plex Mono",monospace; font-size:10.8px; letter-spacing:.09em;
  text-transform:uppercase; color:var(--faint); font-weight:600}
.card .v{font-size:1.5rem; font-weight:700; margin:.14em 0 .08em; letter-spacing:-.025em;
  line-height:1.18; font-variant-numeric:tabular-nums}
.card .d{font-size:12.2px; color:var(--mut); line-height:1.5}

@media (max-width:980px){
  body{font-size:16px}
  .wrap{display:block}
  #toc{position:static; height:auto; width:auto; flex:none; border-right:0;
    border-bottom:1px solid var(--line); padding:11px 16px}
  #toc[data-collapsed="1"] .toclist{display:none}
  #toc[data-collapsed="1"]{padding-bottom:0}
  #toc[data-collapsed="1"] h2{display:none}
  #tocBtn{display:block; width:100%; text-align:left; background:transparent; border:0;
    color:var(--rule); font-weight:600; font-size:14px; padding:6px 2px; cursor:pointer;
    font-family:inherit}
  main{padding-inline:16px; padding-block:0 80px; max-width:none}
  .cover{padding:26px 0 20px}
  .cover h1{font-size:1.54rem}
  h2{font-size:1.26rem}
  table{font-size:12.8px}
}
@media (max-width:430px){
  body{font-size:15.6px}
  .cover h1{font-size:1.36rem}
  figure{padding:10px 9px 8px}
  th,td{padding:6.5px 8px}
  .steps>li{padding-left:42px}
}
@media print{
  :root{--bg:#fff; --surface:#fff; --sunk:#f4f4f4; --ink:#000; --mut:#333;
        --line:#bbb; --line2:#888; --rule:#000}
  body{font-size:10.4pt; line-height:1.48; background:#fff}
  #toc,#tocBtn,.noprint{display:none !important}
  main{padding:0; max-width:none}
  .wrap{display:block}
  h2,h3,h4{break-after:avoid; page-break-after:avoid}
  h2{font-size:13.5pt}
  figure,table,.tw,.box,.card,.steps>li{break-inside:avoid; page-break-inside:avoid}
  thead{display:table-header-group}
  tr{page-break-inside:avoid}
  a{color:#000; text-decoration:none}
  main a[href^="http"]::after{content:" (" attr(href) ")"; font-size:8pt; color:#555; word-break:break-all}
  sup.fn a::after{content:none}
  .n,.b,.sys{border:1px solid #666 !important; background:#fff !important; color:#000 !important}
  figure,details{border:1px solid #999}
  details:not([open])>*:not(summary){display:revert}
}
@media (prefers-reduced-motion:reduce){*{animation:none !important; transition:none !important}}
:focus-visible{outline:2px solid var(--rule); outline-offset:2px; border-radius:3px}
"""

JS = r"""
(function(){
  var links=[].slice.call(document.querySelectorAll('#toc a[href^="#"]')), map={};
  links.forEach(function(a){var id=a.getAttribute('href').slice(1);
    if(document.getElementById(id)) map[id]=a;});
  if('IntersectionObserver' in window){
    var seen={};
    var io=new IntersectionObserver(function(es){
      es.forEach(function(e){seen[e.target.id]=e.isIntersecting;});
      var cur=null;
      Object.keys(map).forEach(function(id){if(seen[id]&&!cur)cur=id;});
      if(cur){links.forEach(function(a){a.classList.remove('cur');});
              if(map[cur])map[cur].classList.add('cur');}
    },{rootMargin:'-8% 0px -80% 0px',threshold:0});
    Object.keys(map).forEach(function(id){io.observe(document.getElementById(id));});
  }
  var btn=document.getElementById('tocBtn'), toc=document.getElementById('toc');
  function narrow(){return window.matchMedia('(max-width:980px)').matches;}
  function setC(v){toc.setAttribute('data-collapsed',v?'1':'0');
    btn.textContent=(v?'▸ 목차 펼치기':'▾ 목차 접기');
    btn.setAttribute('aria-expanded',v?'false':'true');}
  if(btn&&toc){ setC(narrow());
    btn.addEventListener('click',function(){setC(toc.getAttribute('data-collapsed')!=='1');});
    toc.addEventListener('click',function(e){if(e.target.tagName==='A'&&narrow())setC(true);});
    var wasNarrow=narrow();
    window.addEventListener('resize',function(){var n=narrow();
      if(n!==wasNarrow){wasNarrow=n; setC(n);}});}
})();
"""

# 표 안에서만 쓰는 보조 스타일. 위 CSS 블록에 이어 붙인다.
CSS += r"""
.en{font-family:"IBM Plex Mono",monospace; font-size:11px; color:var(--faint)}
.evt{font-family:"IBM Plex Mono",monospace; font-size:9.6px; letter-spacing:.05em;
  color:var(--faint); background:var(--sunk); border-radius:3px; padding:1px 4px;
  white-space:nowrap}
.q.sm{font-size:10.8px; color:var(--faint)}
td .n{margin-right:3px}
"""

CSS += r"""
.gl{color:var(--mut); font-weight:400}
.na{color:var(--faint); font-style:italic}
"""

CSS += r"""
/* 각주가 다섯 개를 넘으면 뒤는 흐리게 — 있는 건 알되 시선을 뺏지 않게 */
.more{opacity:.45}
.more:hover{opacity:1}
table{table-layout:auto}
.tw.mx table,.tw.md table{table-layout:fixed}
.tw.mx td,.tw.md td{overflow-wrap:anywhere}
"""

CSS += r"""
/* 고정폭 표에서는 수치 칸도 접혀야 한다. nowrap을 두면 표가 화면 밖으로 밀린다. */
.tw.mx td.q,.tw.md td.q,.tw.mx td.q .q,.tw.md td.q .q{white-space:normal}
.tw.mx details td,.tw.md details td{white-space:normal}
"""

CSS += r"""
@media print{
  .tw{overflow:visible; break-inside:auto}
  table{min-width:0; font-size:9.6px}
  details{break-inside:avoid}
  figure{break-inside:avoid}
  .box,.steps>li{break-inside:avoid}
}
"""

JS += """
(function(){
  // 인쇄할 때는 접어 둔 전체 명세도 함께 나와야 한다. 구매 담당이 종이로 들고 가기 때문이다.
  var opened=[];
  function openAll(){opened=[];
    [].forEach.call(document.querySelectorAll('details:not([open])'),function(d){
      opened.push(d); d.open=true;});}
  function restore(){opened.forEach(function(d){d.open=false;}); opened=[];}
  if(window.matchMedia){var mq=window.matchMedia('print');
    if(mq.addEventListener)mq.addEventListener('change',function(e){e.matches?openAll():restore();});}
  window.addEventListener('beforeprint',openAll);
  window.addEventListener('afterprint',restore);
})();
"""

CSS += r"""
.sys{white-space:nowrap}
"""

# ── ECMX-004 추가: 재료 A/B/C 표시 ──────────────────────────────
# 이 보고서에는 축이 하나 더 있다. 같은 층위라도 어느 재료 조합을 쓰느냐에 따라
# 필요한 물질이 달라지기 때문이다. 색은 이미 계통(청록/자주)에 쓰고 있으므로
# 재료는 색이 아니라 '칸이 찼는가'로 표시한다 — 색맹과 흑백 인쇄에서도 읽힌다.
CSS += r"""
.mat{display:inline-flex; gap:2px; vertical-align:-1px; margin-left:4px}
.mat i{display:grid; place-items:center; width:15px; height:15px; border-radius:4px;
  font-family:"IBM Plex Mono",monospace; font-size:9.5px; font-weight:600; font-style:normal;
  border:1px solid var(--line2); color:var(--faint); background:var(--surface)}
.mat i.on{border-color:var(--mx); color:#fff; background:var(--mx)}
.mat i.on.helix{background:var(--mx); box-shadow:inset 0 0 0 1.5px #fff}

/* 삼중나선 / 단일사슬 — 이 보고서에서 가장 중요한 구분 */
.form{display:inline-block; font-family:"IBM Plex Mono",monospace; font-size:10px;
  font-weight:600; padding:1px 6px; border-radius:3px; white-space:nowrap; letter-spacing:.02em}
.form-th{color:#0B5E52; background:#DFEFEB; border:1px solid #7FBDB1}
.form-sc{color:#8A5A00; background:#FBF2E0; border:1px dashed #D2A54A}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]) .form-th{color:#74D3BE; background:#123028; border-color:#2E6A60}
  :root:not([data-theme="light"]) .form-sc{color:#E5BE66; background:#332818; border-color:#6B5320}
}
:root[data-theme="dark"] .form-th{color:#74D3BE; background:#123028; border-color:#2E6A60}
:root[data-theme="dark"] .form-sc{color:#E5BE66; background:#332818; border-color:#6B5320}

/* 이종유래 여부 */
.xeno{display:inline-block; font-family:"IBM Plex Mono",monospace; font-size:9.8px;
  padding:1px 5px; border-radius:3px; white-space:nowrap; border:1px solid}
.xeno-0{color:var(--ok); background:var(--ok-bg); border-color:var(--ok)}
.xeno-1{color:var(--bad); background:var(--bad-bg); border-color:var(--bad)}
.xeno-2{color:var(--warn); background:var(--warn-bg); border-color:var(--warn)}
.xeno-3{color:var(--faint); background:var(--sunk); border-color:var(--line2)}

/* 변경 내역 표시 — 이전 판정에서 무엇이 달라졌는가 */
.chg{font-family:"IBM Plex Mono",monospace; font-size:11.5px; white-space:nowrap}
.chg .was{color:var(--faint); text-decoration:line-through}
.chg .now{color:var(--ink); font-weight:600}
.chg .arr{color:var(--rule); padding:0 4px}
@media print{ .mat i.on{background:#000 !important; color:#fff !important} }
"""

CSS += r"""
/* .box.warn이 이미 빨강을 쓰고 있어 이름과 색이 어긋나 있었다.
   .bad를 따로 두어 '판정을 뒤집는 결론'에만 빨강을 준다. */
.box.bad{border-left-color:var(--bad); background:var(--bad-bg)}
"""
