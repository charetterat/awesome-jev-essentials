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
            right = (f'<img src="{S(n)}" alt="stars"> <img src="{S(n, "last-commit")}" alt="updated">')
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
    """怎么选 —— 首屏那一栏。

    🔴 为什么是它、⛔ 不是星数榜：星数榜只答「谁星多」，而那把尺子我们
    自己已经测过**不预测价值**。这一栏按**你想干什么**分，是星数给不了的
    维度，也是唯一说得上「有人挑过」的地方。

    ⚠️ 曾经这里有一栏叫「编辑推荐」，实际是按星数取前 5 —— 和文末热门榜
    前 5 逐条相同、同序。**名字承诺人的判断，内容是机器排序**，属于
    「没人会去更新的结构化声明」。已删掉，把位置让给这一栏。
    """
    picks = (("If you want to understand Jev",
              "`browser-use/jev-ultrafast` — the biggest cost cut in the ecosystem; read how the single decision is made.",
              "想搞懂 Jev 到底在干什么",
              "`browser-use/jev-ultrafast` —— 生态里最大的一次成本削减，看那一次判定怎么做出来的。"),
             ("If you want to use it tomorrow",
              "`tamaratran/fast-jev-compaction` for Claude Code, `Ying-Kai-Liao/jev-browser` for browser work.",
              "想明天就能用上",
              "Claude Code 上用 `tamaratran/fast-jev-compaction`，浏览器操作上 `Ying-Kai-Liao/jev-browser`。"),
             ("If you want to run it yourself",
              "`Mapika/decider` — open weights, and a 「limits, stated plainly」 section.",
              "想不依赖官方 API 自己跑",
              "`Mapika/decider` —— 真给权重，而且自己写了「哪里不行」那一节。"),
             ("If you want to build on it",
              "start from `kerpopule/hermes-jev-skills`; the loop is already wired.",
              "想自己做一个",
              "从 `kerpopule/hermes-jev-skills` 起步，回路已经接好了。"))
    rows = [("| 你要是…… | 从这里开始 |" if zh else "| If you want to… | Start with |"),
            "|:--|:--|"]
    for en_h, en_b, zh_h, zh_b in picks:
        rows.append(f'| **{cell(zh_h if zh else en_h)}** | {cell(zh_b if zh else en_b)} |')
    return "\n".join(rows)


def contents_table(cats, zh):
    """目录做成表格。

    ⛔ 以前是一长串 `<a>…</a> · <a>…</a>` 内联排下来 —— emoji 紧挨着 emoji，
    在 GitHub 上的实际换行位置取决于窗口宽度，看着就是一团。
    表格每一类占一行，左边对齐、右边计数，扫一眼就知道有哪些类、各有几个。
    """
    rows = [("| | 分类 | 个数 |" if zh else "| | Category | Count |"),
            "|:--|:--------------------------|--:|"]
    for c in cats:
        t = c["title_zh"] if zh else c["title_en"]
        rows.append(f'| {c["emoji"]} | <a href="#{c["id"]}">{t}</a> '
                    f'| {len(c["items"])} |')
    tail = (f'| 📈 | <a href="#hot">热门项目</a> | — |'
            f'\n| 🧭 | <a href="#choose">怎么选</a> | — |') if zh else \
           (f'| 📈 | <a href="#hot">Most starred</a> | — |'
            f'\n| 🧭 | <a href="#choose">How to choose</a> | — |')
    return "\n".join(rows) + "\n" + tail


