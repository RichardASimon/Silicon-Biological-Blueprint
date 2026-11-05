# 硅基生命蓝图 · Silicon-Based Life Blueprint

> 硅基生命 / 硅基生物系统的完整设计蓝图。
> 现行设计报告以中文与英文同时发布，并按语言分组存放；两组逐册对应，章节编号、公式、引用标记与术语保持一致。

| 语言组 | 目录 | 内容 |
|---|---|---|
| 简体中文 | [`zh-CN/`](zh-CN/README.md) | 12 册规范化中文设计报告、中文术语表、中文目录 |
| English | [`en-US/`](en-US/README.md) | 12 English design reports, English glossary, English index |

## 目录结构

```
Silicon-Biological-Blueprint/
├── README.md                      双语入口（本文件）
├── zh-CN/                         中文组
│   ├── README.md                  中文目录与阅读顺序
│   ├── GLOSSARY.md                中文术语表（附英文对照）
│   ├── 00_哲学层_设计.md
│   ├── ……（01–10）
│   └── 11_系统整合_设计.md
├── en-US/                         英文组
│   ├── README.md                  English index and reading order
│   ├── GLOSSARY.md                English glossary (with Chinese equivalents)
│   ├── 00-Philosophical-Foundations.md
│   ├── ……（01–10）
│   └── 11-System-Integration.md
├── archive/original-zh/           原始中文稿件（仅供追溯，不属于现行报告）
└── tools/
    ├── STYLE_GUIDE.md             双语写作与翻译规范、完整术语对照表
    └── normalize_docs.py          中文表述规范化脚本（可复现、可校验）
```

## 分册对照索引

| 编号 | 中文版 | English edition |
|---|---|---|
| 00 | [哲学层：基础公理、双层规则与时标映射](zh-CN/00_哲学层_设计.md) | [Philosophical Foundations](en-US/00-Philosophical-Foundations.md) |
| 01 | [DNA 信息层（S1）](zh-CN/01_DNA信息层_设计.md) | [DNA Information Layer](en-US/01-DNA-Information-Layer.md) |
| 02 | [硅基材料工艺](zh-CN/02_硅基材料工艺_设计.md) | [Silicon Materials and Process](en-US/02-Silicon-Materials-and-Process.md) |
| 03 | [能量代谢（S3）](zh-CN/03_能量代谢_设计.md) | [Energy Metabolism](en-US/03-Energy-Metabolism.md) |
| 04 | [边界与个体性（S4）](zh-CN/04_边界个体性_设计.md) | [Boundary and Individuality](en-US/04-Boundary-and-Individuality.md) |
| 05 | [神经网络（S2）](zh-CN/05_神经网络_设计.md) | [Neural Network](en-US/05-Neural-Network.md) |
| 06 | [世界模型（S5）](zh-CN/06_世界模型_设计.md) | [World Model](en-US/06-World-Model.md) |
| 07 | [记忆系统](zh-CN/07_记忆系统_设计.md) | [Memory System](en-US/07-Memory-System.md) |
| 08 | [逻辑推理](zh-CN/08_逻辑推理_设计.md) | [Logical Reasoning](en-US/08-Logical-Reasoning.md) |
| 09 | [本能行为](zh-CN/09_本能行为_设计.md) | [Instinctive Behavior](en-US/09-Instinctive-Behavior.md) |
| 10 | [演化选择（S6）](zh-CN/10_演化选择_设计.md) | [Evolutionary Selection](en-US/10-Evolutionary-Selection.md) |
| 11 | [系统整合](zh-CN/11_系统整合_设计.md) | [System Integration](en-US/11-System-Integration.md) |

## 阅读顺序

1. `00` 哲学层：公理、双层规则与时标映射（最底层，先确定）。
2. `01`–`10` 各分册：按依赖顺序，分别给出信息、材料、能量、边界、神经、世界模型、记忆、逻辑、本能与演化的设计。
3. `11` 系统整合：总装、五回路闭合与最小可构建集。
4. 各册 `§5` 验证计划与 `§10` 适用边界与已知限制：明确待验证项与已知限制。

