# Silicon-Biological-Blueprint

> An engineering design for a silicon-based living system: the criteria that make it alive, the subsystems that implement it, and the tests that would settle each claim.
> 一套硅基生命系统的工程设计：判定它「算不算活着」的判据、实现这些判据的子系统，以及检验每条主张的方法。

---

## English

### What this repository is

This is a design specification in 12 linked volumes. It is not a product, a running simulation, or a popular-science essay. It works through one engineering question: **if a life-form were built on silicon instead of carbon, which functions would it need, how would those functions be realised in materials, energy, information and rules, and what could we observe to decide whether the result is alive?**

The answer is deliberately concrete. The volumes name physical carriers, energy budgets, boundary conditions, memory and reasoning mechanisms, and an evolutionary loop. They also state where a number is a measurement, where it is a project decision, and where it is still unknown.

Three commitments hold the set together:

- **Life is a testable condition.** An individual counts as alive only if it shows organizational closure, dissipation, an internalized goal and causal independence (Volume 00, criteria C1–C4). The point is to replace the phrase "a machine simulating life" with something that can be checked.
- **Rules have two layers.** The philosophical layer (Φ-L1/L2/L3) is fixed; the axiomatic rule layer may evolve, but always under the cooperation constraint A6. This is how cooperation with carbon-based life is made into a selection pressure rather than a stated intention.
- **Every claim carries its evidence class.** Statements are tagged as literature or data, project decision, logical derivation, or unverified placeholder. Unmeasured parameters are listed as verification items, never presented as design baselines.

### The 12 volumes

| No. | Volume | Question it answers |
|---|---|---|
| 00 | [Philosophical Foundations](en-US/00-Philosophical-Foundations.md) · [哲学层](zh-CN/00_哲学层_设计.md) | What counts as alive, which rules may never change, and how carbon-based time scales map onto a silicon individual |
| 01 | [DNA Information Layer](en-US/01-DNA-Information-Layer.md) · [DNA 信息层](zh-CN/01_DNA信息层_设计.md) | What is inherited, how it is stored and repaired, and how copying stays faithful (S1) |
| 02 | [Silicon Materials and Process](en-US/02-Silicon-Materials-and-Process.md) · [硅基材料工艺](zh-CN/02_硅基材料工艺_设计.md) | Which physical carrier can hold information states, and how they are written, read and encapsulated |
| 03 | [Energy Metabolism](en-US/03-Energy-Metabolism.md) · [能量代谢](zh-CN/03_能量代谢_设计.md) | How energy is acquired, converted and budgeted to maintain the ordered state (S3) |
| 04 | [Boundary and Individuality](en-US/04-Boundary-and-Individuality.md) · [边界与个体性](zh-CN/04_边界个体性_设计.md) | Where one individual ends, and how causal self-containment is maintained (S4) |
| 05 | [Neural Network](en-US/05-Neural-Network.md) · [神经网络](zh-CN/05_神经网络_设计.md) | How sensing, action and cooperation between individuals are wired (S2) |
| 06 | [World Model](en-US/06-World-Model.md) · [世界模型](zh-CN/06_世界模型_设计.md) | How the individual predicts the next state of its environment before acting (S5) |
| 07 | [Memory System](en-US/07-Memory-System.md) · [记忆系统](zh-CN/07_记忆系统_设计.md) | What is retained, for how long, and how consolidation interacts with the compressed time scale |
| 08 | [Logical Reasoning](en-US/08-Logical-Reasoning.md) · [逻辑推理](zh-CN/08_逻辑推理_设计.md) | Which minimal inference operators are required, and how they can override instinct |
| 09 | [Instinctive Behavior](en-US/09-Instinctive-Behavior.md) · [本能行为](zh-CN/09_本能行为_设计.md) | Which behaviours follow from the axioms and which are simply chosen by the design |
| 10 | [Evolutionary Selection](en-US/10-Evolutionary-Selection.md) · [演化选择](zh-CN/10_演化选择_设计.md) | How variation and selection operate, including individual and group emergence and the cooperation fitness term (S6) |
| 11 | [System Integration](en-US/11-System-Integration.md) · [系统整合](zh-CN/11_系统整合_设计.md) | How the subsystems close into five loops, and what the smallest buildable system is |

Volumes 00, 04, 10 and 11 also contain the framework for observing and judging emergence: what would count as emergence in a single individual or in a group, which measurable quantities decide it, and which experiments would falsify the claim.

### How to read

- **For the overall argument**: read 00, then 11. Volume 00 states the axioms and constraints; Volume 11 shows what satisfying them requires once all subsystems are assembled.
- **For a subsystem**: in volumes 03–10, Section 5 lists the pending experimental and DFT work, and Section 10 states the scope and known limitations. Volume 01 puts its verification items in Section 9; Volume 02 ends at Section 5 (pending experimental work) and has no Section 10.
- **For a specific claim**: use the evidence tags. `[To be verified]` items are proposals, not results, and always name the source that should supply the value.

### Scope and limits

The design assumes a silicon-based individual that lives far from thermodynamic equilibrium, maintains itself by a continuous energy flow, and evolves in a world model before any rule is applied to the real world. It does not claim that such a system has been built. No parameter without a measured value is treated as a baseline. Reference tags carry literature IDs for locating sources; the source documents themselves are not distributed with this repository.

### Conventions

- The English and Chinese editions contain the same 12 volumes, with identical section numbering, formulae, tables, reference tags and version numbers per volume.
- Evidence categories: `[Ref:…]` literature or data; `[Design decision]` project setting without external evidence; `[Logical derivation]` derived from listed premises; `[To be verified]` placeholder pending a value. The Chinese edition uses `[引用:…]`、`[设计决策]`、`[逻辑推导]`、`[待验证]`.
- Subsystem codes S1–S6 refer to the information, neural, energy, boundary, world-model and evolutionary layers respectively.