def render(cats, stars, zh):
    n_total = sum(len(c["items"]) for c in cats)
    n_with = sum(1 for c in cats for i in c["items"]
                 if (i["reason_zh"] if zh else i["reason_en"]))
    if zh:
        title = "awesome-jev-essentials"
        tag = "**真正值得你花时间的 Jev 项目** —— 挑过、比过、持续更新。"
        toc = "## 目录"
        hot_h = "## 📈 按星数排序（原始数据，自动生成）"
        hot_note = ("星数只说明有多少人点过星标，**不说明项目好不好用**。这里的排序纯粹是数字。"
                    "要看该选哪个，用上面的「怎么选」。")
        why_h = "## 🧭 怎么选"
        picks_h = "## ⭐ 编辑推荐"
        picks_note = ("**全列表里最多人验证过的几个**（按星数）。"
                      "完整的 84 条在下面按类别展开。")
        foot = ""
        lang = "**English** · [中文](README.zh-CN.md)"
    else:
        title = "awesome-jev-essentials"
        tag = "**The Jev projects actually worth your time** — picked, compared, kept current."
        toc = "## Contents"
        hot_h = "## 📈 Most starred (raw data, auto-sorted)"
        hot_note = ("Star count says how many people bookmarked something, **not whether it works**. "
                    "This ordering is nothing but that number. To pick one, use the table above.")
        why_h = "## 🧭 How to choose"
        picks_h = "## ⭐ Editor's picks"
        picks_note = ("**The most widely used entries in the list** (by stars). "
                      "All 84 are laid out by category below.")
        foot = ""
        lang = "**English** · [中文](README.zh-CN.md)"
    if zh:
        about = f"""这是一个**独立的、非官方**的 Jev 项目精选清单，收录 **{n_total} 个项目、{len(cats)} 个类别**。
与 TypeSafe AI 没有隶属关系，也没有得到它的背书。

搜 "Jev" 会出来上万个仓库，大部分点进去是空的、改名的、或者只是把官方文档抄了一遍。
**这个清单回答的不是「Jev 是什么」**——那是[官方文档](https://docs.typesafe.ai)的活，
而且它会变。这里回答的是另一个问题：**这么多项目里，我该看哪个、为什么是它。**

**凭什么信这份清单**：**每一条都配了一句手写的「为什么是它」。**
说不出这句的就不进来 —— ⭐⭐ **清单是 84 条而不是搜出来的上万条，差的就是这一条。**"""

        updates = """**这份清单会持续更新。** 会变的是这些：

- 🔄 **星数和最近更新日期是实时的。** 页面上每个数字都是徽章，不是写死的，
  所以不会过期。
- 📈 **排序表每天重排。** 新的会爬上来、停更的会掉下去，自己会动。
- 🔍 **死链会被清掉。** 被删或改名的仓库会被发现 ——
  ⚠️ 没有这一条的话，死链只会安静地挂在那儿，看起来一切正常。
- ✍️ **新条目要说得出理由才进得来。** 见 [CONTRIBUTING.md](CONTRIBUTING.md)，
  一句话概括：**说不出「为什么它在清单上」，它就不在。**"""

        about2 = """**关于 Jev**：它是 TypeSafe AI 出的 System One 模型 —— 不生成文本，
只在一组带类型的选项里做一次判定，几十到几百毫秒返回。
所有厂商自评的性能数字这里都标注了出处。MIT 许可。"""
    else:
        about = f"""An **independent, unaffiliated** catalog of Jev projects —
**{n_total} projects across {len(cats)} categories**. Not endorsed by,
and not connected to, TypeSafe AI.

Searching for "Jev" returns tens of thousands of repositories, and most of them
are empty, renamed, or a copy of the official docs. **This list does not answer
"what is Jev"** — that is the job of the
[official documentation](https://docs.typesafe.ai), and it changes.
It answers the other question: **of all these projects, which one should I look
at, and why that one.**

**What makes this one worth trusting:** every entry carries a hand-written
reason. There is no entry here that we could not say something specific about —
⭐⭐ **that is the editorial bar, and it is why the list is 84 and not the 10,000+
that a search returns.**"""

        updates = """**This list is maintained, not published once.** Here is what changes:

- 🔄 **Stars and last-commit dates are live.** Every count on this page is a
  badge, not a typed number, so it is never out of date.
- 📈 **The ranking table is re-sorted every day.** New projects climb, stale
  ones fall, on their own.
- 🔍 **Dead links get removed.** Deleted and renamed repos are caught
  automatically — ⚠️ without that, a dead entry just sits there looking fine.
- ✍️ **New entries have to earn their place.** See
  [CONTRIBUTING.md](CONTRIBUTING.md). The short version: **if we cannot say why
  a project is on this list, it does not go on.**"""

        about2 = """**On Jev:** it is TypeSafe AI's System One model. It does not generate
text — it returns a single decision over a set of typed options, in tens to
hundreds of milliseconds. Vendor-reported performance numbers are cited to their
source. MIT licensed."""
    return f"""<p align="center">
  <img src=".github/logo.png" alt="" width="96" height="96">
</p>

<p align="center">
  <img src="assets/banner.svg" alt="awesome-jev-essentials" width="100%">
</p>

# {title}

{tag}

{lang}

## {"这是什么" if zh else "What this is"}

{about}

<p>
{"不按星数排。这里按<strong>你想干什么</strong>分。" if zh else "Not by stars. By <strong>what you are trying to do</strong>."}
</p>

{howto(cats, zh)}

---

{toc}

{contents_table(cats, zh)}

---

{body(cats, stars, zh)}

<h2 id="hot">{hot_h[3:]}</h2>

<em>{hot_note}</em>

{hot_table(stars, cats, zh)}

---

---

### {"关于" if zh else "About"}

{about}

### {"会更新什么" if zh else "What updates"}

{updates}"""


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
