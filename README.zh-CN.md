<p align="center">
  <img src="assets/banner.svg" alt="awesome-jev-essentials" width="100%">
</p>

# awesome-jev-essentials

**真正值得你花时间的 Jev 项目** —— 挑过、比过、持续更新。

**English** · [中文](README.zh-CN.md)

## 这是什么

这是一个**独立的、非官方**的 Jev 项目精选清单，收录 **84 个项目、12 个类别**。
与 TypeSafe AI 没有隶属关系，也没有得到它的背书。

搜 "Jev" 会出来上万个仓库，大部分点进去是空的、改名的、或者只是把官方文档抄了一遍。
**这个清单回答的不是「Jev 是什么」**——那是[官方文档](https://docs.typesafe.ai)的活，
而且它会变。这里回答的是另一个问题：**这么多项目里，我该看哪个、为什么是它。**

## 会更新什么

**这份清单会持续更新。** 说清楚它更新什么、不更新什么：

- 🔄 **星数和最近更新日期是实时的** —— 页面上全部是徽章，不是写死的数字，
  每次打开都会变。⛔ 也因此永远不会过期。
- 🤖 **排序表每天自动重算** —— 每天 03:17 由 GitHub Actions 跑
  `scripts/fetch_stars.py` + `scripts/gen_readme.py` 重排 📈 热门榜。
- 🔍 **死链每天被脚本查一遍** —— 仓库被删或改名会被直接报出来。
  ⚠️ 这一条不加脚本的话会**静默失败**：徽章只是安静地显示 `repo not found`，
  没人顺手去查的话它会一直躺在那儿。
- ✍️ **新条目要过收录标准** —— 见 [CONTRIBUTING.md](CONTRIBUTING.md)。
  一句话概括：**写不出「为什么是它」的项目不进列表。**

---

## 目录

| | 分类 | 个数 |
|:--|:--------------------------|--:|
| 🚦 | <a href="#route">路由与分类</a> | 8 |
| 🛡 | <a href="#guard">守门与验证</a> | 7 |
| 🗜 | <a href="#compact">压缩与上下文</a> | 4 |
| 🧩 | <a href="#skills">技能与智能体</a> | 7 |
| ⚖️ | <a href="#score">打分与排序</a> | 3 |
| 🔎 | <a href="#code">代码搜索与评审</a> | 5 |
| 🌐 | <a href="#browser">浏览器与电脑操作</a> | 4 |
| 🖥 | <a href="#apps">应用与界面</a> | 8 |
| 🔌 | <a href="#infra">基础设施、SDK 与桥接</a> | 11 |
| 🔬 | <a href="#open">开源复现与替代</a> | 10 |
| 📐 | <a href="#eval">评测与基准</a> | 5 |
| 🎯 | <a href="#domain">垂直应用</a> | 12 |
| 📈 | <a href="#hot">热门项目</a> | — |
| 🧭 | <a href="#choose">怎么选</a> | — |

---

## ⭐ 编辑推荐

<em>**全列表里最多人验证过的几个**（按星数）。完整的 84 条在下面按类别展开。</em>

| 项目 | 星数 | 为什么是它 |
|:-----------------------|--------------------:|:--|
| **[browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast)** | <img src="https://img.shields.io/github/stars/browser-use/jev-ultrafast?style=flat&logo=github&label=" alt="stars"> | 用一次类型化判定替代每一步的 LLM 调用。**生态里最大的一次成本削减**——过去每一步要一次完整模型调用，现在只要一次 Jev 调用。 |
| **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | <img src="https://img.shields.io/github/stars/tamaratran/fast-jev-compaction?style=flat&logo=github&label=" alt="stars"> | 一个 Claude Code 插件，压缩前先给每次工具调用打分。它蹭的是现成的用户群，而不是自己攒一个。 |
| **[jaredpalmer/kev](https://github.com/jaredpalmer/kev)** | <img src="https://img.shields.io/github/stars/jaredpalmer/kev?style=flat&logo=github&label=" alt="stars"> | 0.8B/4B/9B 三个尺寸，训练代码和冻结评测集都给；报 95% 置信区间、测试集每个 checkpoint 只读一次，还直说和 Jev 的对比不是受控实验。 |
| **[jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** | <img src="https://img.shields.io/github/stars/jev-chat/jev-chat-jarvis?style=flat&logo=github&label=" alt="stars"> | 手机端的微信 / QQ / X / 飞书副驾。延迟低到能跟上真人对话——这正是 System One 在这里的意义。 |
| **[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)** | <img src="https://img.shields.io/github/stars/jarrodwatts/jev-trader?style=flat&logo=github&label=" alt="stars"> | 每个 Monad 区块做一次决策。快到能塞进一个区块里，便宜到能每次都跑。 |

---

<h2 id="route">🚦 路由与分类 <sub>8</sub></h2>

<p><em>先判断这是什么请求，再决定怎么处理。</em></p>

| 项目 | 星数 · 最近更新 |
|:--------------------------------------------------------|--------------------:|
| **[gargpratyush/jev-router](https://github.com/gargpratyush/jev-router)**<br><sub>创建于 2026-09-16 · 在 Claude Code 和 Codex 里逐轮选路：简单活给快档，难活给强档，而两个 CLI 的界面、工具、会话、登录方式一律不动。属于「装上就用」的那种路由器。</sub> | <img src="https://img.shields.io/github/stars/gargpratyush/jev-router?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/gargpratyush/jev-router?style=flat&logo=github&label=" alt="updated"> |
| **[prismhq/jev-router](https://github.com/prismhq/jev-router)**<br><sub>创建于 2026-09-17 · 服务端路由器：客户端只发一个模型 id，由 Jev 决定这次请求交给哪个模型。传输层用 LiteLLM，所以它是接进你现有的网关，而不是替换掉它。</sub> | <img src="https://img.shields.io/github/stars/prismhq/jev-router?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/prismhq/jev-router?style=flat&logo=github&label=" alt="updated"> |
| **[miniLV/Jev-Auto-Router](https://github.com/miniLV/Jev-Auto-Router)**<br><sub>创建于 2026-08-01 · 中文项目，而且难得地诚实：README 明写架构已定、运行时还在原型验证阶段，并提醒不要把设计当成分投产的安装说明。这种坦白很少见。</sub> | <img src="https://img.shields.io/github/stars/miniLV/Jev-Auto-Router?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/miniLV/Jev-Auto-Router?style=flat&logo=github&label=" alt="updated"> |
| **[shimo4228/jev-skill-router](https://github.com/shimo4228/jev-skill-router)**<br><sub>创建于 2026-09-21 · 作者做完、跑过，然后**在 README 里写明：作为路由器它大概率帮不了强模型**。默认影子模式，你可以先看它怎么判的，再决定要不要信。</sub> | <img src="https://img.shields.io/github/stars/shimo4228/jev-skill-router?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/shimo4228/jev-skill-router?style=flat&logo=github&label=" alt="updated"> |
| **[GodsBoy/jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router)**<br><sub>创建于 2026-09-16 · 带实测数字：72 个合成请求里路由对了 68 个，词法基线是 70.8%；同时自己标注「探索性结果、复用了数据」。把结论和局限写在一起，这点值得学。</sub> | <img src="https://img.shields.io/github/stars/GodsBoy/jev-agent-skill-router?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/GodsBoy/jev-agent-skill-router?style=flat&logo=github&label=" alt="updated"> |
| **[jekozyra/pi-typesafe-router](https://github.com/jekozyra/pi-typesafe-router)**<br><sub>创建于 2026-09-18 · 一句话一个职责：判断请求类型，路由到对应模型。README 第二行就提醒你——别和别的自动路由器同时开。</sub> | <img src="https://img.shields.io/github/stars/jekozyra/pi-typesafe-router?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/jekozyra/pi-typesafe-router?style=flat&logo=github&label=" alt="updated"> |
| **[adarshmishra07/jcm-router](https://github.com/adarshmishra07/jcm-router)**<br><sub>创建于 2026-09-17 · 本地代理，逐消息选模型和推理档位，会给子智能体选路，但**刻意不碰你已缓存的主对话**。原有的订阅登录照常可用。</sub> | <img src="https://img.shields.io/github/stars/adarshmishra07/jcm-router?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/adarshmishra07/jcm-router?style=flat&logo=github&label=" alt="updated"> |
| **[mejiasd3v/pi-jev-router](https://github.com/mejiasd3v/pi-jev-router)**<br><sub>创建于 2026-09-17 · 最小可用版：Jev 每个会话选一次模型，然后固定住。不做逐轮切换——如果你不喜欢模型在自己脚下被换掉，这是更合理的默认。</sub> | <img src="https://img.shields.io/github/stars/mejiasd3v/pi-jev-router?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/mejiasd3v/pi-jev-router?style=flat&logo=github&label=" alt="updated"> |

<h2 id="guard">🛡 守门与验证 <sub>7</sub></h2>

<p><em>在坏动作（和坏结论）落地前拦住它。</em></p>

| 项目 | 星数 · 最近更新 |
|:--------------------------------------------------------|--------------------:|
| **[leepokai/jev-guard](https://github.com/leepokai/jev-guard)**<br><sub>创建于 2026-09-17 · 每次工具调用执行前先打分。小而专一——护栏就该是这个体量。</sub> | <img src="https://img.shields.io/github/stars/leepokai/jev-guard?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/leepokai/jev-guard?style=flat&logo=github&label=" alt="updated"> |
| **[y0usaf/pi-jev](https://github.com/y0usaf/pi-jev)**<br><sub>创建于 2026-09-16 · 一个真被人测过的工具调用闸门，是这一类里被引用最多的起点。</sub> | <img src="https://img.shields.io/github/stars/y0usaf/pi-jev?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/y0usaf/pi-jev?style=flat&logo=github&label=" alt="updated"> |
| **[qkal/Canny](https://github.com/qkal/Canny)**<br><sub>创建于 2026-09-11 · 拦住智能体拿不出证据就说「做完了」。它防的是坏**结论**而不是坏动作——这是大多数护栏都没管的失败模式。</sub> | <img src="https://img.shields.io/github/stars/qkal/Canny?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/qkal/Canny?style=flat&logo=github&label=" alt="updated"> |
| **[jesset/pi-verdict](https://github.com/jesset/pi-verdict)**<br><sub>创建于 2026-08-25 · 约 1 千行的权限闸门，模仿 Claude Code 的 auto 模式。内置危险规则 + 你自己的允许/拒绝清单，先零延迟地解决掉明显的情况；只有真正含糊的才花一次模型调用。</sub> | <img src="https://img.shields.io/github/stars/jesset/pi-verdict?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/jesset/pi-verdict?style=flat&logo=github&label=" alt="updated"> |
| **[raihankhan-rk/diffjury](https://github.com/raihankhan-rk/diffjury)**<br><sub>创建于 2026-09-17 · 贴一个 PR 链接，由 Jev 判断这次改动有没有风险。它做成了能直接用的页面而不是一个库——这一类里最容易上手试的一个。</sub> | <img src="https://img.shields.io/github/stars/raihankhan-rk/diffjury?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/raihankhan-rk/diffjury?style=flat&logo=github&label=" alt="updated"> |
| **[DanRWilloughby/snifftest](https://github.com/DanRWilloughby/snifftest)**<br><sub>创建于 2026-09-17 · 查「AI 味」的文稿检查器：零依赖、规则可数，只在规则判断不了的地方加一次模型判定。**确定性检查 + 模型判断**怎么配合，这里是个干净的例子。</sub> | <img src="https://img.shields.io/github/stars/DanRWilloughby/snifftest?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/DanRWilloughby/snifftest?style=flat&logo=github&label=" alt="updated"> |
| **[GhalebDweikat/winnow](https://github.com/GhalebDweikat/winnow)**<br><sub>创建于 2026-09-16 · Claude Code 的 hook：把每个大 tool result 切成约 25 行一块，一次批量问 Jev 每块「这次任务用得上吗」，判定用不上的换成可随时取回的 stub。难得的是它把不好看的实测也贴出来——ECE 0.14 对基线 0.31、中位 86ms、300 个 case 花 $0.036，校准表里 Jev 给 0.07 的那一档实际需要率仍有 0.26；而且坚持 ECE 和 ROC AUC 并排报，因为只会答基准率的判官 ECE 很漂亮却什么都藏不掉。</sub> | <img src="https://img.shields.io/github/stars/GhalebDweikat/winnow?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/GhalebDweikat/winnow?style=flat&logo=github&label=" alt="updated"> |

<h2 id="compact">🗜 压缩与上下文 <sub>4</sub></h2>

<p><em>窗口满了，决定丢掉什么。</em></p>

| 项目 | 星数 · 最近更新 |
|:--------------------------------------------------------|--------------------:|
| **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)**<br><sub>创建于 2026-09-17 · 一个 Claude Code 插件，压缩前先给每次工具调用打分。它蹭的是现成的用户群，而不是自己攒一个。</sub> | <img src="https://img.shields.io/github/stars/tamaratran/fast-jev-compaction?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/tamaratran/fast-jev-compaction?style=flat&logo=github&label=" alt="updated"> |
| **[tamaratran/jev-pruner](https://github.com/tamaratran/jev-pruner)**<br><sub>创建于 2026-09-18 · 命令跑完、结果还没送到模型之前，先把冗长的 Bash 输出削掉。省下来的**是真的上下文，不是摘要出来的近似物**。</sub> | <img src="https://img.shields.io/github/stars/tamaratran/jev-pruner?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/tamaratran/jev-pruner?style=flat&logo=github&label=" alt="updated"> |
| **[joelhooks/pi-fast-jev-compaction](https://github.com/joelhooks/pi-fast-jev-compaction)**<br><sub>创建于 2026-09-18 · 对话正文原样保留，只清理过期的工具调用记录。而且说得很直白：**只做第一层**——不摘要、不改写、不编造记忆。</sub> | <img src="https://img.shields.io/github/stars/joelhooks/pi-fast-jev-compaction?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/joelhooks/pi-fast-jev-compaction?style=flat&logo=github&label=" alt="updated"> |
| **[leonaaardob/fast-dev-compaction](https://github.com/leonaaardob/fast-dev-compaction)**<br><sub>创建于 2026-09-18 · 把 Claude Code 那个压缩插件移植到 Codex 的生命周期钩子上：给每次工具调用打分、压缩、再把 Jev 判定要留的原样历史重新注入。</sub> | <img src="https://img.shields.io/github/stars/leonaaardob/fast-dev-compaction?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/leonaaardob/fast-dev-compaction?style=flat&logo=github&label=" alt="updated"> |

<h2 id="skills">🧩 技能与智能体 <sub>7</sub></h2>

<p><em>插进智能体回路里的零件，不是成品应用。</em></p>

| 项目 | 星数 · 最近更新 |
|:--------------------------------------------------------|--------------------:|
| **[safzanpirani/pi-jev-skill-picker](https://github.com/safzanpirani/pi-jev-skill-picker)**<br><sub>创建于 2026-09-20 · 把系统提示里整份技能目录换成一个排序工具。装了再多技能，也不再是每一轮都要为那份目录付 token。</sub> | <img src="https://img.shields.io/github/stars/safzanpirani/pi-jev-skill-picker?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/safzanpirani/pi-jev-skill-picker?style=flat&logo=github&label=" alt="updated"> |
| **[yuyang2230/jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)**<br><sub>创建于 2026-09-19 · 把高频小判断（分类/初筛/打分/核查）卸到 Jev 的免费档上，主模型只负责生成。中文文档，而且把成本账算给你看。</sub> | <img src="https://img.shields.io/github/stars/yuyang2230/jev-agent-skill?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/yuyang2230/jev-agent-skill?style=flat&logo=github&label=" alt="updated"> |
| **[HyunjunJeon/pi-quiet-ask](https://github.com/HyunjunJeon/pi-quiet-ask)**<br><sub>创建于 2026-09-17 · 把 Jev 当成安静的决策层：主模型继续写代码，由 Jev 回答框架必须问的那些封闭式问题，约 250 毫秒一次。</sub> | <img src="https://img.shields.io/github/stars/HyunjunJeon/pi-quiet-ask?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/HyunjunJeon/pi-quiet-ask?style=flat&logo=github&label=" alt="updated"> |
| **[kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)**<br><sub>创建于 2026-09-18 · 路由、记忆、压缩、技能选择全都有。是把 Jev 放进智能体回路里（而不是挂在旁边）最完整的一个例子。</sub> | <img src="https://img.shields.io/github/stars/kerpopule/hermes-jev-skills?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/kerpopule/hermes-jev-skills?style=flat&logo=github&label=" alt="updated"> |
| **[dbreunig/building-with-jev-skill](https://github.com/dbreunig/building-with-jev-skill)**<br><sub>创建于 2026-09-17 · 教 agent 怎么「设计 Jev 的问题」而不是怎么调 API：按代码要分支的方式选 primitive、一个问题只问一个属性、共享同一个 state 的问题合并成一次请求，还点明 noul 的 0.5 是「不确定」不是「中等」。明确标了只针对 jev-1.13，模型升版要回去重读 jaggedness 那页。</sub> | <img src="https://img.shields.io/github/stars/dbreunig/building-with-jev-skill?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/dbreunig/building-with-jev-skill?style=flat&logo=github&label=" alt="updated"> |
| **[kitze/skillbox](https://github.com/kitze/skillbox)**<br><sub>创建于 2026-09-17 · 自托管、带版本的 skills 库，通过 MCP 提供，Jev 只用在一件事上：拿当前任务给已启用的 skill 目录打分，把该用的挑出来。看点在接入细节——TypeSafe 直连 / Vercel AI Gateway / OpenRouter 的 /alpha/decisions 三选一，目录按 32 个 skill、24KB 一批在 8 秒内跑完，任一批失败就整体回退到确定性搜索，绝不返回半截排序。</sub> | <img src="https://img.shields.io/github/stars/kitze/skillbox?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/kitze/skillbox?style=flat&logo=github&label=" alt="updated"> |
| **[altryne/jevify](https://github.com/altryne/jevify)**<br><sub>创建于 2026-09-17 · 两种用法：日常干活时，它让 agent 把批量语义判断（扫长文档、排候选、逐条检查）先丢给 Jev，再把选中的证据读进推理上下文；直接说「jevify 这个代码库」，它会去找重复的 LLM 判断和脆弱的语义启发式，并把该换成 Jev 的问题写出来。README 也说清了这是社区 skill、不是 TypeSafe 官方产品，装了也不会自动拦截 tool 输出。</sub> | <img src="https://img.shields.io/github/stars/altryne/jevify?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/altryne/jevify?style=flat&logo=github&label=" alt="updated"> |

<h2 id="score">⚖️ 打分与排序 <sub>3</sub></h2>

<p><em>把判断变成一个能排序的数字。</em></p>

| 项目 | 星数 · 最近更新 |
|:--------------------------------------------------------|--------------------:|
| **[ruban-24/switchboard](https://github.com/ruban-24/switchboard)**<br><sub>创建于 2026-09-20 · 由你自己的策略驱动的模型选择：Jev 只做任务评估，**如何解读这个评估由你的规则决定**。把判断和策略分开，这个形状是对的。</sub> | <img src="https://img.shields.io/github/stars/ruban-24/switchboard?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/ruban-24/switchboard?style=flat&logo=github&label=" alt="updated"> |
| **[compozy/yoshi](https://github.com/compozy/yoshi)**<br><sub>创建于 2026-09-18 · 上下文裁剪代理：超过大小闸门才判定一次，然后按验证过的结论做删减，同时保持协议完整。README 里的说法是**量出来的，不是断言的**。</sub> | <img src="https://img.shields.io/github/stars/compozy/yoshi?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/compozy/yoshi?style=flat&logo=github&label=" alt="updated"> |
| **[shiftynick/jev-axi](https://github.com/shiftynick/jev-axi)**<br><sub>创建于 2026-09-16 · 给智能体用的 Jev 命令行：选、评、查、排、分流、守门——类型化判定实际就那么几种形状，它把这几种做成了 shell 命令。</sub> | <img src="https://img.shields.io/github/stars/shiftynick/jev-axi?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/shiftynick/jev-axi?style=flat&logo=github&label=" alt="updated"> |

<h2 id="code">🔎 代码搜索与评审 <sub>5</sub></h2>

<p><em>按「意思」而不是「字面」来找代码、判代码。</em></p>

| 项目 | 星数 · 最近更新 |
|:--------------------------------------------------------|--------------------:|
| **[uehaj/jev-semgrep](https://github.com/uehaj/jev-semgrep)**<br><sub>创建于 2026-09-19 · 按命题而非主题给每行打分：「顾客在要求退款」会排除余弦相似度近 1 的退款政策行。作者也坦承没有索引，每次查询都要重读整个语料。</sub> | <img src="https://img.shields.io/github/stars/uehaj/jev-semgrep?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/uehaj/jev-semgrep?style=flat&logo=github&label=" alt="updated"> |
| **[NiazMorshed2007/jev-review](https://github.com/NiazMorshed2007/jev-review)**<br><sub>创建于 2026-09-17 · 以 MCP 给编码 agent 19 个质量维度的 1-10 分和置信度，刻意不给综合分、也不给文字解释——找原因仍是 agent 自己的事。</sub> | <img src="https://img.shields.io/github/stars/NiazMorshed2007/jev-review?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/NiazMorshed2007/jev-review?style=flat&logo=github&label=" alt="updated"> |
| **[nassim-arifette/jevgrep](https://github.com/nassim-arifette/jevgrep)**<br><sub>创建于 2026-09-20 · 返回带路径和行号的真实源码片段而非摘要，`inspect` 可离线预览哪些内容会外发。难得坦白：README 自认三个 provider 里有两个从未真机跑通。</sub> | <img src="https://img.shields.io/github/stars/nassim-arifette/jevgrep?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/nassim-arifette/jevgrep?style=flat&logo=github&label=" alt="updated"> |
| **[devagrawal09/jev-review](https://github.com/devagrawal09/jev-review)**<br><sub>创建于 2026-09-16 · 代码审查工具，编排全留在 TypeScript 里，Jev 只在固定管线上做有界判断：Noul 风险矩阵 → Choice/Score 文件画像 → 证据选取 → 机制分类 → 严重度 → 条件式审查者路由，阈值写在代码里而不是 prompt 里。作者也明说这是实验品，产出的是「值得看一眼的线索」而非缺陷证明。</sub> | <img src="https://img.shields.io/github/stars/devagrawal09/jev-review?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/devagrawal09/jev-review?style=flat&logo=github&label=" alt="updated"> |
| **[can1357/jegrep](https://github.com/can1357/jegrep)**<br><sub>创建于 2026-09-19 · 自然语言搜代码，但不建 embedding、不建索引、不起常驻进程：每次直接走实时目录树，对每个路径向 Jev 要一个校准过的 yes/no，所以阈值跨批次是可比的。输出是 dirname/file:起-止 行号，能直接粘进编辑器；全仓搜一次约 $0.01–0.03。默认 cascade 不合用的话，src/strategies/ 里还有十来种可插拔探索策略。</sub> | <img src="https://img.shields.io/github/stars/can1357/jegrep?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/can1357/jegrep?style=flat&logo=github&label=" alt="updated"> |

<h2 id="browser">🌐 浏览器与电脑操作 <sub>4</sub></h2>

<p><em>驱动真实界面，而每一步的判定都做得很便宜。</em></p>

| 项目 | 星数 · 最近更新 |
|:--------------------------------------------------------|--------------------:|
| **[Ying-Kai-Liao/jev-browser](https://github.com/Ying-Kai-Liao/jev-browser)**<br><sub>创建于 2026-09-16 · LLM 只说这一步要达成什么，元素、动作、取值和是否完成全由一次 ~300ms 的 Jev 调用决定；42 个真实网站任务对 40 个，零假 done，token 用量 8k vs 557k。</sub> | <img src="https://img.shields.io/github/stars/Ying-Kai-Liao/jev-browser?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/Ying-Kai-Liao/jev-browser?style=flat&logo=github&label=" alt="updated"> |
| **[wy-coliney/jev-browser-use](https://github.com/wy-coliney/jev-browser-use)**<br><sub>创建于 2026-09-18 · 在 Codex 已有的 Computer Use 连接里，由 Jev 从 accessibility text 中挑点击和滚动，每次点击不再回主模型；打字和验证仍归 Codex。5-10x 作者自己标注为近似值。</sub> | <img src="https://img.shields.io/github/stars/wy-coliney/jev-browser-use?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/wy-coliney/jev-browser-use?style=flat&logo=github&label=" alt="updated"> |
| **[moritzkremb/jev-voice-browser](https://github.com/moritzkremb/jev-voice-browser)**<br><sub>创建于 2026-09-17 · 每个语音中间结果只发一次 Jev 请求，并行问约 10 个 typed question——含「这话是对我说的吗」「会不会造成破坏」——所以你话没说完它已动手。实测 34/34、约 330ms、整个 demo 一美分。</sub> | <img src="https://img.shields.io/github/stars/moritzkremb/jev-voice-browser?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/moritzkremb/jev-voice-browser?style=flat&logo=github&label=" alt="updated"> |
| **[jkudish/jev-browser](https://github.com/jkudish/jev-browser)**<br><sub>创建于 2026-09-17 · 每步由 Jev 选一个动作，另外单独给「目标达成」和「卡住」打分，预算和停止条件交给代码。维基 Coffee→Espresso 约 4 秒、$0.0016；密码脱敏做不到什么也写得很直白。</sub> | <img src="https://img.shields.io/github/stars/jkudish/jev-browser?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/jkudish/jev-browser?style=flat&logo=github&label=" alt="updated"> |

<h2 id="apps">🖥 应用与界面 <sub>8</sub></h2>

<p><em>能直接打开用的成品。</em></p>

| 项目 | 星数 · 最近更新 |
|:--------------------------------------------------------|--------------------:|
| **[browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast)**<br><sub>创建于 2026-09-16 · 用一次类型化判定替代每一步的 LLM 调用。**生态里最大的一次成本削减**——过去每一步要一次完整模型调用，现在只要一次 Jev 调用。</sub> | <img src="https://img.shields.io/github/stars/browser-use/jev-ultrafast?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/browser-use/jev-ultrafast?style=flat&logo=github&label=" alt="updated"> |
| **[jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)**<br><sub>创建于 2026-09-21 · 手机端的微信 / QQ / X / 飞书副驾。延迟低到能跟上真人对话——这正是 System One 在这里的意义。</sub> | <img src="https://img.shields.io/github/stars/jev-chat/jev-chat-jarvis?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/jev-chat/jev-chat-jarvis?style=flat&logo=github&label=" alt="updated"> |
| **[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)**<br><sub>创建于 2026-09-16 · 每个 Monad 区块做一次决策。快到能塞进一个区块里，便宜到能每次都跑。</sub> | <img src="https://img.shields.io/github/stars/jarrodwatts/jev-trader?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/jarrodwatts/jev-trader?style=flat&logo=github&label=" alt="updated"> |
| **[Sac-Y/Jev-cu](https://github.com/Sac-Y/Jev-cu)**<br><sub>创建于 2026-09-18 · 电脑操作（computer use）。这里最接近通用桌面智能体的一个。</sub> | <img src="https://img.shields.io/github/stars/Sac-Y/Jev-cu?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/Sac-Y/Jev-cu?style=flat&logo=github&label=" alt="updated"> |
| **[yikangy873-gif/jev-desktop](https://github.com/yikangy873-gif/jev-desktop)**<br><sub>创建于 2026-09-19 · Codex 负责理解目标、准备文本、核对结果；Jev 在一次请求里选定动作和目标。**规划与判定各归各**，这个切分很干净。</sub> | <img src="https://img.shields.io/github/stars/yikangy873-gif/jev-desktop?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/yikangy873-gif/jev-desktop?style=flat&logo=github&label=" alt="updated"> |
| **[AboveColin/HA-Jev](https://github.com/AboveColin/HA-Jev)**<br><sub>创建于 2026-09-17 · 把 Jev 的答案变成 Home Assistant 的传感器，自动化流程就能像读别的数值一样读一个概率。顺便印证了一件事：决策模型根本不需要聊天界面。</sub> | <img src="https://img.shields.io/github/stars/AboveColin/HA-Jev?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/AboveColin/HA-Jev?style=flat&logo=github&label=" alt="updated"> |
| **[thruwire/foreman](https://github.com/thruwire/foreman)**<br><sub>创建于 2026-09-17 · 在较慢的编码智能体之上放一层快速判定：喂给它一个工单或 bug 报告，由它决定下一步谁做什么。</sub> | <img src="https://img.shields.io/github/stars/thruwire/foreman?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/thruwire/foreman?style=flat&logo=github&label=" alt="updated"> |
| **[Silbercue/public-browser](https://github.com/Silbercue/public-browser)**<br><sub>创建于 2026-04-07 · 让 Claude Code 和 Cursor 驱动你**真的已经登录**的 Chrome，并给出实测差值：token 更少、工具调用更少、工具定义也更少。</sub> | <img src="https://img.shields.io/github/stars/Silbercue/public-browser?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/Silbercue/public-browser?style=flat&logo=github&label=" alt="updated"> |

<h2 id="infra">🔌 基础设施、SDK 与桥接 <sub>11</sub></h2>

<p><em>把 Jev 接进你现有的技术栈。</em></p>

| 项目 | 星数 · 最近更新 |
|:--------------------------------------------------------|--------------------:|
| **[burnigtm/jev-mcp](https://github.com/burnigtm/jev-mcp)**<br><sub>创建于 2026-09-17 · 本地 stdio 的 MCP 服务器，把 Jev 暴露成类型化判定；其中路由下一个步骤的工具，会在同一次请求里把要调用的东西一起选好。</sub> | <img src="https://img.shields.io/github/stars/burnigtm/jev-mcp?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/burnigtm/jev-mcp?style=flat&logo=github&label=" alt="updated"> |
| **[tacticocc/Jevbridge](https://github.com/tacticocc/Jevbridge)**<br><sub>创建于 2026-09-18 · ACP + MCP 适配器，把 Jev 和 Codex、Claude、Grok、OpenCode 摆在一起用。README 一上来就讲清楚**为什么一个不生成文本的模型当聊天机器人不好用**，这个铺垫很有用。</sub> | <img src="https://img.shields.io/github/stars/tacticocc/Jevbridge?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/tacticocc/Jevbridge?style=flat&logo=github&label=" alt="updated"> |
| **[valentynkit/jev-belay](https://github.com/valentynkit/jev-belay)**<br><sub>创建于 2026-09-18 · 一个 Claude Code 的 Stop 钩子，专门拦住「没验证就说做完了」：先读本地记录，只有当改过文件却没有任何检查通过时，才花一次 Jev 调用。出问题时不阻断。</sub> | <img src="https://img.shields.io/github/stars/valentynkit/jev-belay?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/valentynkit/jev-belay?style=flat&logo=github&label=" alt="updated"> |
| **[gtaras7/typesafe-jev](https://github.com/gtaras7/typesafe-jev)**<br><sub>创建于 2026-09-17 · 一组「围绕决策模型而不是聊天提示词来写软件」的实验。每一件都自带 README、测试和实测结果，可以单独拿走。</sub> | <img src="https://img.shields.io/github/stars/gtaras7/typesafe-jev?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/gtaras7/typesafe-jev?style=flat&logo=github&label=" alt="updated"> |
| **[legacybridge-tech/pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)**<br><sub>创建于 2026-09-17 · 把判定能力拆成五个工具：模型只做窄口径的语义判断，**阈值和权重始终留在你的代码手里**。</sub> | <img src="https://img.shields.io/github/stars/legacybridge-tech/pi-typesafe-jev?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/legacybridge-tech/pi-typesafe-jev?style=flat&logo=github&label=" alt="updated"> |
| **[GiesN/typesafe-jev-workflow](https://github.com/GiesN/typesafe-jev-workflow)**<br><sub>创建于 2026-09-16 · 刻意做得又小又完整：塞一封模拟邮件进去，拿回一个带类型的 Choice，再路由到示例处理器。**清单里最小、最清楚的接线范例**。</sub> | <img src="https://img.shields.io/github/stars/GiesN/typesafe-jev-workflow?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/GiesN/typesafe-jev-workflow?style=flat&logo=github&label=" alt="updated"> |
| **[TypeSafeAI/typesafe-playground](https://github.com/TypeSafeAI/typesafe-playground)**<br><sub>创建于 2026-09-16 · 110 个用例，能直接在浏览器里改和跑。零安装——想亲手感受延迟差异，这是最快的路径。</sub> | <img src="https://img.shields.io/github/stars/TypeSafeAI/typesafe-playground?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/TypeSafeAI/typesafe-playground?style=flat&logo=github&label=" alt="updated"> |
| **[jkudish/jev-mcp](https://github.com/jkudish/jev-mcp)**<br><sub>创建于 2026-09-17 · 十个 typed MCP 工具：逐条核对论断、页面进 context 前先查有没有注入指令、无需 embedding 的重排，单次 150–500ms。值得看的是它写清了 fail-closed 规则——某条概率分布不合法只废掉那一条，其余照常返回。</sub> | <img src="https://img.shields.io/github/stars/jkudish/jev-mcp?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/jkudish/jev-mcp?style=flat&logo=github&label=" alt="updated"> |
| **[itsmostafa/typesafe-mcp](https://github.com/itsmostafa/typesafe-mcp)**<br><sub>创建于 2026-09-17 · 一个静态 Go 二进制，不需要 Node 或 Python。`evaluate setup mcp` 一条命令自动注册进 Claude Code、Claude Desktop、Codex 和 pi。单次调用可传 100 条记录批量判断，其中一条失败不影响其余。</sub> | <img src="https://img.shields.io/github/stars/itsmostafa/typesafe-mcp?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/itsmostafa/typesafe-mcp?style=flat&logo=github&label=" alt="updated"> |
| **[vinilana/jev-gateway](https://github.com/vinilana/jev-gateway)**<br><sub>创建于 2026-09-18 · 本地网关，只把"该调哪个工具"这一步交给 Jev，其余照常走原 LLM。参数全是 enum/boolean 时它直接自己拼调用，完全不请求大模型。Jev 挂了就原样透传、绝不让请求失败；作者也直说 Gemini 那条路只跑过单测、没对真 API 验过。</sub> | <img src="https://img.shields.io/github/stars/vinilana/jev-gateway?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/vinilana/jev-gateway?style=flat&logo=github&label=" alt="updated"> |
| **[peterfriese/jev-foundation-models](https://github.com/peterfriese/jev-foundation-models)**<br><sub>创建于 2026-09-21 · 用 Swift 6 把 Jev 接成 Apple Foundation Models 的 model provider：@Generable 结构里的 Bool / enum / @Guide(.range) 直接对应 noul / choice / score，40-150ms 返回，还能从 metadata 拿到概率。README 开头就警告别把 API key 打进 App 包，要走自己的后端。</sub> | <img src="https://img.shields.io/github/stars/peterfriese/jev-foundation-models?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/peterfriese/jev-foundation-models?style=flat&logo=github&label=" alt="updated"> |

<h2 id="open">🔬 开源复现与替代 <sub>10</sub></h2>

<p><em>不依赖官方 API：本地跑、开放权重、或者接口兼容 Jev。</em></p>

| 项目 | 星数 · 最近更新 |
|:--------------------------------------------------------|--------------------:|
| **[Mapika/decider](https://github.com/Mapika/decider)**<br><sub>创建于 2026-09-16 · System One 的开源复现，真给权重（基于 Qwen3.5 的 2B/4B/35B-A3B，没蒸馏 Jev）。最值钱的是「Limits, stated plainly」那节：JevBench hard 项 ECE 0.30、把规则写进问题在这个尺寸上根本不生效（一句话问题 0.67，一整段规则只有 0.24），连没修好的 regression 都列出来。</sub> | <img src="https://img.shields.io/github/stars/Mapika/decider?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/Mapika/decider?style=flat&logo=github&label=" alt="updated"> |
| **[logan-markewich/jeff](https://github.com/logan-markewich/jeff)**<br><sub>创建于 2026-09-19 · 自托管的 Jev 端点替身：把 TYPESAFE_BASE_URL 指过去，官方 SDK 原样能跑，底下是 400M 的 GLiFormer encoder 而非 LLM。README 开头就写自己哪儿输：AG News 75.5% vs 90.5%、JevBench hard 档 38% vs 74%，换来的是每百万请求约 $2.6 对 $15.6。</sub> | <img src="https://img.shields.io/github/stars/logan-markewich/jeff?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/logan-markewich/jeff?style=flat&logo=github&label=" alt="updated"> |
| **[kshetrajna12/reflex](https://github.com/kshetrajna12/reflex)**<br><sub>创建于 2026-09-17 · 少见地写了「实测证明没用」那一节：四种 LoRA 配方、27B 蒸馏、GEPA prompt 优化、措辞集成、推理级联全部量过，一个都没上线；真正起作用的是冻结模型 + 改读出方式（字母化 yes/no、Evidence/Criterion 框架、两种选项顺序取平均），hard 档 0.685、约 200ms。想先看机制的话，还有个 650MB 模型的 WebGPU 浏览器版。</sub> | <img src="https://img.shields.io/github/stars/kshetrajna12/reflex?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/kshetrajna12/reflex?style=flat&logo=github&label=" alt="updated"> |
| **[featherless-ai/simple-jev](https://github.com/featherless-ai/simple-jev)**<br><sub>创建于 2026-09-18 · 直接读 next-token logits，把任意兼容的 HF 开源模型变成 typed-decision 服务——不加分类头、不训练；还挂了个无需 key 的公开 demo API（2k 上下文、2 RPS）可以直接 curl。难得的是它明说自己的 choice/score confidence 和 noul 并不是校准过的正确率概率，别家 wrapper 往往含糊带过。</sub> | <img src="https://img.shields.io/github/stars/featherless-ai/simple-jev?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/featherless-ai/simple-jev?style=flat&logo=github&label=" alt="updated"> |
| **[jaredpalmer/kev](https://github.com/jaredpalmer/kev)**<br><sub>创建于 2026-09-17 · 0.8B/4B/9B 三个尺寸，训练代码和冻结评测集都给；报 95% 置信区间、测试集每个 checkpoint 只读一次，还直说和 Jev 的对比不是受控实验。</sub> | <img src="https://img.shields.io/github/stars/jaredpalmer/kev?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/jaredpalmer/kev?style=flat&logo=github&label=" alt="updated"> |
| **[TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev)**<br><sub>创建于 2026-09-17 · 一个 0.6B Qwen3 加决策头的 checkpoint 同时打迷宫、贪吃蛇和两个 ViZDoom 任务：ViZDoom Basic 128/128，Jev 只有 56/128；输掉的迷宫 4/10 对 7/10 也照登。</sub> | <img src="https://img.shields.io/github/stars/TianyuCodings/NanoJev?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/TianyuCodings/NanoJev?style=flat&logo=github&label=" alt="updated"> |
| **[wfzyx/von](https://github.com/wfzyx/von)**<br><sub>创建于 2026-09-18 · 395M 的 ModernBERT 编码器，本地约 18ms，ViZDoom Defend the Center 击杀 9.00 对 Jev 的 5.62；但要看它自己那张表——49 任务套件上 72.0% 对 Jev 96.6%，别看开头那个 91.23%。</sub> | <img src="https://img.shields.io/github/stars/wfzyx/von?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/wfzyx/von?style=flat&logo=github&label=" alt="updated"> |
| **[razorback16/openjev](https://github.com/razorback16/openjev)**<br><sub>创建于 2026-09-18 · 把 DiffusionGemma 的离散扩散反着用：canvas 上只 mask 答案槽，一次只读 pass，出来的分布就是答案。单问题 p50 27ms，只有熵 >0.1 时才重读四次。</sub> | <img src="https://img.shields.io/github/stars/razorback16/openjev?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/razorback16/openjev?style=flat&logo=github&label=" alt="updated"> |
| **[ekzhang/openjev-sglang](https://github.com/ekzhang/openjev-sglang)**<br><sub>创建于 2026-09-17 · Qwen3.6-35B 跑 SGLang/B200：N+1 次单 token prefill，先发一个丢弃的请求预热 radix cache，启动时验证 64 个答案标签都是单 token，并直说概率未经校准。</sub> | <img src="https://img.shields.io/github/stars/ekzhang/openjev-sglang?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/ekzhang/openjev-sglang?style=flat&logo=github&label=" alt="updated"> |
| **[nokia-applied-research/AnyJev](https://github.com/nokia-applied-research/AnyJev)**<br><sub>创建于 2026-09-21 · 不做训练：一次 prefill 读出答案，再对选项的 K 种循环移位取平均抵消位置偏置——零标注就把翻转率从 0.230 压到 0.073。还坦白当"金标"的教师模型自己跟自己只有 0.735 一致。</sub> | <img src="https://img.shields.io/github/stars/nokia-applied-research/AnyJev?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/nokia-applied-research/AnyJev?style=flat&logo=github&label=" alt="updated"> |

<h2 id="eval">📐 评测与基准 <sub>5</sub></h2>

<p><em>它到底行不行 —— 由不卖它的人量出来的数。</em></p>

| 项目 | 星数 · 最近更新 |
|:--------------------------------------------------------|--------------------:|
| **[fstandhartinger/jevbench](https://github.com/fstandhartinger/jevbench)**<br><sub>创建于 2026-09-19 · 对 48 个 Jev 类决策模型跑四轴调和平均（智能/校准/速度/成本），220 道难题在任何系统开跑前就冻结加哈希，一半封存不公开。即使不看榜也值得读两点：成本按每千次决策而非每千 token 计价并附算式；以及它点名某参赛模型仅把选项顺序反过来，分数就从 72% 掉到 21%。</sub> | <img src="https://img.shields.io/github/stars/fstandhartinger/jevbench?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/fstandhartinger/jevbench?style=flat&logo=github&label=" alt="updated"> |
| **[Zaious/jev-capability-atlas](https://github.com/Zaious/jev-capability-atlas)**<br><sub>创建于 2026-09-18 · 刻意不做排行榜，而是用真实 API 调用记录画出 Jev 哪里靠谱、哪里塌。最有说服力的是他们自曝的翻车：一道历史题的正确选项被打错一个字，Jev 就以 0.90 信心选了错答案，只改错字答案即恢复；这个错还是读者在 issue #2 抓出来后自己更正的。中文为主的双语 repo。</sub> | <img src="https://img.shields.io/github/stars/Zaious/jev-capability-atlas?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/Zaious/jev-capability-atlas?style=flat&logo=github&label=" alt="updated"> |
| **[openlayer-ai/jevals](https://github.com/openlayer-ai/jevals)**<br><sub>创建于 2026-09-20 · 把 Ragas 那套指标重写成一次批量请求的 typed questions：一条 trace 跑 8 个 eval 只要 $0.00006、0.33 秒。还带 `calibrate`，逐个阈值列出误放行 vs 多余升级的代价。难得的是 Status 里直说：适配层只对着假对象测过，没真跑过。</sub> | <img src="https://img.shields.io/github/stars/openlayer-ai/jevals?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/openlayer-ai/jevals?style=flat&logo=github&label=" alt="updated"> |
| **[danielgshea/jev-as-a-judge](https://github.com/danielgshea/jev-as-a-judge)**<br><sub>创建于 2026-09-17 · 把五次 agent 运行冻住，让每个 judge 重复打分 100 次：Jev 与人工标签全对（Claude Sonnet 4.6 只有 80%），分数方差低 92–913 倍，总花费 $0.34 对 $28.17。作者反复强调只有五个 case、一个标注人，不当成普适排名。</sub> | <img src="https://img.shields.io/github/stars/danielgshea/jev-as-a-judge?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/danielgshea/jev-as-a-judge?style=flat&logo=github&label=" alt="updated"> |
| **[sutro-sh/jev-align](https://github.com/sutro-sh/jev-align)**<br><sub>创建于 2026-09-19 · 主动学习式的 CLI：挑出 Jev 最不确定的样本让你标，再用 GEPA 改写函数定义。关键一条是训练分变高也绝不自动采纳，得你点头。发布到 ai-functions.dev 时只带标注和配置，不带你的原始数据和 key。</sub> | <img src="https://img.shields.io/github/stars/sutro-sh/jev-align?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/sutro-sh/jev-align?style=flat&logo=github&label=" alt="updated"> |

<h2 id="domain">🎯 垂直应用 <sub>12</sub></h2>

<p><em>Jev 对准某一个具体问题。</em></p>

| 项目 | 星数 · 最近更新 |
|:--------------------------------------------------------|--------------------:|
| **[Hangzhi/diffusion-jev-sglang](https://github.com/Hangzhi/diffusion-jev-sglang)**<br><sub>创建于 2026-09-21 · 用扩散模型在图像上跑 Jev 式的类型化判定：猜涂鸦、认花、选 emoji。**Jev 这套形状能不能离开文本**，这里在做实测。</sub> | <img src="https://img.shields.io/github/stars/Hangzhi/diffusion-jev-sglang?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/Hangzhi/diffusion-jev-sglang?style=flat&logo=github&label=" alt="updated"> |
| **[shitianfang/jev-use](https://github.com/shitianfang/jev-use)**<br><sub>创建于 2026-09-19 · 把智能体那些不需要产出文本的步骤交给 Jev，而且数字直接摆在开头：p50 约 230 毫秒。中文文档。</sub> | <img src="https://img.shields.io/github/stars/shitianfang/jev-use?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/shitianfang/jev-use?style=flat&logo=github&label=" alt="updated"> |
| **[cline/plugins](https://github.com/cline/plugins)**<br><sub>创建于 2026-05-31 · Cline 的官方插件索引，其中一条精选插件是**刻意不在回路里放 LLM** 的浏览器插件。它是一条值得盯着的集成面。</sub> | <img src="https://img.shields.io/github/stars/cline/plugins?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/cline/plugins?style=flat&logo=github&label=" alt="updated"> |
| **[kyotofin/tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier)**<br><sub>创建于 2026-09-18 · 把生产里的 Sonnet 分类器换掉：每页 $0.00115 vs $0.039、0.5s vs 3.3s、能认 261 种 IRS 表单而不是 30 种。评分很严——置信度低于 0.95 即使答对也算错。</sub> | <img src="https://img.shields.io/github/stars/kyotofin/tax-doc-classifier?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/kyotofin/tax-doc-classifier?style=flat&logo=github&label=" alt="updated"> |
| **[jerryjliu/docjev](https://github.com/jerryjliu/docjev)**<br><sub>创建于 2026-09-19 · 本地抽文本 + 一次 Jev 决策，做 PDF 的分类与拆分。难得的是 40 份文档的 benchmark 如实写了输的那一项：分类 40/40 打平，拆分 7/8 输给 Luna 的 8/8。</sub> | <img src="https://img.shields.io/github/stars/jerryjliu/docjev?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/jerryjliu/docjev?style=flat&logo=github&label=" alt="updated"> |
| **[realZachi/pg-jev](https://github.com/realZachi/pg-jev)**<br><sub>创建于 2026-09-17 · Postgres 扩展，`WHERE jev(tickets,'客户在生气')` 就是个普通布尔函数。最值得看的是分批实测：每请求 20 行 100% 正确，40 行掉到 92–98%，80 行只剩 77–94%。</sub> | <img src="https://img.shields.io/github/stars/realZachi/pg-jev?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/realZachi/pg-jev?style=flat&logo=github&label=" alt="updated"> |
| **[fazlerocks/jevmail](https://github.com/fazlerocks/jevmail)**<br><sub>创建于 2026-09-19 · Gmail 收件箱分拣：每封信问 Jev 三个问题（归哪个 tray、1–5 紧急度、是不是人写给你的），1000 封约一分钟、约 3 美分。只申请 gmail.readonly，动不了你的邮箱。</sub> | <img src="https://img.shields.io/github/stars/fazlerocks/jevmail?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/fazlerocks/jevmail?style=flat&logo=github&label=" alt="updated"> |
| **[rmalde/minecraft-agent](https://github.com/rmalde/minecraft-agent)**<br><sub>创建于 2026-09-20 · Astra 负责规划，Jev 从结构化游戏状态（不是截图）里选下一个动作：131 次 Jev 决策 + 35 次 planner 调用，空手开局 8 分 43 秒打掉末影龙。</sub> | <img src="https://img.shields.io/github/stars/rmalde/minecraft-agent?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/rmalde/minecraft-agent?style=flat&logo=github&label=" alt="updated"> |
| **[fhshaik/typesafe-mario](https://github.com/fhshaik/typesafe-mario)**<br><sub>创建于 2026-09-16 · 不给截图，直接把模拟器 RAM 解析成结构化 JSON（跳跃轨迹、敌人接触时间、起跳截止点、实测响应延迟），Jev 每八帧从七个手柄宏里选一个。难得的是代码只算时序事实、不写死救场动作，按键始终由 Jev 定。</sub> | <img src="https://img.shields.io/github/stars/fhshaik/typesafe-mario?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/fhshaik/typesafe-mario?style=flat&logo=github&label=" alt="updated"> |
| **[RomanSlack/jev-drone](https://github.com/RomanSlack/jev-drone)**<br><sub>创建于 2026-09-16 · MuJoCo 四旋翼，Jev 只在 ~2.5 Hz 出战术建议，50 Hz 反射层保留否决权：实测障碍顶边超出爬升上限就拒绝执行 climb。最值钱的是它的诚实——报了全程 77.5 m vs 基线 17.7 m、中位延迟 0.11 s，同时直说 Jev 那一栏只是单次跑，且更早的三种子对照里 Jev 毫无优势。</sub> | <img src="https://img.shields.io/github/stars/RomanSlack/jev-drone?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/RomanSlack/jev-drone?style=flat&logo=github&label=" alt="updated"> |
| **[bytelabs-oss/clash-jev](https://github.com/bytelabs-oss/clash-jev)**<br><sub>创建于 2026-09-21 · 通过 adb 在真机上打皇室战争，完全没有训练策略：OpenCV 加手标的兵种分类器每秒生成一份 JSON state，Jev 串行回答策略/出牌/落点三问，各约 135 ms，一局约 $0.004。最值得看的是设计取舍表：作者故意不过滤买不起的牌、不喂克制关系——因为一旦 state 里列了克制表，正确出牌率就从五五开跳到 98%，那测的是作者不是模型。</sub> | <img src="https://img.shields.io/github/stars/bytelabs-oss/clash-jev?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/bytelabs-oss/clash-jev?style=flat&logo=github&label=" alt="updated"> |
| **[trungdq88/youtube-sponsor-detection](https://github.com/trungdq88/youtube-sponsor-detection)**<br><sub>创建于 2026-09-17 · 跳 YouTube 恰饭段，但 Jev 从不碰时间戳：字幕渲染成 `L042\|` 行号，Jev 按 80 行窗口挑行 ID，再由代码换算回秒。三种模式都标了每小时观看成本（纯字幕不到一分钱，纯听音 $0.46），策略上宁可多看一秒也不误切正片，并附带以 SponsorBlock 标注为准的 recall/precision/边界误差评测脚本。</sub> | <img src="https://img.shields.io/github/stars/trungdq88/youtube-sponsor-detection?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/trungdq88/youtube-sponsor-detection?style=flat&logo=github&label=" alt="updated"> |

<h2 id="hot">📈 热门项目（按星数自动排序）</h2>

<em>由 `scripts/gen_readme.py` 从 `data/stars.json` 生成。⛔ 不手写。星数即便脚本没跑也不会过期——徽章是实时的。</em>

| # | 项目 | 星数 | 创建 |
|--:|:--------------------------|--------------------:|------------------:|
| 1 | **[browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast)** | <img src="https://img.shields.io/github/stars/browser-use/jev-ultrafast?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/browser-use/jev-ultrafast?style=flat&logo=github&label=" alt="created"> |
| 2 | **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | <img src="https://img.shields.io/github/stars/tamaratran/fast-jev-compaction?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/tamaratran/fast-jev-compaction?style=flat&logo=github&label=" alt="created"> |
| 3 | **[jaredpalmer/kev](https://github.com/jaredpalmer/kev)** | <img src="https://img.shields.io/github/stars/jaredpalmer/kev?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/jaredpalmer/kev?style=flat&logo=github&label=" alt="created"> |
| 4 | **[jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** | <img src="https://img.shields.io/github/stars/jev-chat/jev-chat-jarvis?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/jev-chat/jev-chat-jarvis?style=flat&logo=github&label=" alt="created"> |
| 5 | **[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)** | <img src="https://img.shields.io/github/stars/jarrodwatts/jev-trader?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/jarrodwatts/jev-trader?style=flat&logo=github&label=" alt="created"> |
| 6 | **[TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev)** | <img src="https://img.shields.io/github/stars/TianyuCodings/NanoJev?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/TianyuCodings/NanoJev?style=flat&logo=github&label=" alt="created"> |
| 7 | **[kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** | <img src="https://img.shields.io/github/stars/kerpopule/hermes-jev-skills?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/kerpopule/hermes-jev-skills?style=flat&logo=github&label=" alt="created"> |
| 8 | **[Sac-Y/Jev-cu](https://github.com/Sac-Y/Jev-cu)** | <img src="https://img.shields.io/github/stars/Sac-Y/Jev-cu?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/Sac-Y/Jev-cu?style=flat&logo=github&label=" alt="created"> |
| 9 | **[devagrawal09/jev-review](https://github.com/devagrawal09/jev-review)** | <img src="https://img.shields.io/github/stars/devagrawal09/jev-review?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/devagrawal09/jev-review?style=flat&logo=github&label=" alt="created"> |
| 10 | **[wfzyx/von](https://github.com/wfzyx/von)** | <img src="https://img.shields.io/github/stars/wfzyx/von?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/wfzyx/von?style=flat&logo=github&label=" alt="created"> |

---

<h2 id="choose">🧭 怎么选</h2>

**想搞懂 Jev** → `browser-use/jev-ultrafast`。生态里最大的一次成本削减，看它怎么写那一次判定。

**想明天就能用上** → Claude Code 上用 `tamaratran/fast-jev-compaction`，浏览器自动化用 `browser-use/jev-ultrafast`。

**想自己做一个** → 从 `kerpopule/hermes-jev-skills` 起步，回路已经接好了。

---

### 关于

这是一个**独立的、非官方**的 Jev 项目精选清单，收录 **84 个项目、12 个类别**。
与 TypeSafe AI 没有隶属关系，也没有得到它的背书。

搜 "Jev" 会出来上万个仓库，大部分点进去是空的、改名的、或者只是把官方文档抄了一遍。
**这个清单回答的不是「Jev 是什么」**——那是[官方文档](https://docs.typesafe.ai)的活，
而且它会变。这里回答的是另一个问题：**这么多项目里，我该看哪个、为什么是它。**