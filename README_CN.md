# PPT Master（fork）+ PPT Defense

[English](./README.md) | [中文](./README_CN.md)

> 本仓库是 [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) 的 **fork**（MIT）。  
> 分支 [`feat/ppt-defense`](https://github.com/Siuuusean-52991/ppt-master/tree/feat/ppt-defense) 新增 **PPT Defense**：双层导航 + 答辩式备注，用于面试 / 答辩质询翻页。

---

## 傻瓜上手（直接复制给 Agent）

### 第一步 — 安装 Skill

把下面整段发给 Cursor / Claude Code / Codex 等 Agent：

```text
请到 GitHub 搜索 Skill「PPT Defense」（仓库 Siuuusean-52991/ppt-master，
分支 feat/ppt-defense），并帮我安装：

1）把上游 ppt-master skill 安装/同步到 ~/.cursor/skills/ppt-master
   （可用本 fork 的 skills/ppt-master，或 hugohe3/ppt-master）。
2）把 PPT Defense 叠加 skill 安装到 ~/.cursor/skills/ppt-defense
   （来自 feat/ppt-defense 分支的 skills/ppt-defense）。
3）确认两个目录都在，并跑通 ppt-master 的 attribution_guard。
```

### 第二步 — 生成答辩 / 面试 PPT

把素材丢进对话（PDF / Word / Markdown / 飞书链接 / 文件夹），再粘贴：

```text
请使用 PPT Defense 这个 Skill，根据我刚提供的素材，帮我生成一份面试/答辩用 PPT。

要求：
- 顶栏双层导航（章节栏 + 章内页栏），点击可 #slide-N 跳转
- 每页备注写成 Q: / A: 质询对答
- 用 ppt-master 导出原生可编辑 .pptx
- 不要编造无法核实的数据；说不清的要标明缺口
```

完成。Agent 会用 ppt-master 做生成/导出，用 PPT Defense 做导航和答辩备注。

---

## 你能得到什么

### 上游 PPT Master（仍然是引擎）

**可编辑已经是基本盘——关键是你真正拿到多少 PowerPoint 能力。** PPT Master 面向原生对象模型：可调手柄的形状与连接线、按需数据图表与表格，以及完整的文字 / 图片 / 填充 / 效果模型——点选元素即可当原生对象继续改。模板 / 结构化路线还能带上真正的母版与版式（`p:sldMaster` / `p:sldLayout`）。

它是跑在「能调用 Agent 的 AI 工具」里的 **工作流 Skill**：你说「用这份 PDF 做一版 PPT」，它在本地跑完并导出原生可编辑 `.pptx`。你只需装好 Python + AI Agent，再丢素材。

主要路线（各有明确的「保留什么」约定）：

| 路线 | 做什么 |
|---|---|
| **Generate** | 文档 / 主题 → 设计好的 SVG 页 → 原生 PPTX |
| **Create Template** | 从参考提炼可复用品牌 / 样式 / 版式 / 整套模板 |
| **Fill Native PPTX** | 往已有 `.pptx` 填内容并尽量保留设计 |
| **Enhance Native PPTX** | 给成品加切换、动画、旁白等 |

上游定位里的三条承诺：

- **成本可预期** — 开源；你只付所用 AI 模型的费用
- **数据尽量本地** — 除模型 API 通信外，流水线在本机跑
- **不绑死平台** — 只要是能跑 Agent 的 AI IDE 都能驱动

> [!IMPORTANT]
> ### 这是工具，不是许愿池
> `harness + model = agent` — PPT Master / PPT Defense 负责流程；**模型**决定上限。素材多时优先用长上下文强模型。别期待一次完美定稿；价值是去掉大部分苦力活，让你在**原生可编辑**稿上继续打磨。

上游深文档（本 fork 保留）：[Why PPT Master](./docs/why-ppt-master.md) · [Getting Started](./docs/getting-started.md) · [PowerPoint ↔ SVG Mapping](./docs/powerpoint-svg-mapping.md)

### 本 fork 的 PPT Defense

| 能力 | 答辩场景为什么有用 |
|---|---|
| **双层导航** | 被打断时快速跳章 / 跳页 |
| **`nav_map.json`** | 章节与页码的单一事实来源 |
| **答辩备注** | PowerPoint 备注栏里的 `Q:` / `A:` 对答稿 |
| **注入 / 校验脚本** | 改页序后批量刷新顶栏 |

详情：[`skills/ppt-defense/`](./skills/ppt-defense/) · 口径：[`docs/FORK.md`](./docs/FORK.md)

---

## 手动安装（Agent 需要路径时）

```bash
git clone -b feat/ppt-defense https://github.com/Siuuusean-52991/ppt-master.git
cd ppt-master
python3 -m venv .venv && source .venv/bin/activate   # 建议
pip install -r requirements.txt

mkdir -p ~/.cursor/skills
cp -R skills/ppt-master ~/.cursor/skills/ppt-master
cp -R skills/ppt-defense ~/.cursor/skills/ppt-defense

python3 ~/.cursor/skills/ppt-master/scripts/attribution_guard.py
```

依赖：Python 3 + [pandoc](https://pandoc.org/)（Windows 可参考上游 [安装指南](./docs/windows-installation.md)）。

---

## 更多可直接粘贴的提示词

```text
用 PPT Defense。根据 ./sources/ 做 16:9 答辩稿，约 15–20 页，
章节：介绍 / 开场 / 项目 / 方法 / 证据 / 收束。要双层导航 + Q/A 备注。
```

```text
我已有 svg_output/。只用 PPT Defense 的 inject_dual_nav.py 按 nav_map.json
刷新双层导航，然后重新导出 PPTX（另存，不要覆盖旧文件）。
```

---

## 许可证与归属

- 许可证：[MIT](./LICENSE)（与上游一致）
- 上游项目：[hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)
- 本 fork 增量：`skills/ppt-defense/`

上游 README 中的赞助展示与维护者个人介绍已省略；需要原文请看上游仓库。`SPONSORS.md` 等占位文件仅用于保持官方 skill 归属门禁完整。
