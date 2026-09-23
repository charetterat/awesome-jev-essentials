#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Refresh data/stars.json from the GitHub API.

    GITHUB_TOKEN=... python3 scripts/fetch_stars.py

Why this exists: README.md must contain no hand-written numbers.
The star counts there are live shields.io badges, so they survive not
running this. This script fills the ranking table's data and the
created-at dates.
"""
import json, os, re, sys, time, urllib.request, urllib.error

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOK = os.environ.get("GITHUB_TOKEN", "")
if not TOK:
    env = os.path.expanduser("~/.acp/secrets/github.env")
    if os.path.exists(env):
        m = re.search(r"GITHUB_TOKEN=(\S+)", open(env).read())
        TOK = m.group(1) if m else ""
H = {"User-Agent": "awesome-jev-essentials", "Accept": "application/vnd.github+json"}
if TOK:
    H["Authorization"] = f"Bearer {TOK}"


def api(path):
    r = urllib.request.Request("https://api.github.com" + path, headers=H)
    try:
        x = urllib.request.urlopen(r)
        raw = x.read()
        return x.status, (json.loads(raw) if raw else None)
    except urllib.error.HTTPError as e:
        return e.code, None


def main():
    proj = json.load(open(os.path.join(ROOT, "data", "projects.json")))
    full = [i["repo"] for c in proj["categories"] for i in c["items"]]
    out, miss = {}, []
    for n in full:
        c, r = api("/repos/" + n)
        if c == 200:
            out[n] = {"stars": r["stargazers_count"], "created": r["created_at"][:10],
                      "pushed": r["pushed_at"][:10], "lang": r.get("language"),
                      "archived": r["archived"],
                      "desc": (r.get("description") or "")[:160]}
        else:
            # 🔴 404 = 仓库/账号没了。这条必须报出来 —— 徽章会在页面上
            #    显示 "repo not found"，而它是静默的，没人会顺手去查。
            miss.append((n, c))
        time.sleep(0.05)
    json.dump(out, open(os.path.join(ROOT, "data", "stars.json"), "w"),
              ensure_ascii=False, indent=2)
    print(f"✅ {len(out)}/{len(full)} 个抓到 -> data/stars.json")
    if miss:
        print(f"🔴 {len(miss)} 个抓不到（仓库已删或改名，需要从清单里拿掉）：")
        for n, c in miss:
            print(f"     HTTP {c}  {n}")
    top = sorted(out.items(), key=lambda kv: -kv[1]["stars"])[:10]
    for i, (k, v) in enumerate(top, 1):
        print(f"  {i:>2}. {k:<46} {v['stars']:>7}★")


if __name__ == "__main__":
    main()
