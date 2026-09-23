<p align="center">
  <img src="assets/banner.svg" alt="awesome-jev-essentials" width="100%">
</p>

# awesome-jev-essentials

**真正值得你花时间的 Jev 项目** —— 挑过、比过、持续更新。

**English** · [中文](README.zh-CN.md)

## 目录

<a href="#route">🚦 Route & classify</a> · <a href="#guard">🛡 Guard & verify</a> · <a href="#compact">🗜 Compaction & context</a> · <a href="#skills">🧩 Skills & agents</a> · <a href="#score">⚖️ Score & rank</a> · <a href="#apps">🖥 Apps & interfaces</a> · <a href="#infra">🔌 Infra, SDKs & bridges</a> · <a href="#domain">🎯 Domain apps</a> · <a href="#hot">📈 热门</a> · <a href="#choose">🧭 怎么选</a>

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

<h2 id="guard">🛡 守门与验证 <sub>6</sub></h2>

<p><em>在坏动作（和坏结论）落地前拦住它。</em></p>

| 项目 | 星数 · 最近更新 |
|:--------------------------------------------------------|--------------------:|
| **[leepokai/jev-guard](https://github.com/leepokai/jev-guard)**<br><sub>创建于 2026-09-17 · 每次工具调用执行前先打分。小而专一——护栏就该是这个体量。</sub> | <img src="https://img.shields.io/github/stars/leepokai/jev-guard?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/leepokai/jev-guard?style=flat&logo=github&label=" alt="updated"> |
| **[y0usaf/pi-jev](https://github.com/y0usaf/pi-jev)**<br><sub>创建于 2026-09-16 · 一个真被人测过的工具调用闸门，是这一类里被引用最多的起点。</sub> | <img src="https://img.shields.io/github/stars/y0usaf/pi-jev?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/y0usaf/pi-jev?style=flat&logo=github&label=" alt="updated"> |
| **[qkal/Canny](https://github.com/qkal/Canny)**<br><sub>创建于 2026-09-11 · 拦住智能体拿不出证据就说「做完了」。它防的是坏**结论**而不是坏动作——这是大多数护栏都没管的失败模式。</sub> | <img src="https://img.shields.io/github/stars/qkal/Canny?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/qkal/Canny?style=flat&logo=github&label=" alt="updated"> |
| **[jesset/pi-verdict](https://github.com/jesset/pi-verdict)**<br><sub>创建于 2026-08-25 · 约 1 千行的权限闸门，模仿 Claude Code 的 auto 模式。内置危险规则 + 你自己的允许/拒绝清单，先零延迟地解决掉明显的情况；只有真正含糊的才花一次模型调用。</sub> | <img src="https://img.shields.io/github/stars/jesset/pi-verdict?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/jesset/pi-verdict?style=flat&logo=github&label=" alt="updated"> |
| **[raihankhan-rk/diffjury](https://github.com/raihankhan-rk/diffjury)**<br><sub>创建于 2026-09-17 · 贴一个 PR 链接，由 Jev 判断这次改动有没有风险。它做成了能直接用的页面而不是一个库——这一类里最容易上手试的一个。</sub> | <img src="https://img.shields.io/github/stars/raihankhan-rk/diffjury?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/raihankhan-rk/diffjury?style=flat&logo=github&label=" alt="updated"> |
| **[DanRWilloughby/snifftest](https://github.com/DanRWilloughby/snifftest)**<br><sub>创建于 2026-09-17 · 查「AI 味」的文稿检查器：零依赖、规则可数，只在规则判断不了的地方加一次模型判定。**确定性检查 + 模型判断**怎么配合，这里是个干净的例子。</sub> | <img src="https://img.shields.io/github/stars/DanRWilloughby/snifftest?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/DanRWilloughby/snifftest?style=flat&logo=github&label=" alt="updated"> |

<h2 id="compact">🗜 压缩与上下文 <sub>4</sub></h2>

<p><em>窗口满了，决定丢掉什么。</em></p>

| 项目 | 星数 · 最近更新 |
|:--------------------------------------------------------|--------------------:|
| **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)**<br><sub>创建于 2026-09-17 · 一个 Claude Code 插件，压缩前先给每次工具调用打分。它蹭的是现成的用户群，而不是自己攒一个。</sub> | <img src="https://img.shields.io/github/stars/tamaratran/fast-jev-compaction?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/tamaratran/fast-jev-compaction?style=flat&logo=github&label=" alt="updated"> |
| **[tamaratran/jev-pruner](https://github.com/tamaratran/jev-pruner)**<br><sub>创建于 2026-09-18 · 命令跑完、结果还没送到模型之前，先把冗长的 Bash 输出削掉。省下来的**是真的上下文，不是摘要出来的近似物**。</sub> | <img src="https://img.shields.io/github/stars/tamaratran/jev-pruner?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/tamaratran/jev-pruner?style=flat&logo=github&label=" alt="updated"> |
| **[joelhooks/pi-fast-jev-compaction](https://github.com/joelhooks/pi-fast-jev-compaction)**<br><sub>创建于 2026-09-18 · 对话正文原样保留，只清理过期的工具调用记录。而且说得很直白：**只做第一层**——不摘要、不改写、不编造记忆。</sub> | <img src="https://img.shields.io/github/stars/joelhooks/pi-fast-jev-compaction?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/joelhooks/pi-fast-jev-compaction?style=flat&logo=github&label=" alt="updated"> |
| **[leonaaardob/fast-dev-compaction](https://github.com/leonaaardob/fast-dev-compaction)**<br><sub>创建于 2026-09-18 · 把 Claude Code 那个压缩插件移植到 Codex 的生命周期钩子上：给每次工具调用打分、压缩、再把 Jev 判定要留的原样历史重新注入。</sub> | <img src="https://img.shields.io/github/stars/leonaaardob/fast-dev-compaction?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/leonaaardob/fast-dev-compaction?style=flat&logo=github&label=" alt="updated"> |

<h2 id="skills">🧩 技能与智能体 <sub>4</sub></h2>

<p><em>插进智能体回路里的零件，不是成品应用。</em></p>

| 项目 | 星数 · 最近更新 |
|:--------------------------------------------------------|--------------------:|
| **[safzanpirani/pi-jev-skill-picker](https://github.com/safzanpirani/pi-jev-skill-picker)**<br><sub>创建于 2026-09-20 · 把系统提示里整份技能目录换成一个排序工具。装了再多技能，也不再是每一轮都要为那份目录付 token。</sub> | <img src="https://img.shields.io/github/stars/safzanpirani/pi-jev-skill-picker?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/safzanpirani/pi-jev-skill-picker?style=flat&logo=github&label=" alt="updated"> |
| **[yuyang2230/jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)**<br><sub>创建于 2026-09-19 · 把高频小判断（分类/初筛/打分/核查）卸到 Jev 的免费档上，主模型只负责生成。中文文档，而且把成本账算给你看。</sub> | <img src="https://img.shields.io/github/stars/yuyang2230/jev-agent-skill?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/yuyang2230/jev-agent-skill?style=flat&logo=github&label=" alt="updated"> |
| **[HyunjunJeon/pi-quiet-ask](https://github.com/HyunjunJeon/pi-quiet-ask)**<br><sub>创建于 2026-09-17 · 把 Jev 当成安静的决策层：主模型继续写代码，由 Jev 回答框架必须问的那些封闭式问题，约 250 毫秒一次。</sub> | <img src="https://img.shields.io/github/stars/HyunjunJeon/pi-quiet-ask?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/HyunjunJeon/pi-quiet-ask?style=flat&logo=github&label=" alt="updated"> |
| **[kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)**<br><sub>创建于 2026-09-18 · 路由、记忆、压缩、技能选择全都有。是把 Jev 放进智能体回路里（而不是挂在旁边）最完整的一个例子。</sub> | <img src="https://img.shields.io/github/stars/kerpopule/hermes-jev-skills?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/kerpopule/hermes-jev-skills?style=flat&logo=github&label=" alt="updated"> |

<h2 id="score">⚖️ 打分与排序 <sub>3</sub></h2>

<p><em>把判断变成一个能排序的数字。</em></p>

| 项目 | 星数 · 最近更新 |
|:--------------------------------------------------------|--------------------:|
| **[ruban-24/switchboard](https://github.com/ruban-24/switchboard)**<br><sub>创建于 2026-09-20 · 由你自己的策略驱动的模型选择：Jev 只做任务评估，**如何解读这个评估由你的规则决定**。把判断和策略分开，这个形状是对的。</sub> | <img src="https://img.shields.io/github/stars/ruban-24/switchboard?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/ruban-24/switchboard?style=flat&logo=github&label=" alt="updated"> |
| **[compozy/yoshi](https://github.com/compozy/yoshi)**<br><sub>创建于 2026-09-18 · 上下文裁剪代理：超过大小闸门才判定一次，然后按验证过的结论做删减，同时保持协议完整。README 里的说法是**量出来的，不是断言的**。</sub> | <img src="https://img.shields.io/github/stars/compozy/yoshi?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/compozy/yoshi?style=flat&logo=github&label=" alt="updated"> |
| **[shiftynick/jev-axi](https://github.com/shiftynick/jev-axi)**<br><sub>创建于 2026-09-16 · 给智能体用的 Jev 命令行：选、评、查、排、分流、守门——类型化判定实际就那么几种形状，它把这几种做成了 shell 命令。</sub> | <img src="https://img.shields.io/github/stars/shiftynick/jev-axi?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/shiftynick/jev-axi?style=flat&logo=github&label=" alt="updated"> |

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

<h2 id="infra">🔌 基础设施、SDK 与桥接 <sub>7</sub></h2>

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

<h2 id="domain">🎯 垂直应用 <sub>3</sub></h2>

<p><em>Jev 对准某一个具体问题。</em></p>

| 项目 | 星数 · 最近更新 |
|:--------------------------------------------------------|--------------------:|
| **[Hangzhi/diffusion-jev-sglang](https://github.com/Hangzhi/diffusion-jev-sglang)**<br><sub>创建于 2026-09-21 · 用扩散模型在图像上跑 Jev 式的类型化判定：猜涂鸦、认花、选 emoji。**Jev 这套形状能不能离开文本**，这里在做实测。</sub> | <img src="https://img.shields.io/github/stars/Hangzhi/diffusion-jev-sglang?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/Hangzhi/diffusion-jev-sglang?style=flat&logo=github&label=" alt="updated"> |
| **[shitianfang/jev-use](https://github.com/shitianfang/jev-use)**<br><sub>创建于 2026-09-19 · 把智能体那些不需要产出文本的步骤交给 Jev，而且数字直接摆在开头：p50 约 230 毫秒。中文文档。</sub> | <img src="https://img.shields.io/github/stars/shitianfang/jev-use?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/shitianfang/jev-use?style=flat&logo=github&label=" alt="updated"> |
| **[cline/plugins](https://github.com/cline/plugins)**<br><sub>创建于 2026-05-31 · Cline 的官方插件索引，其中一条精选插件是**刻意不在回路里放 LLM** 的浏览器插件。它是一条值得盯着的集成面。</sub> | <img src="https://img.shields.io/github/stars/cline/plugins?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/cline/plugins?style=flat&logo=github&label=" alt="updated"> |

<h2 id="hot">📈 热门项目（按星数自动排序）</h2>

<em>由 `scripts/gen_readme.py` 从 `data/stars.json` 生成。⛔ 不手写。星数即便脚本没跑也不会过期——徽章是实时的。</em>

| # | 项目 | 星数 | 创建 |
|--:|:--------------------------|--------------------:|------------------:|
| 1 | **[browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast)** | <img src="https://img.shields.io/github/stars/browser-use/jev-ultrafast?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/browser-use/jev-ultrafast?style=flat&logo=github&label=" alt="created"> |
| 2 | **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)** | <img src="https://img.shields.io/github/stars/tamaratran/fast-jev-compaction?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/tamaratran/fast-jev-compaction?style=flat&logo=github&label=" alt="created"> |
| 3 | **[jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)** | <img src="https://img.shields.io/github/stars/jev-chat/jev-chat-jarvis?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/jev-chat/jev-chat-jarvis?style=flat&logo=github&label=" alt="created"> |
| 4 | **[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)** | <img src="https://img.shields.io/github/stars/jarrodwatts/jev-trader?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/jarrodwatts/jev-trader?style=flat&logo=github&label=" alt="created"> |
| 5 | **[kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)** | <img src="https://img.shields.io/github/stars/kerpopule/hermes-jev-skills?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/kerpopule/hermes-jev-skills?style=flat&logo=github&label=" alt="created"> |
| 6 | **[Sac-Y/Jev-cu](https://github.com/Sac-Y/Jev-cu)** | <img src="https://img.shields.io/github/stars/Sac-Y/Jev-cu?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/Sac-Y/Jev-cu?style=flat&logo=github&label=" alt="created"> |
| 7 | **[thruwire/foreman](https://github.com/thruwire/foreman)** | <img src="https://img.shields.io/github/stars/thruwire/foreman?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/thruwire/foreman?style=flat&logo=github&label=" alt="created"> |
| 8 | **[gargpratyush/jev-router](https://github.com/gargpratyush/jev-router)** | <img src="https://img.shields.io/github/stars/gargpratyush/jev-router?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/gargpratyush/jev-router?style=flat&logo=github&label=" alt="created"> |
| 9 | **[y0usaf/pi-jev](https://github.com/y0usaf/pi-jev)** | <img src="https://img.shields.io/github/stars/y0usaf/pi-jev?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/y0usaf/pi-jev?style=flat&logo=github&label=" alt="created"> |
| 10 | **[tamaratran/jev-pruner](https://github.com/tamaratran/jev-pruner)** | <img src="https://img.shields.io/github/stars/tamaratran/jev-pruner?style=flat&logo=github&label=" alt="stars"> | <img src="https://img.shields.io/github/created-at/tamaratran/jev-pruner?style=flat&logo=github&label=" alt="created"> |

---

<h2 id="choose">🧭 怎么选</h2>

**想搞懂 Jev** → `browser-use/jev-ultrafast`。生态里最大的一次成本削减，看它怎么写那一次判定。

**想明天就能用上** → Claude Code 上用 `tamaratran/fast-jev-compaction`，浏览器自动化用 `browser-use/jev-ultrafast`。

**想自己做一个** → 从 `kerpopule/hermes-jev-skills` 起步，回路已经接好了。

---

### 关于

这是一个**独立的、非官方**的 Jev 项目精选清单。与 TypeSafe AI 没有隶属关系，
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

**收录 43 个，覆盖 8 类**；其中 43 个已经写了选它的理由，
剩下的在补 —— ⭐ **补理由这件事本身就是这个清单的内容**，不是收尾工作。

**关于 Jev**：它是 TypeSafe AI 出的 System One 模型 —— 不生成文本，
只在一组带类型的选项里做一次判定，几十到几百毫秒返回。
所有厂商自评的性能数字这里都标注了出处。

MIT 许可。收录标准见 [CONTRIBUTING.md](CONTRIBUTING.md)。
