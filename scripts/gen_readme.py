#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate README.md / README.zh-CN.md / assets/hot.svg from the data files.

    data/projects.json   ← the list itself (categories, entries, reasons)
    data/stars.json      ← refreshed by fetch_stars.py

⛔ Never hand-edit README.md. Any number in it comes from here.
Badges are live shields.io images, so star counts never go stale even
if this script is not run.
"""
import json, os, re, sys, html, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = lambda *p: os.path.join(ROOT, *p)

S = lambda n, f="stars": (
    f"https://img.shields.io/github/{f}/{n}?style=flat&logo=github&label=")


def badge(n):
    return (f'<img src="{S(n)}" alt="stars"> '
            f'<img src="{S(n, "created-at")}" alt="created">')


def anchors(cats):
    return " · ".join(
        f'<a href="#{c["id"]}">{c["emoji"]} {c["title_en"]}</a>' for c in cats)


def cell(s):
    """Sanitise a string for use inside a markdown table cell.

    🔴 表格单元格里这两样会静默破坏结构：
      `|`  直接把表格切成两列错位
      ```  未配对的反引号会把后面整段吞掉 —— 实测 realZachi/pg-jev 那条
           理由里有 `WHERE jev(tickets,'...')`，结果整条理由在 GitHub 上消失
    ⛔ 不能靠"写理由时小心点"，理由是人/agent 写的，必须在这里兜住。
    """
    if not s:
        return ""
    s = s.replace("|", "\\|")
    if s.count("`") % 2:
        s = s.replace("`", "'")
    return s


def body(cats, stars, zh):
    """Render the category sections. zh=False → English.

    🔴 用 markdown 表格，⛔ 不用一项目一行的列表。
    GitHub 的表格支持 `|:---|--:|` 列对齐语法，`<th align=left>` / `<td align=right>`
    在消毒后仍然保留（实测过）—— 这就是「名字靠左、徽章靠右、中间留白」的做法。
    列表做不到这一点，所有东西都会被挤到左边。

    🔴 每个块之间必须留空行。GFM 里裸 HTML 块（<h2>…</h2>）会一路吃到空行，
    紧跟其后的表格会被整段当成字面文本输出。实测过：漏一个空行，整节变纯文本。
    """
    out = []
    for c in cats:
        title = c["title_zh"] if zh else c["title_en"]
        note = c["note_zh"] if zh else c["note_en"]
        blk = [f'<h2 id="{c["id"]}">{c["emoji"]} {title} <sub>{len(c["items"])}</sub></h2>',
               "", f'<p><em>{note}</em></p>', "",
               "| 项目 | 星数 · 最近更新 |" if zh else "| Project | Stars · Updated |",
               "|:--------------------------------------------------------|--------------------:|"]
        for it in c["items"]:
            n = it["repo"]
            reason = it["reason_zh"] if zh else it["reason_en"]
            st = stars.get(n, {})
            left = f'**[{n}](https://github.com/{n})**'
            subs = []
            if st.get("created"):
                subs.append((("创建于 " if zh else "created ") + st["created"]))
            if reason:
                subs.append(cell(reason))
            if subs:
                left += "<br><sub>" + " · ".join(subs) + "</sub>"
            right = (f'<img src="{S(n)}" alt="stars"> '
                     f'<img src="{S(n, "last-commit")}" alt="updated">')
            blk.append(f'| {left} | {right} |')
        # 🔴 表格行之间只能有单个换行 —— 空行会把表格截断成一堆独立段落。
        #    块与块之间才用空行（见最后的 join）。
        out.append("\n".join(blk))
    return "\n\n".join(out)


def hot_table(stars, cats, zh=False):
    """Ranked by real stars. Computed, never written by hand."""
    known = {i["repo"] for c in cats for i in c["items"]}
    rows = sorted(((n, s) for n, s in stars.items() if n in known),
                  key=lambda kv: -kv[1].get("stars", 0))[:10]
    head = ("| # | 项目 | 星数 | 创建 |" if zh else "| # | Project | Stars | Created |")
    out = [head, "|--:|:--------------------------|--------------------:|------------------:|"]
    for i, (n, s) in enumerate(rows, 1):
        out.append(f'| {i} | **[{n}](https://github.com/{n})** '
                   f'| <img src="{S(n)}" alt="stars"> '
                   f'| <img src="{S(n, "created-at")}" alt="created"> |')
    return "\n".join(out)


