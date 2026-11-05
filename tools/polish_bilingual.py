# -*- coding: utf-8 -*-
"""双语终稿后处理：统一方案编号、清除过程性注释与口语引导句、修正标点。

对 zh-CN/ 与 en-US/ 下的 12 册设计报告执行同一套语义等价的改写，
保证两版在编号、术语与语气上一致。可重复运行。
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / "zh-CN"
EN = ROOT / "en-US"

ZH_RULES: list[tuple[str, str]] = [
    # 方案编号：旧的罗马数字路线号统一为 A/B/C
    (r"I \+ II/III 混合", "A + B/C 混合"),
    (r"I \+ II 混合", "A + B 混合"),
    (r"I \+ III 混合", "A + C 混合"),
    (r"I\+II 混合", "A+B 混合"),
    (r"I\+III 混合", "A+C 混合"),
    (r"II 为主 \+ I 留作 P2", "方案 B 为主 + 方案 A 留作 P2"),
    (r"II 降风险", "方案 B 降风险"),
    (r"III DNA 门底层约束", "方案 C：DNA 门约束"),
    (r"C\. 方案 B/III 为主", "C. 方案 B/C 为主"),
    (r"C\. III 为主", "C. 方案 C 为主"),
    (r"I 为主 \+ 协同备用", "方案 A 为主 + 协同备用"),
    (r"方案 A/II 组合", "方案 A/B 组合"),
    (r"\[路线III\]", "[方案 C]"),
    (r"II 为主 \+ I 验证", "方案 B 为主 + 方案 A 验证"),
    (r"II 为主", "方案 B 为主"),
    (r"III 为主", "方案 C 为主"),
    # 主观绝对化措辞
    (r"世界范围最佳实践", "公开研究实践"),
    (r"领域最佳实践", "领域公开实践"),
    (r"分阶段最佳实践", "分阶段公开实践"),
    (r"最佳实践", "公开研究实践"),
    (r"哪条选项是天花板", "对应方案"),
    # 内部过程记录
    (r"\*\*命名消歧\([^)\n]*交叉引用一致性复核\)\*\*", "**命名约定**"),
    (r"\(2026-09-16 一致性复核收敛", "（2026-09-16 结论"),
    (r"一致性复核", "一致性检查"),
    # 口语引导句
    (r"回答[「\"]如何设计[」\"]:", "设计问题："),
    (r"回答四个比[「\"]本能[」\"]更底层的问题[，,]并把它落成", "本节处理四个比「本能」更底层的问题，并将其转化为"),
    (r"怎么摆/怎么造/怎么读", "布局/制造/读取"),
    (r"怎么取/怎么转/怎么分", "获取/转化/分配"),
    (r"[「\"]作用接口怎么映射[」\"]", "「作用接口的映射方式」"),
    (r"C4 因果独立性怎么定", "C4 因果独立性的判据形式"),
    (r"适应度裁判怎么[「\"]可测量、可运行[」\"]", "适应度裁判实现可测量、可运行的方式"),
    (r"5 回路怎么[「\"]先证哪部分、后证哪部分[」\"]", "五回路的分阶段验证顺序"),
    (r"I0a 反射 / I0b CPG 在硅基凝胶里怎么实现", "I0a 反射 / I0b CPG 在硅基凝胶中的实现方式"),
    (r"布尔门用什么物理实现", "布尔门的物理实现方式"),
    (r"代际经验怎么传递", "代际经验的传递方式"),
    (r"世界模型的潜变量落在哪", "世界模型潜变量的载体"),
    (r"突触基质 \+ 长程联结用什么物理实现[，,]以及[「\"]学习[」\"]落哪一层", "突触基质与长程联结的物理实现，以及学习所在层次"),
    (r"落成\*\*可裁判的规则\*\*", "转化为**可裁判的规则**"),
    (r"现在就能判[「\"]个体[」\"]", "可直接判定个体性"),
    (r"最贴合", "符合"),
]

EN_RULES: list[tuple[str, str]] = [
    # 方案编号
    (r"I \+ II/III hybrid", "A + B/C hybrid"),
    (r"I \+ II hybrid", "A + B hybrid"),
    (r"I \+ III hybrid", "A + C hybrid"),
    (r"II-primary \+ I-verification", "B-primary + A-verification"),
    (r"II-primary \+ I verification", "B-primary + A verification"),
    (r"I-dominant \+ cooperative backup", "A-dominant + cooperative backup"),
    (r"II primary \+ I retained as P2", "B primary + A retained as P2"),
    (r"II primary", "B primary"),
    (r"III DNA gate", "Option C DNA gate"),
    # 术语一致性
    (r"[Ww]orld-[Ww]ide [Bb]est [Pp]ractice", "Published Research Practice"),
    (r"world-wide best practice", "published research practice"),
    (r"World Best Practice", "Published Research Practice"),
    (r"world best practice", "published research practice"),
    (r"Domain best practice", "Published practice"),
    (r"domain best practice", "published practice"),
    (r"best practice", "published practice"),
    (r"concept option", "conceptual option"),
    (r"Concept option", "Conceptual option"),
    # 内部过程记录
    (r"Naming disambiguation \([^)\n]*consistency review\)", "Naming convention"),
    (r"\(converged in the [^)\n]*consistency review\)", ""),
    (r"\(marked in the consistency review\)", ""),
    (r"\(\d{4}-\d{2}-\d{2} cross-reference consistency review\)", ""),
    (r"Key assumption boundary \(marked[^)\n]*\)", "Key assumption boundary"),
    (r"DOIs verified item by item[^)\n]*", "DOIs checked against the source records"),
    # 口语引导句与标点
    (r"Answering [\"“]how to design[\"”]:", "Design question:"),
    (r"\*\*This section presents the comparison of design options\.\*\*\.", "**This section presents the comparison of design options.**"),
    (r"not mutually exclusive\., and", "not mutually exclusive, and"),
    (r"options\.\*\*\.", "options.**"),
    (r"\.\*\*\.", ".**"),
    (r"\.,", "."),
]


def apply(text: str, rules: list[tuple[str, str]]) -> tuple[str, int]:
    total = 0
    for pat, rep in rules:
        text, n = re.subn(pat, rep, text)
        total += n
    return text, total


# 终稿精修：整行改写与括号注释中性化（限定单行，避免跨段落匹配）
ZH_RULES += [
    (r"落成", "转化为"),
    (r"本节把", "本节将"),
    (r"不等式 \+ 参数窗口", "不等式与参数窗口"),
    (r"\*\*升级说明\*\*", "**公理表述**"),
    (r"\*\*量纲说明\([^)\n]*\)\*\*", "**量纲说明**"),
    (r"\*\*可证伪化前置\([^)\n]*\)\*\*", "**可证伪化前置**"),
    (r"\*\*命名消歧\([^)\n]*\)\*\*", "**命名约定**"),
    (r"(?m)^> 原 v2/v3 只画了个.*$", "> 本节将**方案 B 复制**转化为 5 步可执行流程。"),
    (r"(?m)^> 原 v2/v3 说.*$", "> 本节给出**读取机制**，对应「可寻址 + 上下文选择性表达」。"),
    (r"(?m)^> 原 §6 是张表.*$", "> 本节将各区域映射到复制与变异机制。"),
    (r"(?m)^> \*\*待验证 · 误标修正.*$", ""),
    (r"一致性检查", "一致性核验"),
]

EN_RULES += [
    (r"\bclearly\s+", ""),
    (r"\*\*Upgrade note\*\*", "**Axiom formulation**"),
    (r"the original \"ordered state\" is upgraded to", "the criterion is expressed as"),
    (r"\(marked in the consistency review, explicitly retained\)", ""),
    (r"\(marked in the consistency review, to be settled by design review\)", "(to be confirmed by design review)"),
    (r"\*\*Regional semantic convergence \([^)\n]*\)\*\*", "**Regional semantics**"),
    (r"\*\*T0 synchronisation note \([^)\n]*\)\*\*", "**Design decision (T0)**"),
    (r"\*\*Dimensional note[^*]*\*\*", "**Dimensional note**"),
    (r"\(marked \"to be checked\" on [^)\n]*\)", ""),
    (r"DOIs verified item by item[^)\n]*", "DOIs checked against the source records"),
    (r"\bconsistency review\b", "consistency check"),
    (r"\bConsistency review\b", "Consistency check"),
    (r"(?m)^> The original v2/v3 only drew.*$", "> This section converts **Option B replication** into a five-step executable flow."),
    (r"(?m)^> The original v2/v3 stated.*$", "> This section specifies the **readout mechanism** for addressability and context-dependent selective expression."),
    (r"(?m)^> The original §6 was a table.*$", "> This section maps the regions onto the replication and mutation mechanisms."),
    (r"(?m)^> \*\*To be verified · mislabeling correction.*$", ""),
]


# 变量名中的中文字符统一为拉丁记号，保证两版公式一致
ZH_RULES.append((r"t_压", "t_sup"))
EN_RULES.append((r"t_压", "t_sup"))


def main() -> None:
    for folder, rules, label in ((ZH, ZH_RULES, "zh-CN"), (EN, EN_RULES, "en-US")):
        for path in sorted(folder.glob("[0-9][0-9]_*.md")) + sorted(folder.glob("[0-9][0-9]-*.md")):
            original = path.read_text(encoding="utf-8")
            updated, n = apply(original, rules)
            if updated != original:
                path.write_text(updated, encoding="utf-8")
            print(f"[{label}] {path.name}: {n} replacements")
    print("\nPost-processing complete.")


if __name__ == "__main__":
    main()