---

## 中文

### 这套文档是什么

这是一套由 12 册相互衔接的设计报告，不是产品说明、可运行仿真，也不是科普文章。它只处理一个工程问题：**如果以硅而非碳为物质基底构建生命，需要具备哪些功能；这些功能如何落到材料、能量、信息与规则上；又该观察什么，才能判断造出来的系统确实「活着」，而不只是在模拟生命。**

报告尽量写到可核对的粒度：指定物理载体、能量预算、边界条件、记忆与推理机制、演化回路；同时区分哪些数字来自实测、哪些是项目设定、哪些至今没有数值。

贯穿全书的三条基本立场：

- **「生命」是可检验的条件。** 个体只有同时具备组织闭合、耗散、内化目标与因果独立性，才被判定为生命（00 册 C1–C4）。这样就把「一台模拟生命的机器」这类说法换成可以逐项核对的判据。
- **规则分两层。** 哲学层（Φ-L1/L2/L3）不可演化；公理规则层可以演化，但始终受协同适应度项 A6 约束。与碳基生命协同因此成为选择压力，而不是一句声明。
- **每条主张都标明依据类别。** 正文用标记区分文献或数据、项目设定、逻辑推导与待验证占位。没有实测值的参数一律列为验证项，不作为设计基准值。

### 12 册内容

| 编号 | 分册 | 回答的问题 |
|---|---|---|
| 00 | [哲学层](zh-CN/00_哲学层_设计.md) · [English](en-US/00-Philosophical-Foundations.md) | 什么算活着；哪些规则永远不可改；碳基时标如何映射到硅基个体 |
| 01 | [DNA 信息层](zh-CN/01_DNA信息层_设计.md) · [English](en-US/01-DNA-Information-Layer.md) | 遗传什么、存在哪里、如何修复，复制如何保真（S1） |
| 02 | [硅基材料工艺](zh-CN/02_硅基材料工艺_设计.md) · [English](en-US/02-Silicon-Materials-and-Process.md) | 哪种物理载体能承载信息态，如何写入、读取与封装 |
| 03 | [能量代谢](zh-CN/03_能量代谢_设计.md) · [English](en-US/03-Energy-Metabolism.md) | 能量如何获取、转换与分配，以维持远离平衡的有序态（S3） |
| 04 | [边界个体性](zh-CN/04_边界个体性_设计.md) · [English](en-US/04-Boundary-and-Individuality.md) | 一个个体在哪里结束，因果自含如何维持（S4） |
| 05 | [神经网络](zh-CN/05_神经网络_设计.md) · [English](en-US/05-Neural-Network.md) | 感知、行动以及个体间协同如何连接（S2） |
| 06 | [世界模型](zh-CN/06_世界模型_设计.md) · [English](en-US/06-World-Model.md) | 个体如何在行动前预测环境的下一状态（S5） |
| 07 | [记忆系统](zh-CN/07_记忆系统_设计.md) · [English](en-US/07-Memory-System.md) | 记住什么、保留多久，巩固过程如何受压缩时标影响 |
| 08 | [逻辑推理](zh-CN/08_逻辑推理_设计.md) · [English](en-US/08-Logical-Reasoning.md) | 需要哪些最小推理算子，它们如何压制本能反应 |
| 09 | [本能行为](zh-CN/09_本能行为_设计.md) · [English](en-US/09-Instinctive-Behavior.md) | 哪些行为由公理导出，哪些只是设计选定 |
| 10 | [演化选择](zh-CN/10_演化选择_设计.md) · [English](en-US/10-Evolutionary-Selection.md) | 变异与选择如何运作，含个体与群体涌现、协同适应度项（S6） |
| 11 | [系统整合](zh-CN/11_系统整合_设计.md) · [English](en-US/11-System-Integration.md) | 各子系统如何闭合成五个回路，最小可构建集是什么 |

00、04、10、11 册还给出涌现的观察与判定框架：单个个体和群体分别出现什么才算涌现，用哪些可测量来判定，以及哪些实验能否证该判断。

### 怎么读

- **想把握整体论证**：先读 00，再读 11。00 给出公理与约束，11 展示全部子系统装配后满足这些约束需要什么。
- **想查某个子系统**：03–10 册的第 5 节是待实验验证／DFT，第 10 节是适用边界与已知限制；01 册的验证项在第 9 节，02 册只到第 5 节（待实验验证／DFT），没有第 10 节。
- **想核对某条主张**：看依据标记。标 `[待验证]` 的内容是提案而非结论，并注明应由哪一方提供数值。

### 适用边界

设计假定硅基个体工作在远离热力学平衡的耗散态，靠持续能量流维持自身，并在世界模型中先试错、再把规则用于真实世界。文档不主张这样的系统已经造出。未给出实测值的参数不作为基准值。引用标记中的文献 ID 仅用于定位来源，原文不随本版本库分发。

### 文档约定

- 中英两组各 12 册，章节编号、公式、表格、引用标记与逐册版本号一致。
- 依据类别：`[引用:…]` 文献或数据、`[设计决策]` 无外部依据的项目设定、`[逻辑推导]` 由已列前提导出、`[待验证]` 仅作占位并注明供值方；英文版对应 `[Ref:…]`、`[Design decision]`、`[Logical derivation]`、`[To be verified]`。
- 子系统代号 S1–S6 依次指信息层、神经层、能量层、边界层、世界模型层与演化层。
