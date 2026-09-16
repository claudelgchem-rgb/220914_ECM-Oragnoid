# -*- coding: utf-8 -*-
"""수집된 서지·청구항에서 인용 메타 색인을 만든다.

이 색인이 있어야 '에이전트가 지어낸 DOI'를 기계적으로 걸러낼 수 있다.
ECMX-002에서 조작 인용 0건을 유지한 것이 이 장치 덕이었으므로 여기서도 먼저 세운다.
"""
import json, os, re

P = "/tmp/claude-0/-home-user-220914-ECM-Oragnoid/7409ae7d-4931-5788-bfd9-7819ccdb9274/scratchpad/ecmx"
OUT = "/mnt/user-data/outputs/ECMX2/tools/citemeta3.json"


def add(meta, key, rec):
    k = str(key or "").strip()
    if not k:
        return
    kl = k.lower()
    if kl in meta:
        for a, b in rec.items():
            if b and not meta[kl].get(a):
                meta[kl][a] = b
    else:
        meta[kl] = dict(rec)


def main():
    meta, ft = {}, set()
    for f in ("pool_col.json", "pool_med.json"):
        d = json.load(open(os.path.join(P, f), encoding="utf-8"))
        for doi, r in d.get("pool", {}).items():
            rec = {"kind": "paper", "doi": r.get("doi") or doi, "pmid": r.get("pmid", ""),
                   "pmcid": r.get("pmcid", ""), "title": r.get("title", ""),
                   "journal": r.get("journal", ""), "year": r.get("year", ""),
                   "authors": r.get("authors", ""), "cited": r.get("cited", 0)}
            add(meta, doi, rec)
            if r.get("pmid"):
                add(meta, r["pmid"], rec)
            if r.get("pmcid"):
                add(meta, r["pmcid"], rec)
    # 이전 조사에서 모은 풀도 인용 가능 범위에 포함
    ep = os.path.join(P, "evidence_pool.json")
    if os.path.exists(ep):
        d = json.load(open(ep, encoding="utf-8"))
        it = d.get("pool", d) if isinstance(d, dict) else d
        if isinstance(it, dict):
            for doi, r in it.items():
                if not isinstance(r, dict):
                    continue
                rec = {"kind": "paper", "doi": r.get("doi") or doi, "pmid": r.get("pmid", ""),
                       "pmcid": r.get("pmcid", ""), "title": r.get("title", ""),
                       "journal": r.get("journal", ""), "year": r.get("year", ""),
                       "authors": r.get("authors", ""), "cited": r.get("cited", 0)}
                add(meta, doi, rec)
                for a in ("pmid", "pmcid"):
                    if r.get(a):
                        add(meta, r[a], rec)
    # 전문 확인 표시
    for idx in ("ft3_index.json", "ft_index.json"):
        p = os.path.join(P, idx)
        if os.path.exists(p):
            d = json.load(open(p, encoding="utf-8"))
            for k in (d.keys() if isinstance(d, dict) else d):
                ft.add(str(k).upper())
    for k, r in meta.items():
        if r.get("pmcid") and str(r["pmcid"]).upper() in ft:
            r["ft"] = True
    # 특허
    for f in ("claims3.json", "fpo_claims.json"):
        p = os.path.join(P, f)
        if not os.path.exists(p):
            continue
        d = json.load(open(p, encoding="utf-8"))
        for pid, r in d.items():
            add(meta, pid, {"kind": "patent", "title": r.get("title", ""),
                            "assignee": r.get("assignee", ""),
                            "url": r.get("url", ""),
                            "year": (re.search(r"y(\d{4})", r.get("url", "")) or [None, ""])[1]})
    json.dump(meta, open(OUT, "w", encoding="utf-8"), ensure_ascii=False)
    kinds = {}
    for r in meta.values():
        kinds[r.get("kind")] = kinds.get(r.get("kind"), 0) + 1
    print("색인 키", len(meta), kinds, "전문", len(ft))


if __name__ == "__main__":
    main()