def howto(cats, zh):
    if zh:
        return ("**想搞懂 Jev** → `browser-use/jev-ultrafast`。"
                "生态里最大的一次成本削减，看它怎么写那一次判定。\n\n"
                "**想明天就能用上** → Claude Code 上用 `tamaratran/fast-jev-compaction`，"
                "浏览器自动化用 `browser-use/jev-ultrafast`。\n\n"
                "**想自己做一个** → 从 `kerpopule/hermes-jev-skills` 起步，"
                "回路已经接好了。")
    return ("**Want to understand Jev** → `browser-use/jev-ultrafast`. "
            "The biggest cost cut in the ecosystem — read how the single decision is made.\n\n"
            "**Want to use it tomorrow** → `tamaratran/fast-jev-compaction` for Claude Code, "
            "`browser-use/jev-ultrafast` for browser automation.\n\n"
            "**Want to ship your own** → start from `kerpopule/hermes-jev-skills`; "
            "the loop is already wired.")


def render(cats, stars, zh):
    n_total = sum(len(c["items"]) for c in cats)
    n_with = sum(1 for c in cats for i in c["items"]
                 if (i["reason_zh"] if zh else i["reason_en"]))
    if zh:
        title = "awesome-jev-essentials"
        tag = "**真正值得你花时间的 Jev 项目** —— 挑过、比过、持续更新。"
        toc = "## 目录"
        hot_h = "## 📈 热门项目（按星数自动排序）"
        hot_note = (f"由 `scripts/gen_readme.py` 从 `data/stars.json` 生成。"
                    f"⛔ 不手写。星数即便脚本没跑也不会过期——徽章是实时的。")
        why_h = "## 🧭 怎么选"
        foot = ""
        lang = "**English** · [中文](README.zh-CN.md)"
    else:
        title = "awesome-jev-essentials"
        tag = "**The Jev projects actually worth your time** — picked, compared, kept current."
        toc = "## Contents"
        hot_h = "## 📈 Most starred (ranked automatically)"
        hot_note = (f"Generated by `scripts/gen_readme.py` from `data/stars.json`. "
                    f"⛔ Never hand-edited. Counts cannot go stale — the badges are live.")
        why_h = "## 🧭 How to choose"
        foot = ""
        lang = "**English** · [中文](README.zh-CN.md)"
    if zh:
        about = f"""这是一个**独立的、非官方**的 Jev 项目精选清单。与 TypeSafe AI 没有隶属关系，
也没有得到它的背书。

**它解决什么问题。** 搜 "Jev" 会出来上万个仓库，而其中大部分点进去是空的、
改名的、或者只是把官方文档抄了一遍。这一个清单的回答不是"Jev 是什么"
——那是[官方文档](https://docs.typesafe.ai)的活，而且它会变。
这里回答的是另一个问题：**这么多项目里，我该看哪个、为什么是它。**

**它和别的清单有什么不同。**

- 🔴 **每个条目都写了「为什么是它」** —— 不是从仓库名或描述里抄一句，
  是真的看过之后写的一句话。写不出这句的，不进列表。
- 📊 **星数和日期⛔ 不是手写的** —— 页面上的徽章是实时的，排序表由
  `data/stars.json` 生成。手写的数字第一个月就会错，而我们不会记得去改。
- 🔍 **死链会被脚本抓出来** —— 仓库没了的话，徽章只会安静地显示
  `repo not found`，如果没人顺手查，它会一直躺在那儿。`scripts/fetch_stars.py`
  对每个仓库打一次 API，拿不到的直接报错。

**收录 {n_total} 个，覆盖 {len(cats)} 类**；其中 {n_with} 个已经写了选它的理由，
剩下的在补 —— ⭐ **补理由这件事本身就是这个清单的内容**，不是收尾工作。

**关于 Jev**：它是 TypeSafe AI 出的 System One 模型 —— 不生成文本，
只在一组带类型的选项里做一次判定，几十到几百毫秒返回。
所有厂商自评的性能数字这里都标注了出处。

MIT 许可。收录标准见 [CONTRIBUTING.md](CONTRIBUTING.md)。
"""
    else:
        about = f"""An **independent, unaffiliated** catalog of Jev projects.
Not endorsed by, and not connected to, TypeSafe AI.

**The problem.** Searching for "Jev" returns tens of thousands of repositories,
and most of them are empty, renamed, or a copy of the official docs. This list
does not answer "what is Jev" — that is the job of the
[official documentation](https://docs.typesafe.ai), and it changes.
This answers the other question: **of all these projects, which one should I
look at, and why that one.**

**How it differs from the other catalogs.**

- 🔴 **Every entry says why it is here.** Not a line copied from the repo's own
  description — a sentence written after actually reading it. If we cannot write
  that sentence, the project does not go in.
- 📊 **No hand-written numbers.** The badges are live, and the ranking table is
  generated from `data/stars.json`. A hand-typed count is wrong within a month,
  and nobody remembers to go fix it.
- 🔍 **Dead links get caught by a script.** A deleted repo makes its badge say
  `repo not found`, quietly, forever, unless somebody happens to look.
  `scripts/fetch_stars.py` hits the API for every entry and fails loudly.

**{n_total} projects across {len(cats)} categories**; {n_with} have a written
reason and the rest are being written — ⭐ **writing those reasons is the
content of this list, not the cleanup afterwards.**

**On Jev:** it is TypeSafe AI's System One model. It does not generate text —
it returns a single decision over a set of typed options, in tens to hundreds of
milliseconds. Vendor-reported performance numbers are cited to their source.

MIT licensed. Inclusion criteria are in [CONTRIBUTING.md](CONTRIBUTING.md).
"""
    return f"""<p align="center">
  <img src="assets/banner.svg" alt="awesome-jev-essentials" width="100%">
</p>

# {title}

{tag}

{lang}

{toc}

{anchors(cats)} · <a href="#hot">📈 {"热门" if zh else "Most starred"}</a> · <a href="#choose">🧭 {"怎么选" if zh else "How to choose"}</a>

---

{body(cats, stars, zh)}

<h2 id="hot">{hot_h[3:]}</h2>

<em>{hot_note}</em>

{hot_table(stars, cats, zh)}

---

<h2 id="choose">{why_h[3:]}</h2>

{howto(cats, zh)}

---

### {"关于" if zh else "About"}

{about}"""


