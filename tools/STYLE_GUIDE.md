# 双语设计报告 · 写作与翻译规范

本文件是《硅基生命蓝图》中文组与英文组的统一规范，用于保证两种语言版本在结构、术语与语气上一致。

## 1. 目录分组

| 目录 | 内容 | 语言 |
|---|---|---|
| `zh-CN/` | 12 册规范化中文设计报告 + 中文术语表 + 中文目录 | 简体中文 |
| `en-US/` | 与中文组逐册对应的 12 册英文设计报告 + 英文术语表 + 英文目录 | English |
| `archive/original-zh/` | 原始中文稿件（仅作追溯，不属于现行设计报告） | 简体中文 |
| `tools/` | 规范化脚本与本文档 | — |
| `README.md` | 双语入口与导航 | 中文 + English |

## 2. 文件命名映射（编号一一对应）

| 编号 | `zh-CN/` | `en-US/` |
|---|---|---|
| 00 | `00_哲学层_设计.md` | `00-Philosophical-Foundations.md` |
| 01 | `01_DNA信息层_设计.md` | `01-DNA-Information-Layer.md` |
| 02 | `02_硅基材料工艺_设计.md` | `02-Silicon-Materials-and-Process.md` |
| 03 | `03_能量代谢_设计.md` | `03-Energy-Metabolism.md` |
| 04 | `04_边界个体性_设计.md` | `04-Boundary-and-Individuality.md` |
| 05 | `05_神经网络_设计.md` | `05-Neural-Network.md` |
| 06 | `06_世界模型_设计.md` | `06-World-Model.md` |
| 07 | `07_记忆系统_设计.md` | `07-Memory-System.md` |
| 08 | `08_逻辑推理_设计.md` | `08-Logical-Reasoning.md` |
| 09 | `09_本能行为_设计.md` | `09-Instinctive-Behavior.md` |
| 10 | `10_演化选择_设计.md` | `10-Evolutionary-Selection.md` |
| 11 | `11_系统整合_设计.md` | `11-System-Integration.md` |

## 3. 语言与语气（两种版本共同遵守）

- 使用客观第三人称与陈述语气；禁止第一人称、第二人称、读者称呼与对话体。
- 禁止内部过程记录：评审流水、文献抓取与核实日志、决策对话、版本库操作说明、时间戳、本地文件路径说明。
- 禁止口语、情绪化表达、主观绝对化评价、状态表情符号与「建议／推荐／默认」式的主观措辞。
- 设计选择以「设计决策 / Design decision」陈述；备选方案以「方案 A/B/C」标识，比较表列「适用条件」而非「适合谁」。
- 待验证项统一写作「待验证 / To be verified」，并注明供值方与验证方式；不得把未经验证的数值写成基准值。
- 引用标记中的文献 ID 与路径指向文献库中的具体文件，用于追溯与定位；文献库 `Reference Documentation/` 为项目本地配套资源，不随本版本库分发。不得引用内部工作清单、评审记录或抓取日志。
- 章节标题采用名词性短语（如「设计方案比选」「适用边界与已知限制」），不使用疑问句或口语标题。

## 4. 依据类别标记

| 中文 | English |
|---|---|
| `[引用:路径]` | `[Ref:path]`（路径与文件名原样保留） |
| `[设计决策]` | `[Design decision]` |
| `[逻辑推导]` | `[Logical derivation]` |
| `[待验证]` | `[To be verified]` |
| `[设计设定]` | `[Design setting]` |

标记内的文献编号、DOI、章节号与括号结构保持不变，仅翻译其中的说明性文字。

## 5. 编号、符号与图形

- 保持全部编号：`A1–A6`、`Φ-L1/L2/L3`、`S1–S6`、`I0–I8`、`C1–C4`、`P0/P1/P2`、`T0–T6`、`V1–V5`、`D1–D6`、`W1–W5`、`E1–E6` 等。
- `原则 N` 译为 `Design Principle N`；`分册 NN` 译为 `Volume NN`。
- 公式、单位、化学符号、希腊字母、数学比较符、箭头、圈码（①②③④⑤）与 mermaid 代码块内容原样保留；仅翻译图内必要的说明文字。
- 表格的列数、行序、对齐方式与引用标记逐行对应，不得合并或省略行。

