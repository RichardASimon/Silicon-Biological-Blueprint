# 硅基 DNA 设计 · 参考文献

> **状态标注**：
> - 📁 本地已有，**已核对真实内容**（`Reference Documentation/` 下两个分类文件夹）
> - ⚠️ 卡在付费墙 / 需手动补全
> - 🔗 数据库/在线入口
>
> 两个分类文件夹：
> - `Reference Documentation/DNA Reference/` — DNA / 硅基信息层
> - `Reference Documentation/Neuroscience & Neural Networks/` — 神经 / 学习 / DNA 神经网络
>
> 文件真实内容已逐篇用 pdftotext 抽检确认。

---

## A. 奠基性里程碑（碳基 DNA 结构与密码破译）

| 文献 | 来源 | 状态 | 核心价值 |
|------|------|------|---------|
| Watson & Crick (1953). *Molecular structure of nucleic acids: A structure for deoxyribonucleic acid.* Nature 171: 737–738 | Nature | 📁 `DNA Reference/MOLECULAR_STRUCTURE_OF_NUCLEIC_ACIDS_A_S.pdf` | 双螺旋 + 互补配对（A-T, C-G），暗示自我复制机制 |
| Crick (1970). *Central dogma of molecular biology.* Nature 227: 561–563 | Nature | 📁 `DNA Reference/Crick_Central_Dogma_1970_Nature227.pdf`（免费 Caltech 镜像；Nature.org 付费） | 中心法则：信息流不可逆（DNA→RNA→蛋白质） |
| Nirenberg, Leder, et al. (1965). *RNA codewords and protein synthesis, VII.* PNAS 53(5): 1161–1168 | PNAS | 📁 `DNA Reference/nirenberg-et-al-1965...pdf` | 64 个三联体密码子与氨基酸的完整破译 |

---

## B. 教科书（系统性原理）

> 你本地原有两个"教科书 .txt" 经核实**只是 Google Books 书签（无正文）**，已删除。整本书需另行获取。

| 文献 | 状态 | 备注 |
|------|------|------|
| Alberts, B., et al. *Molecular Biology of the Cell* (Garland Science) | ⚠️ 需手动补全 | 可走 NCBI Bookshelf 免费章节 |
| Krebs, Goldstein, Kilpatrick. *Lewin's GENES* (Jones & Bartlett) | ⚠️ 需手动补全 | Google Books / 出版商 |

**用途**：DNA 复制/转录/翻译全链路；基因表达调控；染色质结构。

---

## C. 现代前沿综述（代码的拓展与演变）

| 文献 | 状态 | 方向 |
|------|------|------|
| *The Central Dogma Decentralized: New Perspectives on RNA Function and Local Translation in Neurons* | 📁 `Neuroscience & Neural Networks/The Central Dogma Decentralized....pdf` | 中心法则的拓展与神经局部翻译 |
| Robinson, Zhang, et al. (2026). *Construction of complex and diverse DNA sequences using DNA three-way junctions (Sidewinder).* **Nature 651: 491**, doi:10.1038/s41586-025-10006-0 | 📁 `DNA Reference/Sidewinder_2026_DNA_Three-Way_Junction_Assembly_Nature.pdf` | **DNA 三叉点(3WJ)组装：把"指导组装的信息"与"最终序列"分离开**——直接命中设计原则 P1（信息层与基底分离） |

> 原 `s41586-025-10006-0.pdf` 已按内容重命名为 `Sidewinder_2026...pdf`。

---

## D. 官方权威数据库（Fact Sheets / 实时数据）

