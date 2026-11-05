# English Edition · Silicon-Based Life Blueprint Design Reports

> This directory contains the current English design reports (12 volumes). The Chinese edition is in [`../zh-CN/`](../zh-CN/README.md); the bilingual entry point is [`../README.md`](../README.md).

## Volumes

| No. | Volume | Subject | Chinese counterpart |
|---|---|---|---|
| 00 | [Philosophical Foundations](00-Philosophical-Foundations.md) | Axioms, two-layer rule structure, time-scale mapping | [00](../zh-CN/00_哲学层_设计.md) |
| 01 | [DNA Information Layer (S1)](01-DNA-Information-Layer.md) | Carrier, encoding, read-out and replication of genetic information | [01](../zh-CN/01_DNA信息层_设计.md) |
| 02 | [Silicon Materials and Process](02-Silicon-Materials-and-Process.md) | Physical carrier, fabrication and characterisation | [02](../zh-CN/02_硅基材料工艺_设计.md) |
| 03 | [Energy Metabolism (S3)](03-Energy-Metabolism.md) | Energy acquisition, conversion and allocation | [03](../zh-CN/03_能量代谢_设计.md) |
| 04 | [Boundary and Individuality (S4)](04-Boundary-and-Individuality.md) | Criteria of individuality, artificial seeding, individual/environment boundary | [04](../zh-CN/04_边界个体性_设计.md) |
| 05 | [Neural Network (S2)](05-Neural-Network.md) | Perception, decision-making, learning and affective modulation | [05](../zh-CN/05_神经网络_设计.md) |
| 06 | [World Model (S5)](06-World-Model.md) | Internal predictive model and action-consequence simulation | [06](../zh-CN/06_世界模型_设计.md) |
| 07 | [Memory System](07-Memory-System.md) | Memory hierarchy and explicit synaptic structure | [07](../zh-CN/07_记忆系统_设计.md) |
| 08 | [Logical Reasoning](08-Logical-Reasoning.md) | Propositional reasoning, causal inference and conditional simulation | [08](../zh-CN/08_逻辑推理_设计.md) |
| 09 | [Instinctive Behavior](09-Instinctive-Behavior.md) | I0 prerequisite set, I1–I8 instincts and affect | [09](../zh-CN/09_本能行为_设计.md) |
| 10 | [Evolutionary Selection (S6)](10-Evolutionary-Selection.md) | Fitness function, selection pressure and intergenerational transfer | [10](../zh-CN/10_演化选择_设计.md) |
| 11 | [System Integration](11-System-Integration.md) | Final assembly, closure of the five loops, minimum buildable set | [11](../zh-CN/11_系统整合_设计.md) |

## Reading Order

1. Volume 00 — axioms, two-layer rules and time-scale mapping.
2. Volumes 01–10 — subsystem designs in dependency order.
3. Volume 11 — final assembly and the minimum buildable set.
4. Section 5 and Section 10 of each volume — verification plan, scope and known limitations.

## Common Structure

| Section | Contents |
|---|---|
| Document control block | Module, document type, version, dependencies, language |
| Section 0 | Comparison of design options (A/B/C), combined option and baseline configuration, structural description |
| Section 1 | Design objectives |
| Section 2 | Related research and alternative implementations |
| Section 3 | Design: structure, mechanisms, formulae and interfaces |
| Section 4 | Relationships with other parts (interface contracts) |
| Section 5 | Verification plan and parameters to be measured |
| Section 10 | Scope and known limitations |

Volumes 00 and 11 differ slightly: the former includes axioms and design-decision records, the latter a project-wide verification summary and implementation sequence.

## Evidence Categories

| Tag | Meaning |
|---|---|
| `[Ref:…]` | Supported by literature or data; points to a specific file in the reference library |
| `[Design decision]` | Project setting without external evidence; adjustability is stated |
| `[Logical derivation]` | Derived from listed premises and formulae |
| `[To be verified]` | Unvalidated value or method; placeholder only, with a named value provider |

Every key assertion carries one of these categories. The `Reference Documentation/` library is a local companion resource and is not distributed with this repository; the literature IDs and paths in reference tags serve traceability and retrieval.

## Editorial Standard

All volumes follow [`../tools/STYLE_GUIDE.md`](../tools/STYLE_GUIDE.md): objective third-person style; no conversational wording, first/second person, internal process records, colloquial or subjective expressions; design choices are recorded as design decisions; unvalidated items are not used as design baselines. The complete terminology table is in Section 6 of the style guide; a compact bilingual list is in [`GLOSSARY.md`](GLOSSARY.md).

## Archive

The original Chinese drafts are retained in [`../archive/original-zh/`](../archive/original-zh/) for traceability only and are not part of the current reports.
