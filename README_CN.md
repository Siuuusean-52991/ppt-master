# PPT Master（fork）+ PPT Defense

[English](./README.md) | [中文](./README_CN.md)

> 本仓库是 [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master) 的 **fork**（MIT）。  
> 分支 [`feat/ppt-defense`](https://github.com/Siuuusean-52991/ppt-master/tree/feat/ppt-defense) 新增叠加 skill **PPT Defense**，面向答辩 / 面试 / 质询翻页。

## 这个 fork 做什么

| 层级 | 作用 |
|---|---|
| **ppt-master**（上游 skill） | 从文档 / brief 生成原生可编辑 PPTX（SVG → 质检 → 导出） |
| **PPT Defense**（`skills/ppt-defense`） | 双层可点击导航 + 答辩式备注（`Q:` / `A:`），方便质询时跳转 |

适合需要在压力下快速跳章答问的场景，不是官网营销页。

## PPT Defense（本分支）

目录：[`skills/ppt-defense/`](./skills/ppt-defense/)

1. 双层导航：一级=章节（跳到该章首页）；二级=当前章内各页（`#slide-N`）。
2. 备注格式：`notes/` 里用 `Q:` / `A:` 写质询对答。
3. 工具：`nav_map.json` 校验 + 注入 SVG 顶栏。

### Cursor 安装

```bash
# 上游运行时（必需）
# 将 skills/ppt-master 安装到 ~/.cursor/skills/ppt-master

# 叠加 skill
cp -R skills/ppt-defense ~/.cursor/skills/ppt-defense
# 或: ln -s "$PWD/skills/ppt-defense" ~/.cursor/skills/ppt-defense
```

### 项目内快速用法

```bash
# ppt-master 已生成 <project>/svg_output/ 之后
python3 skills/ppt-defense/scripts/validate_nav_map.py /path/to/project
python3 skills/ppt-defense/scripts/inject_dual_nav.py /path/to/project
# 再用 ppt-master 的 finalize / 质检 / svg_to_pptx 导出
```

详见 [`skills/ppt-defense/README.md`](./skills/ppt-defense/README.md) 与 [`skills/ppt-defense/SKILL.md`](./skills/ppt-defense/SKILL.md)。

## 上游 ppt-master

生成、模板、质检、导出仍走上游 skill：

- 入口：[`skills/ppt-master/SKILL.md`](./skills/ppt-master/SKILL.md)
- 官方上游：https://github.com/hugohe3/ppt-master

**不要**删除 `LICENSE`、skill 归属元数据或 `attribution_guard` 相关门禁。

## 文档索引

| 文档 | 用途 |
|---|---|
| [`skills/ppt-defense/`](./skills/ppt-defense/) | 本 fork 重点：答辩叠加 skill |
| [`skills/ppt-master/`](./skills/ppt-master/) | 上游生成 skill |
| [`docs/FORK.md`](./docs/FORK.md) | 相对上游：保留 / 省略了什么 |
| [`CONTRIBUTING.md`](./CONTRIBUTING.md) | 上游贡献说明（给上游提 PR 请走原仓库） |

## 许可证与归属

- 许可证：[MIT](./LICENSE)（与上游一致）。
- 上游作者 / 项目：[Hugo He / ppt-master](https://github.com/hugohe3/ppt-master)。
- 本 fork 增量：`skills/ppt-defense/` 下的 PPT Defense。

上游 README 中的赞助展示、联盟链接、维护者个人介绍等，**本 fork 文档已省略**。如需原文，请查看 [上游仓库](https://github.com/hugohe3/ppt-master)。