## 本次优化说明

- **表述规范化**：删除对话体、第一/第二人称、内部过程记录（评审流水、文献抓取日志、决策对话、版本库操作说明）、口语与主观评价、状态表情符号；章节标题改为名词性短语；依据标注与设计决策改为规范陈述；统一文档控制块。
- **双语分组**：`zh-CN/` 与 `en-US/` 各含完整 12 册，逐册对应；`tools/STYLE_GUIDE.md` 规定术语、依据类别标记、编号与图形的处理规则，保证两版一致。
- **原文归档**：`archive/original-zh/` 保留原始中文稿件供追溯，不参与现行报告阅读。
- **可复现清洗**：`tools/normalize_docs.py` 从归档原文生成 `zh-CN/`，并输出残留表述校验结果。

## 文档约定

- 版本：按册标注 v2.1–v4.1；两种语言版本号一致。
- 依据类别：`[引用:…]` / `[Ref:…]` 指向文献库中的具体文件；`[设计决策]` / `[Design decision]` 为无外部依据的项目设定；`[逻辑推导]` / `[Logical derivation]` 由已列前提导出；`[待验证]` / `[To be verified]` 仅作占位并注明供值方。
- 文献库 `Reference Documentation/` 为项目本地配套资源，不随本版本库分发；引用标记中的文献 ID 与路径用于追溯与定位。
- 未给出实测值的参数一律列为待验证项，不作为设计基准值。

---

# Silicon-Based Life Blueprint

> A complete design blueprint for silicon-based life / silicon-based biological systems.
> The current design reports are published in both Chinese and English, grouped by language. The two sets correspond volume by volume, with identical section numbering, formulae, reference tags and terminology.

| Language | Directory | Contents |
|---|---|---|
| 简体中文 | [`zh-CN/`](zh-CN/README.md) | 12 standardised Chinese design reports, Chinese glossary, Chinese index |
| English | [`en-US/`](en-US/README.md) | 12 English design reports, English glossary, English index |

## Structure

- `zh-CN/` — Chinese edition (normative full text).
- `en-US/` — English edition, corresponding volume by volume to the Chinese edition.
- `archive/original-zh/` — Original Chinese drafts, retained for traceability only; not part of the current reports.
- `tools/STYLE_GUIDE.md` — Bilingual writing and translation rules, including the complete terminology table.
- `tools/normalize_docs.py` — Reproducible normalisation script for the Chinese edition, with a residual-wording check.

## Volume Index

See [the table above](#分册对照索引) for the 12 corresponding volume pairs (00–11).

## Reading Order

1. Volume 00 — axioms, two-layer rule structure and time-scale mapping.
2. Volumes 01–10 — information, materials, energy, boundary, neural, world-model, memory, logic, instinct and evolution layers.
3. Volume 11 — system integration, closure of the five loops and the minimum buildable set.
4. Section 5 (verification plan) and Section 10 (scope and known limitations) of each volume.

## Optimisation Summary

- **Wording**: Removed conversational style, first/second person, internal process records, colloquial or subjective expressions and status emojis; section titles, evidence tags and design decisions were rewritten in formal report language; document control blocks were unified.
- **Bilingual grouping**: `zh-CN/` and `en-US/` each contain the complete 12 volumes; `tools/STYLE_GUIDE.md` governs terminology, evidence tags, identifiers and diagrams.
- **Traceability**: Original drafts are archived in `archive/original-zh/`.

## Conventions

- Versions are recorded per volume (v2.1–v4.1) and are identical across languages.
- Evidence categories: `[Ref:…]` literature or data; `[Design decision]` project setting without external evidence; `[Logical derivation]` derived from listed premises; `[To be verified]` placeholder with a named value provider.
- The `Reference Documentation/` library is a local companion resource and is not distributed with this repository; the literature IDs and paths in reference tags serve traceability and retrieval.
- Parameters without measured values are listed as verification items and are not used as design baselines.
