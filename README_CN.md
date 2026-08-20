# PPT Master（fork）+ PPT Defense

[English](./README.md) | [中文](./README_CN.md)

> 本仓库是 [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) 的 **fork**（MIT）。  
> 分支 [`feat/ppt-defense`](https://github.com/Siuuusean-52991/ppt-master/tree/feat/ppt-defense)：**PPT Defense = 扩容包**——只装 **一个** Cursor Skill，即可同时获得完整 ppt-master + 双层导航 / 答辩备注。

---

## 傻瓜上手（复制给 Agent）

### 第一步 — 只装 PPT Defense

```text
请到 GitHub 搜索 Skill「PPT Defense」
（仓库 Siuuusean-52991/ppt-master，分支 feat/ppt-defense），
并按「扩容包 / 单 Skill」方式帮我安装：

目标目录：
  ~/.cursor/skills/ppt-defense/
    SKILL.md
    ppt-master/     ← 内嵌完整上游引擎
    scripts/ …      ← 答辩工具

做法：
1）拉取该分支的 skills/ppt-defense + skills/ppt-master
   （可用 sparse checkout；或把已有 ppt-master 当作 --master-src）。
2）执行：./skills/ppt-defense/install.sh -y
3）确认 attribution_guard 在
   ~/.cursor/skills/ppt-defense/ppt-master/scripts/ 下通过。
4）不要再让我单独安装 ppt-master —— 已经嵌在 PPT Defense 里面了。
```

### 第二步 — 生成

把素材丢进对话，然后说：

```text
请使用 PPT Defense 根据我的素材生成 PPT。

我只安装了 PPT Defense：请用它内嵌的 ppt-master 引擎。
若是面试/答辩场景：加上双层 #slide-N 导航和 Q:/A: 备注。
导出原生可编辑 .pptx。不要编造无法核实的数据。
```

---

## 「只装一个」是什么意思

| 层级 | 安装后位置 | 能力 |
|---|---|---|
| **ppt-master**（引擎） | `~/.cursor/skills/ppt-defense/ppt-master/` | 生成 / 模板 / 填充 / 增强 → 原生 PPTX |
| **PPT Defense**（扩容） | `~/.cursor/skills/ppt-defense/` | 双层导航 + 答辩 `Q:`/`A:` 备注 |

Cursor 只需要发现 **`ppt-defense`**。详见 [`skills/ppt-defense/BUNDLE.md`](./skills/ppt-defense/BUNDLE.md)。

---

## 你能得到什么

### 上游 PPT Master（内嵌引擎）

**可编辑已经是基本盘——关键是你真正拿到多少 PowerPoint 能力。** PPT Master 面向原生对象模型：可调手柄的形状与连接线、按需数据图表与表格，以及完整的文字 / 图片 / 填充 / 效果模型。模板 / 结构化路线还能带上真正的母版与版式。

它是跑在 Agent 里的工作流：你说「用这份 PDF 做 PPT」，它在本地导出原生可编辑 `.pptx`。

| 路线 | 做什么 |
|---|---|
| **Generate** | 文档 / 主题 → SVG 页 → 原生 PPTX |
| **Create Template** | 提炼可复用模板 |
| **Fill Native PPTX** | 往已有 PPTX 填内容并尽量保留设计 |
| **Enhance Native PPTX** | 给成品加切换 / 动画 / 旁白 |

- **成本可预期** — 开源；只付模型费用  
- **数据尽量本地** — 除模型 API 外在本机跑  
- **不绑死平台** — 能跑 Agent 的 AI IDE 均可  

> [!IMPORTANT]
> ### 这是工具，不是许愿池
> `harness + model = agent` — 流程是 skill 的；**模型**决定上限。素材多时用长上下文强模型。

上游深文档：[Why PPT Master](./docs/why-ppt-master.md) · [Getting Started](./docs/getting-started.md) · [PowerPoint ↔ SVG Mapping](./docs/powerpoint-svg-mapping.md)

### PPT Defense（扩容）

| 能力 | 用途 |
|---|---|
| **双层导航** | 质询时跳章 / 跳页 |
| **`nav_map.json`** | 结构单一事实来源 |
| **答辩备注** | 备注栏 `Q:` / `A:` |
| **`install.sh`** | 一键装成单 Skill |

---

## 手动安装

```bash
git clone --filter=blob:none --sparse -b feat/ppt-defense \
  https://github.com/Siuuusean-52991/ppt-master.git
cd ppt-master
git sparse-checkout set skills/ppt-defense skills/ppt-master
./skills/ppt-defense/install.sh -y
```

已有 ppt-master 副本时：

```bash
./skills/ppt-defense/install.sh -y --master-src /path/to/ppt-master
```

---

## 许可证与归属

- 许可证：[MIT](./LICENSE)
- 上游：[hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)
- 扩容层：`skills/ppt-defense/`

本 fork README 省略赞助与个人介绍；内嵌 `ppt-master/` 仍保留 `attribution_guard` 所需文件。