## 6. 术语对照表（强制使用）

| 中文 | English |
|---|---|
| 硅基生命 | silicon-based life |
| 硅基生命蓝图 | Silicon-Based Life Blueprint |
| 碳基生命 / 碳基意识体 | carbon-based life / carbon-based conscious agents |
| 组织闭合 | organizational closure |
| 因果自含 | causally self-contained |
| 耗散结构 | dissipative structure |
| 远离热力学平衡 | far from thermodynamic equilibrium |
| 负熵 / 熵产生 | negentropy / entropy production |
| 内化目标 | internalized goal (teleonomy) |
| 自创生 | autopoiesis |
| 自催化集合 | autocatalytic set |
| (M,R) 代谢-修复系统 | (M,R) metabolism–repair system |
| 生命判据 | criteria of life |
| 因果独立性 | causal independence |
| 公理 / 公理层 | axiom / axiomatic layer |
| 哲学层 | philosophical layer |
| 双层规则 | two-layer rule structure |
| 价值中立 | value neutrality |
| 碳基协同 | cooperation with carbon-based life |
| 群落协同 | community cooperation |
| 适应度 / 适应度函数 | fitness / fitness function |
| 协同适应度项 | cooperation fitness term |
| 存续公理 | persistence axiom |
| 复制公理 | replication axiom |
| 适应公理 | adaptation axiom |
| 世界模型公理 | world-model axiom |
| 时标映射 | time-scale mapping |
| 压缩比 | compression ratio |
| 黑猩猩基准 | chimpanzee baseline |
| 设计决策 | design decision |
| 关键假设 | key assumption |
| 基线方案 | baseline option |
| 方案比选 | comparison of design options |
| 对照方案 | alternative option |
| 依据类别 | evidence category |
| 逻辑推导 | logical derivation |
| 设计设定 | design setting |
| 待验证 | to be verified |
| 一致性复核 | consistency review |
| 公开研究实践 | published research practice |
| 适用边界与已知限制 | scope and known limitations |
| 验证计划与待测定参数 | verification plan and parameters to be measured |
| 开放问题与后续工作 | open issues and follow-up work |
| 实施顺序 | implementation sequence |
| 横切约束落实 | implementation of cross-cutting constraints |
| 第一性原理计算（DFT） | first-principles calculation (DFT) |
| 实验验证 | experimental verification |
| 供值方 | value provider |
| DNA 信息层 | DNA information layer |
| 遗传信息层 | genetic information layer |
| 构造规则 | construction rules |
| 公理校验子 | axiom checksum |
| 复制保真度 | replication fidelity |
| 侧基键态 | side-group bonding state |
| 多缺陷簇 | multi-defect cluster |
| POMs 杂化凝胶 | POM-based hybrid gel |
| 离子束 / 原子层沉积（ALD） | ion beam / atomic layer deposition (ALD) |
| 载体 / 软载体 | carrier / soft carrier |
| 制造与表征 | fabrication and characterisation |
| 能量代谢 | energy metabolism |
| 能量获取、转化与分配 | energy acquisition, conversion and allocation |
| 能量币 | energy currency |
| 热电获取 | thermoelectric harvesting |
| 超级电容储能 | supercapacitor storage |
| 动态功率管理 | dynamic power management |
| 边界与个体性 | boundary and individuality |
| 个体性判据 | criteria of individuality |
| 人工播种 | artificial seeding |
| 涌现判活 | emergence-based viability assessment |
| 自维持 | self-maintenance |
| 神经网络 | neural network |
| 感知、决策与学习 | perception, decision-making and learning |
| 情绪调制 | affective modulation |
| 逻辑可压制情绪 | affect can be suppressed by logic |
| 突触 / 自生长突触 | synapse / self-growing synapse |
| 忆阻器 | memristor |
| 脉冲神经网络（SNN） | spiking neural network (SNN) |
| 世界模型 | world model |
| 循环状态空间模型（RSSM） | recurrent state-space model (RSSM) |
| 潜变量 | latent variable |
| 预测头 | prediction head |
| 试跑 / 推演 | rollout / simulation |
| 作用算子 | action operator |
| 记忆系统 | memory system |
| 记忆巩固 | memory consolidation |
| 显化突触结构 | explicit synaptic structure |
| 慢波睡眠 | slow-wave sleep |
| 表观遗传 | epigenetic inheritance |
| 跨代传递 | intergenerational transfer |
| 中心法则 | central dogma |
| 拉马克式 | Lamarckian |
| 逻辑推理 | logical reasoning |
| 命题推理 / 因果推断 | propositional reasoning / causal inference |
| 最小逻辑集 | minimal logic set |
| 本能行为 | instinctive behavior |
| I0 判定前提集 | I0 prerequisite set |
| 硬核心 / 软扩展 | hard core / soft extension |
| 中央模式发生器（CPG） | central pattern generator (CPG) |
| 条件反射 | conditioned reflex |
| 演化选择 | evolutionary selection |
| 变异 / 选择 / 代际 | mutation / selection / generation |
| 选择压力 | selection pressure |
| 质量多样性（QD） | quality-diversity (QD) |
| 奖励塑形 | reward shaping |
| 保留/淘汰接口 | retention/elimination interface |
| 开放演化 | open-ended evolution |
| 系统整合 | system integration |
| 总装 | final assembly |
| 五回路闭合 | closure of the five loops |
| 最小可构建集 | minimum buildable set |
| 接口契约 | interface contract |