| 资源 | 链接 | 用途 |
|------|------|------|
| NHGRI DNA Fact Sheet | [genome.gov](https://www.genome.gov/about-genomics/fact-sheets/Deoxyribonucleic-Acid-Fact-Sheet) | 人类基因组（~30 亿 bp、~2 万基因）权威数据 |
| Britannica: DNA | [britannica.com/science/DNA](https://www.britannica.com/science/DNA) | 磷酸二酯键、氢键、复制机制的准确定义 |
| ASBMB: Discoveries made possible by DNA | [asbmb.org](https://www.asbmb.org/asbmb-today/science/112425/discoveries-made-possible-by-dna) | 综述 |

---

## E. DNA 数据存储 / 信息层（生物 × 计算机）

| 文献 | 状态 | 硅基映射 |
|------|------|---------|
| **Erlich & Zielinski (2017)**. *Massive Data Storage in DNA by Dense Error-Correcting Coding.* Science. doi:10.1126/science.aaj2038 | 📁 `DNA Reference/Erlich-Zielinski_2017_DNA_Fountain_Science_fulltext.pdf`（bioRxiv 预印本，CC-BY-NC，全文可用） | **DNA Fountain**：fountain 码冗余——任意大子集可重建全消息 = P2 稳定性设计 |
| **Sun, Hong/Song 组 (2026)**. *Long-stranded XNA-cssDNA hybrids for robust data storage.* **Science Advances**, doi:10.1126/sciadv.aed2917 | 📁 `DNA Reference/Sun_2026_XNA_cssDNA_data_storage_SciAdv_FULLTEXT.txt`（正文已清洗 HTML） | **XNA-cssDNA 杂交**：把信息层与天然 DNA 处理机制解耦 + 抗丢失鲁棒——XNA 方向的代表（注意：**并非 "Liu 组"，Liu 名下无此论文，已核实**） |
| **Gudodagi, et al. (2022)**. *Design and development of learning model for compression and processing of DNA genome sequence.* IJECE 12(2) | 📁 `DNA Reference/Gudodagi_2022_DNA_Genome_Sequence_Compression_IJECE.pdf` | 把 DNA 序列当数据做压缩/编码（信息层方向） |

> 原"Microsoft/Harvard DNA 存储" 已并入 Erlich 2017（同属 DNA 存储 + ECC）。

---

## F. 人工合成生命与扩展遗传码（合成生物学）

| 文献 | 状态 | 硅基映射 |
|------|------|---------|
| **Kutney, et al. (2016)**. *A cell freed from its genome: the stripped-bare cell.* PMC | 📁 `DNA Reference/Kutney_2016_JCVI-syn3.0_Synthetic_Genome_Stripped_Bare_Cell_PMC.pdf` | JCVI-syn3.0 最小基因组：鲁棒性 = 冗余 + 模块化 + 潜在松弛（P4 保真度窗口参照） |
| **Hutchison, …, Venter (2016)**. *Designing a bacterial genome of 531,000 base pairs and implementing it in a 10,800-base synthetic genome.* **Science**, doi:10.1126/science.aad6253 | 📁 `DNA Reference/Hutchison_2016_JCVI_syn3.0_minimal_bacterial_genome_Science.pdf` | syn3.0 原始设计（与上篇互补） |
| **Young, …, Schultz (2010)**. *Expanding the genetic lexicon.* JBC (Scripps) | 📁 `DNA Reference/Young-Schultz_2010_Expanding_Genetic_Lexicon_JBC_Scripps.pdf` | 往字母表加新符号（正交性，P4 机制） |
| **Xiao, …, Schultz (2015)**. *Expanded genetic code.* PNAS, doi:10.1073/pnas.1507741112 | 📁 `DNA Reference/Schultz_2015_PNAS_expanded_genetic_code_FULLTEXT.txt`（OA PNAS 全文） | 扩展氨基酸 / 新碱基对（P4 正交性） |

> 原"6 碱基半合成生命（Scripps）"即 Schultz 组扩展遗传密码，已并入上两篇。

---

## G. 硅基信息存储 / 分子计算（跨领域）

| 文献 | 状态 | 硅基映射 |
|------|------|---------|
| **Adleman (1994)**. *Molecular Computation of Logical Solutions.* Science 266: 1022–1023, doi:10.1126/science.7973651 | 📁 `DNA Reference/Adleman_1994_Science_molecular_computation_scanned.pdf`（扫描件，纯图；Science.org 付费，此为唯一可获取来源，引用需人工翻图） | 数据并行、指数体积——分子计算开山之作 |
| **Becker & Becher (2017)**. *Coherence properties and quantum control of silicon vacancy color centers in diamond.* arXiv:1709.10321 | 📁 `DNA Reference/Becker-Becher_2017_SiV_Spin_Qubit_Silicon_Vacancy_Color_Center_arXiv1709.pdf` | 硅空位色心（SiV）quantum control（**注意：SiV 在金刚石中，非硅衬底**） |
| **Sohn & Choi (2018)**. *Quantum coherence properties of SiV spin qubits in diamond.* Nat. Commun., doi:10.1038/s41467-018-04340-3 | 📁 `DNA Reference/Sohn_2018_SiV_spin_qubit_coherence_NatComms_FULLTEXT.txt`（OA 全文） | 终点态光学表征；spin 退极化 → 第一代不用（§6.1） |
| **Holmes, …, Morello (2023)**. *Improved placement precision of implanted donor spin qubits in silicon using molecule ions.* arXiv:2308.04117 | 📁 `DNA Reference/Holmes-2023_Improved_Placement_Precision_Implanted_Donor_Spin_Qubits_arXiv.pdf` | **确定性单原子放置精度**（唯一可放单掺杂原子的工艺，§6 物理承载层）——原"IBM IBAD"实为 UNSW/Morello 组 STM 单原子路线 |
| **Schofield, et al. (2025)**. *Roadmap on Atomic-scale Semiconductor Devices.* (多机构，含 IBM/UNSW/UC/NIST) | 📁 `DNA Reference/Schofield_2025_Atomically_Precise_Manufacturing_Silicon_Roadmap_arXiv2501.pdf` | **硅基原子级制造路线图**——"确定性单原子放置 + 封装"的权威替代（补上"IBM IBAD"未解决项），覆盖 IBM FIB / UNSW STM / 单原子晶体管 |
| **Milenkovic, et al. (2023)**. *DNA-based data storage systems: a review of implementations and code constructions.* arXiv:2310 | 📁 `DNA Reference/Milenkovic_2023_DNA_Data_Storage_Systems_Review_arXiv2310.pdf` | DNA 存储 + 编码构造综述（§6 冗余 / ECC 设计的系统参照） |
| Memristive crossbar | ⚠️ 需手动检索 | 状态与操作共址 |
| Landauer 极限 / DFT（VASP/QE/Wien2k） | 🔗 已确立工具 | §8 理论计算 |

> **注**：原"IBM IBAD 单磷原子放置"经检索**并非一篇可定位的 IBM 论文**——单原子晶体管/放置的公开工作属于 **UNSW（Simmons/Morello 组，STM 路线）** 与 IBM 的单原子数据存储（holmium 2017）。已用 `Holmes-2023`（arXiv）作为"确定性单原子放置"的权威代表。

---

## H. 神经 / 学习 / DNA 神经网络

| 文献 | 状态 | 价值 |
|------|------|------|
| **Qian, Winfree, Bruck (2011)**. *Neural network computation with DNA strand displacement cascades.* **Nature 475: 373–377**, doi:10.1038/nature10262 | 📁 `Neuroscience & Neural Networks/Qianlab_2011_DNA_Seeseesaw_Neural_Networks.pdf` | **DNA 分子计算做神经网络**（经典）——直接对应硅基 DNA 的"可执行 + 可学习" |
| **te Vrugt (2024)**. *Neural networks consisting of DNA.* arXiv:2501.03235 | 📁 `Neuroscience & Neural Networks/teVrugt_2024_DNA_Neural_Networks_arXiv2501.pdf` | DNA 神经网络入门（DNA 天然信息存储 → 软物质神经网） |
| **Steward & Schuman (2001)**. *Protein synthesis at synaptic sites on dendrites.* Annu. Rev. Neurosci. 24: 299–325 | 📁 `Neuroscience & Neural Networks/Stout_2001_Protein_Synthesis_Synaptic_Sites_Dendrites_Caltech.pdf` | 突触局部蛋白合成——"按图施工"（§5.1 路线 B）的生物参照 |
| **Lansner, Fiebig, Herman (2023)**. *Fast Hebbian plasticity and working memory.* arXiv | 📁 `Neuroscience & Neural Networks/Hebbian_2023_Fast_Hebbian_Platicity_Working_Memory_arXiv.pdf` | Hebbian 可塑性机制（"本能 + 学习"如何内建，P5 参照） |
| **Kriegeskorte & Wei (2021)**. *Neural tuning and representational geometry.* arXiv:2104.09743 | 📁 `Neuroscience & Neural Networks/Kriegeskorte_2021_Neural_Tuning_Representational_Geometry_arXiv2104.pdf` | 神经编码 / 表征几何（信息论视角，P5"学习"机制参照） |
| **Morales, di Santo, Muñoz (2023)**. *Unveiling the intrinsic dynamics of biological and artificial neural networks: from criticality to optimal representations.* arXiv:2307.10669 | 📁 `DNA Reference/Morales_2023_Neural_Dynamics_Criticality_Optimal_Representations_arXiv2307.pdf` | 生物/人工神经网动力学 + 临界性（"本能 + 学习"涌现的理论基础） |
| **Khacef, et al. (2022)**. *Spike-based local synaptic plasticity: a survey of computational models and neuromorphic circuits.* arXiv:2209.15536 | 📁 `Neuroscience & Neural Networks/Khacef_2022_Spike_Local_Synaptic_Plasticity_Neuromorphic_Survey_arXiv2209.pdf` | 本地方应可塑性综述（P5 本能"写死 vs 涌现"机制参照） |
| **BlumMoyse & Berry (2024)**. *A coupled neural field model for the standard consolidation theory.* arXiv:2404 | 📁 `Neuroscience & Neural Networks/BlumMoyse_2024_Coupled_Neural_Field_Memory_Consolidation_arXiv2404.pdf` | 记忆巩固神经场模型（P5"学习能力"内建机制） |
| **Nwadiugwu (2021)**. *Neural Networks, Artificial Intelligence and the Computational Brain.* | 📁 `Neuroscience & Neural Networks/Nwadiugwu_2021_Neural_Networks_AI_Computational_Brain_Review_arXiv.pdf` | 生物神经 vs ANN 对照综述 |

---

## 检索建议（需手动补全的 ⚠️ 项）

本环境 WebSearch/WebFetch 抓取不可靠，以下条目需你手动去数据库检索并下载到 `Reference Documentation/` 对应分类文件夹：

**优先级 1**：
1. **Erlich 2017 补充材料**（main text 卡在 Science.org 付费墙；正文 bioRxiv 预印本已在手，`DNA Reference/Erlich-Zielinski_2017_DNA_Fountain_Science_fulltext.pdf`）——手动下载 supplementary 更全
2. **两本教科书整本**（Alberts *MBoC*、Lewin's GENES）——NCBI Bookshelf / Google Books

**优先级 2**：
3. Memristive crossbar（`memristor crossbar molecular memory`）

**数据库入口**：PubMed / PMC（免费全文）· Google Scholar · DOI.org · NCBI Bookshelf

**关键作者/团队**：Erlich & Zielinski（DNA Fountain）· Venter/JCVI（syn3.0）· Schultz/Young（扩展遗传密码）· Sun 组（XNA 存储）· Adleman（分子计算）· UNSW Morello/Simmons（单原子放置）· Qian/Winfree/Bruck（DNA 神经网）

---

## 待你决策的开放项（§5 / §6 / §9 文档里留的）
1. **复制由谁驱动？**（自发 vs 外部能量场）——§5.1
2. **保真度/变异率窗口**——§6.2
3. **本能方案**：写死 vs 涌现 vs 混合（§5.2 推荐混合）
4. **候选载体定哪一个**（建议 SiO₂ 宿主 + 离子束掺杂 + ALD 封装，§9.1）

---

*更新：2026-09-13 · 配套主文档 `硅基DNA设计调研报告.md` · 文件已按两分类归档并逐篇核对*
