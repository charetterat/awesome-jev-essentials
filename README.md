<p align="center">
  <img src="assets/banner.svg" alt="awesome-jev-essentials" width="100%">
</p>

# awesome-jev-essentials

**The Jev projects actually worth your time** — picked, compared, kept current.

**English** · [中文](README.zh-CN.md)

## Contents

<a href="#route">🚦 Route & classify</a> · <a href="#guard">🛡 Guard & verify</a> · <a href="#compact">🗜 Compaction & context</a> · <a href="#skills">🧩 Skills & agents</a> · <a href="#score">⚖️ Score & rank</a> · <a href="#apps">🖥 Apps & interfaces</a> · <a href="#infra">🔌 Infra, SDKs & bridges</a> · <a href="#domain">🎯 Domain apps</a> · <a href="#hot">📈 Most starred</a> · <a href="#choose">🧭 How to choose</a>

---

<h2 id="route">🚦 Route & classify <sub>8</sub></h2>

<p><em>Deciding what a request is, before deciding what to do with it.</em></p>

| Project | Stars · Updated |
|:--------------------------------------------------------|--------------------:|
| **[gargpratyush/jev-router](https://github.com/gargpratyush/jev-router)**<br><sub>created 2026-09-16 · Routes per turn in Claude Code and Codex — simple work to the fast tier, hard work to the strong one — without changing either CLI's interface, tools, sessions or auth. The drop-in kind of router.</sub> | <img src="https://img.shields.io/github/stars/gargpratyush/jev-router?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/gargpratyush/jev-router?style=flat&logo=github&label=" alt="updated"> |
| **[prismhq/jev-router](https://github.com/prismhq/jev-router)**<br><sub>created 2026-09-17 · A server-side router: clients send one model id and Jev picks which model serves the request. Transport is LiteLLM, so it slots into an existing gateway rather than replacing it.</sub> | <img src="https://img.shields.io/github/stars/prismhq/jev-router?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/prismhq/jev-router?style=flat&logo=github&label=" alt="updated"> |
| **[miniLV/Jev-Auto-Router](https://github.com/miniLV/Jev-Auto-Router)**<br><sub>created 2026-08-01 · Chinese-language, and honest about it: the README says the architecture is settled but the runtime is still a prototype, and tells you not to treat the design as production install instructions. Rare candour.</sub> | <img src="https://img.shields.io/github/stars/miniLV/Jev-Auto-Router?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/miniLV/Jev-Auto-Router?style=flat&logo=github&label=" alt="updated"> |
| **[shimo4228/jev-skill-router](https://github.com/shimo4228/jev-skill-router)**<br><sub>created 2026-09-21 · The authors built it, ran it, and then published the conclusion that as a router it probably won't help a strong model. It ships shadow-first so you can watch its calls before trusting them.</sub> | <img src="https://img.shields.io/github/stars/shimo4228/jev-skill-router?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/shimo4228/jev-skill-router?style=flat&logo=github&label=" alt="updated"> |
| **[GodsBoy/jev-agent-skill-router](https://github.com/GodsBoy/jev-agent-skill-router)**<br><sub>created 2026-09-16 · Carries a measured number — 68 of 72 synthetic requests routed correctly against a 70.8% lexical baseline — and labels the result exploratory and reused-data. States its limits next to its win.</sub> | <img src="https://img.shields.io/github/stars/GodsBoy/jev-agent-skill-router?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/GodsBoy/jev-agent-skill-router?style=flat&logo=github&label=" alt="updated"> |
| **[jekozyra/pi-typesafe-router](https://github.com/jekozyra/pi-typesafe-router)**<br><sub>created 2026-09-18 · One sentence, one job: classify the request, route it to the right model. The README's second line warns you not to run it alongside another automatic router.</sub> | <img src="https://img.shields.io/github/stars/jekozyra/pi-typesafe-router?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/jekozyra/pi-typesafe-router?style=flat&logo=github&label=" alt="updated"> |
| **[adarshmishra07/jcm-router](https://github.com/adarshmishra07/jcm-router)**<br><sub>created 2026-09-17 · A local proxy that picks model and effort per message, routes subagents, and deliberately leaves your cached main chat alone. Your subscription login keeps working.</sub> | <img src="https://img.shields.io/github/stars/adarshmishra07/jcm-router?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/adarshmishra07/jcm-router?style=flat&logo=github&label=" alt="updated"> |
| **[mejiasd3v/pi-jev-router](https://github.com/mejiasd3v/pi-jev-router)**<br><sub>created 2026-09-17 · Smallest useful version: Jev picks the model once per session and the choice stays fixed. No per-turn churn — which is the right default if you dislike a model changing under you.</sub> | <img src="https://img.shields.io/github/stars/mejiasd3v/pi-jev-router?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/mejiasd3v/pi-jev-router?style=flat&logo=github&label=" alt="updated"> |

<h2 id="guard">🛡 Guard & verify <sub>6</sub></h2>

<p><em>Catching bad actions — and bad claims — before they land.</em></p>

| Project | Stars · Updated |
|:--------------------------------------------------------|--------------------:|
| **[leepokai/jev-guard](https://github.com/leepokai/jev-guard)**<br><sub>created 2026-09-17 · Scores every tool call before it runs. Small and single-purpose — the right size for a guardrail.</sub> | <img src="https://img.shields.io/github/stars/leepokai/jev-guard?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/leepokai/jev-guard?style=flat&logo=github&label=" alt="updated"> |
| **[y0usaf/pi-jev](https://github.com/y0usaf/pi-jev)**<br><sub>created 2026-09-16 · A tool-call gate that people have actually tested. The most cited starting point in this category.</sub> | <img src="https://img.shields.io/github/stars/y0usaf/pi-jev?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/y0usaf/pi-jev?style=flat&logo=github&label=" alt="updated"> |
| **[qkal/Canny](https://github.com/qkal/Canny)**<br><sub>created 2026-09-11 · Stops an agent claiming it's done without evidence. Guards against bad **claims**, not bad actions — a failure mode most guardrails ignore.</sub> | <img src="https://img.shields.io/github/stars/qkal/Canny?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/qkal/Canny?style=flat&logo=github&label=" alt="updated"> |
| **[jesset/pi-verdict](https://github.com/jesset/pi-verdict)**<br><sub>created 2026-08-25 · A ~1k-line permission gate in the style of Claude Code's auto mode. Built-in danger rules and your own allow/deny lists settle the obvious cases at zero latency; only the ambiguous ones cost a model call.</sub> | <img src="https://img.shields.io/github/stars/jesset/pi-verdict?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/jesset/pi-verdict?style=flat&logo=github&label=" alt="updated"> |
| **[raihankhan-rk/diffjury](https://github.com/raihankhan-rk/diffjury)**<br><sub>created 2026-09-17 · Paste a PR URL and Jev decides whether it is risky. Shipped as a usable page rather than a library, which makes it the easiest one here to actually try.</sub> | <img src="https://img.shields.io/github/stars/raihankhan-rk/diffjury?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/raihankhan-rk/diffjury?style=flat&logo=github&label=" alt="updated"> |
| **[DanRWilloughby/snifftest](https://github.com/DanRWilloughby/snifftest)**<br><sub>created 2026-09-17 · Prose linter for AI writing tells: zero dependencies, countable rules, plus one judgment model for the calls a rule cannot make. A clean example of mixing deterministic checks with a model.</sub> | <img src="https://img.shields.io/github/stars/DanRWilloughby/snifftest?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/DanRWilloughby/snifftest?style=flat&logo=github&label=" alt="updated"> |

<h2 id="compact">🗜 Compaction & context <sub>4</sub></h2>

<p><em>Deciding what to throw away when the window fills up.</em></p>

| Project | Stars · Updated |
|:--------------------------------------------------------|--------------------:|
| **[tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction)**<br><sub>created 2026-09-17 · A Claude Code plugin that scores every tool call before compaction. Rides an existing user base instead of building one.</sub> | <img src="https://img.shields.io/github/stars/tamaratran/fast-jev-compaction?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/tamaratran/fast-jev-compaction?style=flat&logo=github&label=" alt="updated"> |
| **[tamaratran/jev-pruner](https://github.com/tamaratran/jev-pruner)**<br><sub>created 2026-09-18 · Trims noisy Bash output after the command runs but before the result reaches the model — so the saving is real context, not a summarised approximation of it.</sub> | <img src="https://img.shields.io/github/stars/tamaratran/jev-pruner?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/tamaratran/jev-pruner?style=flat&logo=github&label=" alt="updated"> |
| **[joelhooks/pi-fast-jev-compaction](https://github.com/joelhooks/pi-fast-jev-compaction)**<br><sub>created 2026-09-18 · Keeps conversation text verbatim while pruning stale tool history, and says so plainly: layer 1 only — it does not summarise, rewrite, or invent memory.</sub> | <img src="https://img.shields.io/github/stars/joelhooks/pi-fast-jev-compaction?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/joelhooks/pi-fast-jev-compaction?style=flat&logo=github&label=" alt="updated"> |
| **[leonaaardob/fast-dev-compaction](https://github.com/leonaaardob/fast-dev-compaction)**<br><sub>created 2026-09-18 · Port of the Claude Code compaction plugin to Codex lifecycle hooks: score every tool call, compact, then re-inject the verbatim history Jev chose to keep.</sub> | <img src="https://img.shields.io/github/stars/leonaaardob/fast-dev-compaction?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/leonaaardob/fast-dev-compaction?style=flat&logo=github&label=" alt="updated"> |

<h2 id="skills">🧩 Skills & agents <sub>4</sub></h2>

<p><em>Pieces you plug into an agent loop, not finished apps.</em></p>

| Project | Stars · Updated |
|:--------------------------------------------------------|--------------------:|
| **[safzanpirani/pi-jev-skill-picker](https://github.com/safzanpirani/pi-jev-skill-picker)**<br><sub>created 2026-09-20 · Replaces the whole skills catalog in the system prompt with one ranking tool — so installing more skills stops costing you tokens on every turn.</sub> | <img src="https://img.shields.io/github/stars/safzanpirani/pi-jev-skill-picker?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/safzanpirani/pi-jev-skill-picker?style=flat&logo=github&label=" alt="updated"> |
| **[yuyang2230/jev-agent-skill](https://github.com/yuyang2230/jev-agent-skill)**<br><sub>created 2026-09-19 · Offloads the small frequent judgments — classify, screen, score, check — onto Jev's free tier so the main model only does generation. Chinese docs, and it shows the cost arithmetic.</sub> | <img src="https://img.shields.io/github/stars/yuyang2230/jev-agent-skill?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/yuyang2230/jev-agent-skill?style=flat&logo=github&label=" alt="updated"> |
| **[HyunjunJeon/pi-quiet-ask](https://github.com/HyunjunJeon/pi-quiet-ask)**<br><sub>created 2026-09-17 · Jev as the quiet decision layer: the main model keeps writing code, Jev answers the closed questions the harness has to ask, in about 250 ms.</sub> | <img src="https://img.shields.io/github/stars/HyunjunJeon/pi-quiet-ask?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/HyunjunJeon/pi-quiet-ask?style=flat&logo=github&label=" alt="updated"> |
| **[kerpopule/hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills)**<br><sub>created 2026-09-18 · Routing, memory, compaction and skill selection. The most complete example of Jev inside an agent loop rather than bolted on the side.</sub> | <img src="https://img.shields.io/github/stars/kerpopule/hermes-jev-skills?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/kerpopule/hermes-jev-skills?style=flat&logo=github&label=" alt="updated"> |

<h2 id="score">⚖️ Score & rank <sub>3</sub></h2>

<p><em>Turning a judgement into a number you can sort by.</em></p>

| Project | Stars · Updated |
|:--------------------------------------------------------|--------------------:|
| **[ruban-24/switchboard](https://github.com/ruban-24/switchboard)**<br><sub>created 2026-09-20 · Model-agnostic routing driven by your own policy: Jev assesses the task, your rules decide what that assessment means. Separating judgement from policy is the right shape.</sub> | <img src="https://img.shields.io/github/stars/ruban-24/switchboard?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/ruban-24/switchboard?style=flat&logo=github&label=" alt="updated"> |
| **[compozy/yoshi](https://github.com/compozy/yoshi)**<br><sub>created 2026-09-18 · Context-pruning proxy that judges once above a size gate and then applies the validated omissions while keeping the protocol intact. The README claims are measured, not asserted.</sub> | <img src="https://img.shields.io/github/stars/compozy/yoshi?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/compozy/yoshi?style=flat&logo=github&label=" alt="updated"> |
| **[shiftynick/jev-axi](https://github.com/shiftynick/jev-axi)**<br><sub>created 2026-09-16 · An agent-ergonomic CLI over Jev: pick, rate, check, rank, triage, guard — the six shapes a typed decision actually takes, exposed as shell commands.</sub> | <img src="https://img.shields.io/github/stars/shiftynick/jev-axi?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/shiftynick/jev-axi?style=flat&logo=github&label=" alt="updated"> |

<h2 id="apps">🖥 Apps & interfaces <sub>8</sub></h2>

<p><em>Finished things you can open and use.</em></p>

| Project | Stars · Updated |
|:--------------------------------------------------------|--------------------:|
| **[browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast)**<br><sub>created 2026-09-16 · A web agent that replaces the per-step LLM call with a typed decision. **Biggest cost cut in the ecosystem** — every step that used to be a full model call is now one Jev call.</sub> | <img src="https://img.shields.io/github/stars/browser-use/jev-ultrafast?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/browser-use/jev-ultrafast?style=flat&logo=github&label=" alt="updated"> |
| **[jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)**<br><sub>created 2026-09-21 · A phone-side copilot for WeChat / QQ / X / Feishu. Low enough latency to keep up with a live conversation — that is the whole point of System One here.</sub> | <img src="https://img.shields.io/github/stars/jev-chat/jev-chat-jarvis?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/jev-chat/jev-chat-jarvis?style=flat&logo=github&label=" alt="updated"> |
| **[jarrodwatts/jev-trader](https://github.com/jarrodwatts/jev-trader)**<br><sub>created 2026-09-16 · One decision per Monad block. Fast enough to sit inside a block, cheap enough to run every time.</sub> | <img src="https://img.shields.io/github/stars/jarrodwatts/jev-trader?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/jarrodwatts/jev-trader?style=flat&logo=github&label=" alt="updated"> |
| **[Sac-Y/Jev-cu](https://github.com/Sac-Y/Jev-cu)**<br><sub>created 2026-09-18 · Computer use. The closest thing here to a general desktop agent.</sub> | <img src="https://img.shields.io/github/stars/Sac-Y/Jev-cu?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/Sac-Y/Jev-cu?style=flat&logo=github&label=" alt="updated"> |
| **[yikangy873-gif/jev-desktop](https://github.com/yikangy873-gif/jev-desktop)**<br><sub>created 2026-09-19 · Codex handles the goal, prepares the text and verifies the result; Jev picks the action and its target in one request. A clean split between planning and deciding.</sub> | <img src="https://img.shields.io/github/stars/yikangy873-gif/jev-desktop?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/yikangy873-gif/jev-desktop?style=flat&logo=github&label=" alt="updated"> |
| **[AboveColin/HA-Jev](https://github.com/AboveColin/HA-Jev)**<br><sub>created 2026-09-17 · Turns Jev's answers into Home Assistant sensors, so an automation can read a probability like any other number. A nice reminder that a decision model needs no chat UI.</sub> | <img src="https://img.shields.io/github/stars/AboveColin/HA-Jev?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/AboveColin/HA-Jev?style=flat&logo=github&label=" alt="updated"> |
| **[thruwire/foreman](https://github.com/thruwire/foreman)**<br><sub>created 2026-09-17 · Puts a fast decision model above slower coding agents: feed it a ticket or a bug report and it decides who does what next.</sub> | <img src="https://img.shields.io/github/stars/thruwire/foreman?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/thruwire/foreman?style=flat&logo=github&label=" alt="updated"> |
| **[Silbercue/public-browser](https://github.com/Silbercue/public-browser)**<br><sub>created 2026-04-07 · Lets Claude Code and Cursor drive your real logged-in Chrome, and reports the delta it measured: fewer tokens, fewer tool calls, fewer tool definitions.</sub> | <img src="https://img.shields.io/github/stars/Silbercue/public-browser?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/Silbercue/public-browser?style=flat&logo=github&label=" alt="updated"> |

<h2 id="infra">🔌 Infra, SDKs & bridges <sub>7</sub></h2>

<p><em>Getting Jev into the stack you already have.</em></p>

| Project | Stars · Updated |
|:--------------------------------------------------------|--------------------:|
| **[burnigtm/jev-mcp](https://github.com/burnigtm/jev-mcp)**<br><sub>created 2026-09-17 · A local stdio MCP server exposing Jev as typed judgments, including a step router that selects a prepared call in the same request.</sub> | <img src="https://img.shields.io/github/stars/burnigtm/jev-mcp?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/burnigtm/jev-mcp?style=flat&logo=github&label=" alt="updated"> |
| **[tacticocc/Jevbridge](https://github.com/tacticocc/Jevbridge)**<br><sub>created 2026-09-18 · ACP and MCP adapter putting Jev next to Codex, Claude, Grok and OpenCode. The README opens by explaining why a text-free model makes a poor chatbot — useful framing.</sub> | <img src="https://img.shields.io/github/stars/tacticocc/Jevbridge?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/tacticocc/Jevbridge?style=flat&logo=github&label=" alt="updated"> |
| **[valentynkit/jev-belay](https://github.com/valentynkit/jev-belay)**<br><sub>created 2026-09-18 · A Claude Code Stop hook that blocks an unverified "done": it reads the transcript, and only when files changed with no check passed does it spend one Jev call. Fails open.</sub> | <img src="https://img.shields.io/github/stars/valentynkit/jev-belay?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/valentynkit/jev-belay?style=flat&logo=github&label=" alt="updated"> |
| **[gtaras7/typesafe-jev](https://github.com/gtaras7/typesafe-jev)**<br><sub>created 2026-09-17 · Experiments in building software around a decision model instead of a chat prompt. Each piece is self-contained with its own README, tests and measured results.</sub> | <img src="https://img.shields.io/github/stars/gtaras7/typesafe-jev?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/gtaras7/typesafe-jev?style=flat&logo=github&label=" alt="updated"> |
| **[legacybridge-tech/pi-typesafe-jev](https://github.com/legacybridge-tech/pi-typesafe-jev)**<br><sub>created 2026-09-17 · Exposes the judgments as five tools, so the model makes narrow semantic calls while your code keeps control of thresholds and weights.</sub> | <img src="https://img.shields.io/github/stars/legacybridge-tech/pi-typesafe-jev?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/legacybridge-tech/pi-typesafe-jev?style=flat&logo=github&label=" alt="updated"> |
| **[GiesN/typesafe-jev-workflow](https://github.com/GiesN/typesafe-jev-workflow)**<br><sub>created 2026-09-16 · Deliberately small and complete: a mocked email goes in, a typed Choice comes out, and it routes to a demo handler. The clearest minimal wiring in the list.</sub> | <img src="https://img.shields.io/github/stars/GiesN/typesafe-jev-workflow?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/GiesN/typesafe-jev-workflow?style=flat&logo=github&label=" alt="updated"> |
| **[TypeSafeAI/typesafe-playground](https://github.com/TypeSafeAI/typesafe-playground)**<br><sub>created 2026-09-16 · 110 use cases you can edit and run in the browser. Zero install — the fastest way to feel the latency difference for yourself.</sub> | <img src="https://img.shields.io/github/stars/TypeSafeAI/typesafe-playground?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/TypeSafeAI/typesafe-playground?style=flat&logo=github&label=" alt="updated"> |

<h2 id="domain">🎯 Domain apps <sub>3</sub></h2>

<p><em>Jev pointed at one specific problem.</em></p>

| Project | Stars · Updated |
|:--------------------------------------------------------|--------------------:|
| **[Hangzhi/diffusion-jev-sglang](https://github.com/Hangzhi/diffusion-jev-sglang)**<br><sub>created 2026-09-21 · A diffusion model that runs Jev-style typed decisions on images — guess the doodle, name the flower, pick an emoji. Whether Jev's shape generalises past text, tested.</sub> | <img src="https://img.shields.io/github/stars/Hangzhi/diffusion-jev-sglang?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/Hangzhi/diffusion-jev-sglang?style=flat&logo=github&label=" alt="updated"> |
| **[shitianfang/jev-use](https://github.com/shitianfang/jev-use)**<br><sub>created 2026-09-19 · Hands the agent steps that need no text output to Jev, with the numbers stated up front: p50 around 230 ms. Chinese docs.</sub> | <img src="https://img.shields.io/github/stars/shitianfang/jev-use?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/shitianfang/jev-use?style=flat&logo=github&label=" alt="updated"> |
| **[cline/plugins](https://github.com/cline/plugins)**<br><sub>created 2026-05-31 · Cline's official plugin index, and one of its curated entries is a browser plugin that deliberately runs with no LLM in the loop. Worth watching as an integration surface.</sub> | <img src="https://img.shields.io/github/stars/cline/plugins?style=flat&logo=github&label=" alt="stars"> <img src="https://img.shields.io/github/last-commit/cline/plugins?style=flat&logo=github&label=" alt="updated"> |

<h2 id="hot">📈 Most starred (ranked automatically)</h2>

<em>Generated by `scripts/gen_readme.py` from `data/stars.json`. ⛔ Never hand-edited. Counts cannot go stale — the badges are live.</em>

| # | Project | Stars | Created |
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

<h2 id="choose">🧭 How to choose</h2>

**Want to understand Jev** → `browser-use/jev-ultrafast`. The biggest cost cut in the ecosystem — read how the single decision is made.

**Want to use it tomorrow** → `tamaratran/fast-jev-compaction` for Claude Code, `browser-use/jev-ultrafast` for browser automation.

**Want to ship your own** → start from `kerpopule/hermes-jev-skills`; the loop is already wired.

---

### About

An **independent, unaffiliated** catalog of Jev projects.
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

**43 projects across 8 categories**; 43 have a written
reason and the rest are being written — ⭐ **writing those reasons is the
content of this list, not the cleanup afterwards.**

**On Jev:** it is TypeSafe AI's System One model. It does not generate text —
it returns a single decision over a set of typed options, in tens to hundreds of
milliseconds. Vendor-reported performance numbers are cited to their source.

MIT licensed. Inclusion criteria are in [CONTRIBUTING.md](CONTRIBUTING.md).