## 7. 英文版文档控制块模板

```markdown
# 00 · Philosophical Foundations (Axioms, Two-Layer Rules and Time-Scale Mapping)

| Item | Value |
|---|---|
| Module | Philosophical foundations: axioms, two-layer rules and time-scale mapping |
| Document type | Design report (English edition) |
| Version | v2.1 |
| Dependencies | Upstream of all volumes; no dependencies |
| Language | English (Chinese edition: `../zh-CN/00_哲学层_设计.md`) |

> **Evidence categories**: `[Ref:…]` literature or data; `[Design decision]` project setting without external evidence, with adjustability stated; `[Logical derivation]` derived from listed premises and formulae; `[To be verified]` unvalidated values or methods, placeholder only, with the value provider named. Every key assertion carries one of these categories.
```

## 8. 英文版翻译完整性要求（强制）

1. 逐节、逐段、逐表格行完整翻译 `zh-CN/` 对应分册；不得摘要、压缩、改写或省略技术内容。
2. 章节编号、层级、表格行列、公式、代码块、图示说明、引用 ID 与文献路径一一对应。
3. 中文版中已删除的对话体、过程记录与主观措辞不得重新引入。
4. 不添加中文版没有的技术断言；允许且仅允许：英文文档控制块、依据类别说明、文件末尾的对应关系说明。
5. 每册末尾添加：`> Corresponding Chinese edition: \`../zh-CN/<中文文件名>\``。
6. 全文使用正式技术英语；避免第一/第二人称、缩略口语、主观评价与 emoji。

## 9. 写入要求

- 目标路径为 `d:/Tool Development/Silicon/Silicon-Biological-Blueprint/en-US/<映射文件名>`。
- 必须使用 UTF-8 编码写入。优先使用 `write_to_file`；若不可用，使用 Python `Path.write_text(text, encoding="utf-8")`，禁止使用默认 ANSI 编码的 PowerShell 重定向。
- 完成后回报：生成的文件名、章节数量、字符数与自检结果。

## 10. 自检清单

- [ ] 章节编号与中文版一致（`## 0` 至 `## 10`，含 `### 0.1`–`### 0.5`）。
- [ ] 表格行数与中文版一致，引用标记完整。
- [ ] 无中文残留（除文献库路径与中文文件名）。
- [ ] 无第一/第二人称、无 emoji、无「recommend / default / obviously / honestly」等主观措辞。
- [ ] 术语与第 6 节一致。
- [ ] 文件以 UTF-8 保存，末尾含对应关系说明。
