#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""자체 완결형 보고서(ECMX_report.html)를 Artifact 발행용으로 변환한다.

두 산출물의 역할이 다르다.
  · ECMX_report.html — 하니스 §9-1 규격. 외부 자원 0건, 오프라인 단독 실행. 시스템 폰트.
  · 이 스크립트의 출력 — 웹에서 바로 열리는 링크용. 폰트만 Google Fonts로 올린다.
Artifact 런타임이 <!doctype>…<head>…<body> 골격을 씌우므로 그 태그들은 제거한다.
"""
import os, re, sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(BASE, "ECMX_report.html")
OUT = os.path.join(BASE, "ECMX_report_artifact.html")

# Artifact CSP가 허용하는 유일한 스타일시트 호스트
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=IBM+Plex+Mono:wght@400;600&'
         'family=IBM+Plex+Sans+KR:wght@400;500;600;700&'
         'family=Noto+Serif+KR:wght@500;600;700&display=swap">')

# 서체·지면 보정. 등급 색(E0~E3)과 강조색은 본문 인라인 SVG 13점이 같은 값으로 그려져 있으므로
# 건드리지 않는다 — 색을 바꾸면 그림과 배지가 어긋난다. 바꾸는 것은 서체와 지면 리듬뿐이다.
TYPO = r"""
/* ── Artifact 발행본 서체 보정 ───────────────────────────────────────────
   본문은 IBM Plex Sans KR — 수치가 많은 문서라 자간이 고르고 숫자가 또렷하다.
   표제는 Noto Serif KR — 근거로 논증하는 문서의 성격에 맞는 무게를 준다.
   식별자(N-001, E0, OMIT, DOI, 특허번호)는 IBM Plex Mono로 고정해
   '근거 장치'가 본문과 시각적으로 구분되게 한다.                        */
:root{
  --font-body: "IBM Plex Sans KR", system-ui, -apple-system, "Apple SD Gothic Neo", sans-serif;
  --font-display: "Noto Serif KR", "Apple SD Gothic Neo", Georgia, serif;
  --font-mono: "IBM Plex Mono", ui-monospace, SFMono-Regular, Menlo, monospace;
  --paper: #FAFBFC;
}
body{ font-family:var(--font-body); font-size:16.5px; letter-spacing:-.003em;
      -webkit-font-smoothing:antialiased; }

h1,h2,h3,.cover h1{ font-family:var(--font-display); font-weight:700;
  letter-spacing:-.018em; text-wrap:balance; }
h2{ font-weight:600; }
h4{ font-family:var(--font-body); font-weight:700; letter-spacing:.005em; }
.cover .kicker{ font-family:var(--font-mono); font-weight:600; letter-spacing:.14em; }
.cover .sub{ font-family:var(--font-body); }

code,.b,.t,.card .k{ font-family:var(--font-mono); font-feature-settings:"zero" 1; }
.b,.t{ letter-spacing:.01em; }
.meta span{ font-family:var(--font-mono); font-size:11.8px; letter-spacing:.005em; }

/* 숫자가 열을 이루는 곳은 등폭 숫자로 — Pa/kPa, 건수, 연도, 비율 */
table,.card .v,.tw,.meta{ font-variant-numeric:tabular-nums; }
td.num{ font-family:var(--font-mono); font-size:12.8px; }
thead th{ font-family:var(--font-body); font-weight:600; letter-spacing:.01em; }

#toc a{ font-family:var(--font-body); letter-spacing:-.002em; }
#toc h2{ font-family:var(--font-mono); font-weight:600; }
li.ref{ font-family:var(--font-body); }
li.ref .nw{ font-family:var(--font-mono); font-size:12.4px; }
figcaption{ font-family:var(--font-body); }
figcaption b{ font-family:var(--font-display); font-weight:600; }
.cap,caption{ font-family:var(--font-body); }
details>summary{ font-family:var(--font-display); font-weight:600; }

/* 지면 — 웹에서 읽을 때의 여백. 규격본보다 조금 더 넉넉하게 준다. */
:root{ --maxw:74ch; }
main{ padding-block:0 110px; }
.cover{ padding-top:60px; }
p{ line-height:1.82; }
h2{ margin-top:2.9em; }

/* 근거 배지는 이 보고서의 정보 구조 자체다. 조금 더 또렷하게. */
.b,.t{ padding:1.5px 8px; font-size:11.2px; }
sup.fn a{ font-family:var(--font-mono); font-weight:600; }

@media (max-width:980px){
  body{ font-size:16px; }
  main{ padding-block:0 80px; }
  .cover{ padding-top:30px; }
}
@media print{
  body{ font-family:var(--font-body); }
  h1,h2,h3{ font-family:var(--font-display); }
}
"""


def main():
    h = open(SRC, encoding="utf-8").read()

    m_title = re.search(r"<title>(.*?)</title>", h, re.S)
    m_style = re.search(r"<style>(.*?)</style>", h, re.S)
    m_body = re.search(r"<body>(.*?)</body>", h, re.S)
    m_script = re.search(r"<script>(.*?)</script>", h, re.S)
    if not all((m_title, m_style, m_body)):
        sys.exit("원본에서 title/style/body 블록을 찾지 못했다")

    body = m_body.group(1)
    if m_script:
        body = body.replace(m_script.group(0), "")   # 스크립트는 맨 끝으로 옮긴다

    parts = [
        FONTS,
        # Artifact 갤러리·탭에 표시되는 이름. 설명은 발행 시 description으로 따로 준다.
        "<title>오가노이드 지지체 필수 물질</title>",
        "<style>" + m_style.group(1) + TYPO + "</style>",
        body.strip(),
    ]
    if m_script:
        parts.append("<script>" + m_script.group(1) + "</script>")

    out = "\n".join(parts)
    open(OUT, "w", encoding="utf-8").write(out)

    # 발행 전 확인 — 금지 태그가 남지 않았는지, 허용 외 외부 자원이 없는지
    bad = [t for t in ("<!DOCTYPE", "<html", "<head>", "<body>", "</html>") if t in out]
    ext = re.findall(r'(?:src|href)\s*=\s*["\'](https?://[^"\']+)', out)
    allowed = [u for u in ext if u.startswith(("https://fonts.googleapis.com",
                                               "https://fonts.gstatic.com"))]
    print(f"saved: {OUT}  ({len(out)/1024:.0f} KB)")
    print(f"  금지 래퍼 태그 잔존: {bad or '없음'}")
    print(f"  외부 자원 {len(ext)}건 (전부 허용 호스트: {len(ext) == len(allowed)}) → {sorted(set(ext))[:3]}")
    print(f"  figure {len(re.findall(r'<figure', out))}점 · 인라인 SVG {len(re.findall(r'<svg ', out))}점")
    anchors = set(re.findall(r'\sid\s*=\s*["\']([^"\']+)', out))
    links = set(re.findall(r'href="#([^"]+)"', out))
    print(f"  내부 앵커 {len(links)}개 · 끊어진 링크 {len(links - anchors)}개")


if __name__ == "__main__":
    main()