def main():
    cats = json.load(open(D("data", "projects.json")))["categories"]
    try:
        stars = json.load(open(D("data", "stars.json")))
    except FileNotFoundError:
        print("⚠️  data/stars.json 不在 —— 先跑 scripts/fetch_stars.py")
        stars = {}
    for lang, zh in (("README.md", False), ("README.zh-CN.md", True)):
        open(D(lang), "w").write(render(cats, stars, zh))
        print(f"✅ {lang}")
    os.makedirs(D("assets"), exist_ok=True)
    write_banner(cats, stars)


def write_banner(cats, stars):
    """Title image. The concept: many paths, only three lit — that is 'essentials'."""
    total = sum(len(c["items"]) for c in cats)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 300" width="1200" height="300" role="img" aria-label="awesome-jev-essentials">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#080b17"/><stop offset="50%" stop-color="#101529"/><stop offset="100%" stop-color="#171233"/>
    </linearGradient>
    <linearGradient id="acc" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#5eead4"/><stop offset="55%" stop-color="#8b9cf8"/><stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>
    <linearGradient id="acc2" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#5eead4" stop-opacity="0.8"/><stop offset="100%" stop-color="#818cf8" stop-opacity="0.5"/>
    </linearGradient>
    <radialGradient id="glow" cx="0.74" cy="0.5" r="0.48">
      <stop offset="0%" stop-color="#8b9cf8" stop-opacity="0.22"/><stop offset="100%" stop-color="#8b9cf8" stop-opacity="0"/>
    </radialGradient>
    <pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse">
      <path d="M24 0 H0 V24" fill="none" stroke="#ffffff" stroke-opacity="0.032" stroke-width="1"/>
    </pattern>
    <filter id="gl" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
    <filter id="gls" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="2.6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <rect width="1200" height="300" fill="url(#bg)"/>
  <rect width="1200" height="300" fill="url(#grid)"/>
  <rect width="1200" height="300" fill="url(#glow)"/>
  <g fill="none" stroke-linecap="round">
    <g stroke="#212a42" stroke-width="1.5">
      <path d="M812 150 C 880 150 930 34  1150 34"/><path d="M812 150 C 880 150 930 90  1150 90"/>
      <path d="M812 150 C 880 150 930 122 1150 122"/><path d="M812 150 C 880 150 930 178 1150 178"/>
      <path d="M812 150 C 880 150 930 210 1150 210"/><path d="M812 150 C 880 150 930 266 1150 266"/>
    </g>
    <g filter="url(#gl)">
      <path d="M812 150 C 880 150 930 62  1150 62"  stroke="url(#acc)" stroke-width="3.2" opacity="0.95"/>
      <path d="M812 150 C 880 150 930 150 1150 150" stroke="url(#acc)" stroke-width="3.2" opacity="0.95"/>
      <path d="M812 150 C 880 150 930 238 1150 238" stroke="url(#acc)" stroke-width="3.2" opacity="0.95"/>
    </g>
    <g stroke="url(#acc2)" stroke-width="1.7" opacity="0.55">
      <path d="M1002 62  C 1052 62  1062 44  1150 44"/><path d="M1002 62  C 1052 62  1062 80  1150 80"/>
      <path d="M1002 150 C 1052 150 1062 132 1150 132"/><path d="M1002 150 C 1052 150 1062 168 1150 168"/>
      <path d="M1002 238 C 1052 238 1062 220 1150 220"/><path d="M1002 238 C 1052 238 1062 256 1150 256"/>
    </g>
  </g>
  <circle cx="812" cy="150" r="16" fill="#080b17" stroke="url(#acc)" stroke-width="3" filter="url(#gls)"/>
  <circle cx="812" cy="150" r="5.5" fill="url(#acc)"/>
  <g filter="url(#gls)">
    <circle cx="1150" cy="62"  r="6" fill="#5eead4"/><circle cx="1150" cy="150" r="6" fill="#8b9cf8"/>
    <circle cx="1150" cy="238" r="6" fill="#c084fc"/>
  </g>
  <text x="72" y="118" font-family="ui-sans-serif,-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,PingFang SC,sans-serif"
        font-size="50" font-weight="700" fill="#f2f5ff" letter-spacing="-1.4">awesome-jev<tspan fill="#6b76a3">-</tspan><tspan fill="url(#acc)">essentials</tspan></text>
  <text x="74" y="160" font-family="ui-sans-serif,-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,PingFang SC,sans-serif"
        font-size="19" fill="#a9b3d6">The Jev projects actually worth your time.</text>
  <rect x="74" y="184" width="64" height="3" rx="1.5" fill="url(#acc)"/>
  <text x="74" y="216" font-family="ui-sans-serif,-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,PingFang SC,sans-serif"
        font-size="14.5" fill="#7a85ad">{total} projects, {len(cats)} categories. Not everything — just the ones we'd tell a friend to try.</text>
  <text x="74" y="246" font-family="ui-sans-serif,-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,PingFang SC,sans-serif"
        font-size="12.5" fill="#4e5878" letter-spacing="1.6">ENGLISH  ·  中文</text>
</svg>
'''
    open(D("assets", "banner.svg"), "w").write(svg)
    print("✅ assets/banner.svg")


if __name__ == "__main__":
    main()
