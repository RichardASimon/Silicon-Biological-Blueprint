# -*- coding: utf-8 -*-
"""双语设计报告验收工具

检查中文组与英文组的逐册对应关系、章节编号、表格规模、
引用标记、语言纯度与不合规表述残留，并输出可执行的修复清单。
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ZH = ROOT / "zh-CN"
EN = ROOT / "en-US"

VOLUMES: list[tuple[str, str, str]] = [
    ("00", "00_哲学层_设计.md", "00-Philosophical-Foundations.md"),
    ("01", "01_DNA信息层_设计.md", "01-DNA-Information-Layer.md"),
    ("02", "02_硅基材料工艺_设计.md", "02-Silicon-Materials-and-Process.md"),
    ("03", "03_能量代谢_设计.md", "03-Energy-Metabolism.md"),
    ("04", "04_边界个体性_设计.md", "04-Boundary-and-Individuality.md"),
    ("05", "05_神经网络_设计.md", "05-Neural-Network.md"),
    ("06", "06_世界模型_设计.md", "06-World-Model.md"),
    ("07", "07_记忆系统_设计.md", "07-Memory-System.md"),
    ("08", "08_逻辑推理_设计.md", "08-Logical-Reasoning.md"),
    ("09", "09_本能行为_设计.md", "09-Instinctive-Behavior.md"),
    ("10", "10_演化选择_设计.md", "10-Evolutionary-Selection.md"),
    ("11", "11_系统整合_设计.md", "11-System-Integration.md"),
]

CJK = re.compile(r"[\u4e00-\u9fff]")
CODE_SPAN = re.compile(r"`[^`]*`")
REF_TAG = re.compile(r"\[Ref:[^\]]*\]")
H2 = re.compile(r"^##\s+(\d+)\.")
BAD_ZH = re.compile(
    r"你|我定|我漏|我拍|拍板|拍脑袋|写死|兜底|气势|适合谁|待你|由你|用户|agent|"
    r"⚠|✅|📌|🌐|📎|推荐|默认|冷读者|甩标签|套硅基|清一色|跑不起来|"
    r"承重|诚实边界|待实测|待 DFT|生成:|生成：|本仓库|本地配套|gitignore|"
    r"核实记录见|魔数|sidecar|检索推荐|见原文|基于你的|你作为|不假装|待补抓|反爬|"
    r"最佳实践|命名消歧|回答[「\"]如何设计|落成|最贴合"
)
BAD_EN = re.compile(
    r"\b(?:we|you|your|our|my|me|us|recommend|recommended|obviously|honestly|"
    r"clearly|surely|TODO|TBD|maybe|probably|sorry|please note|best practice|"
    r"naming disambiguation|should be noted)\b|[⚠✅📌🌐📎💡🚧]|Answering\s+[\"“]how to design"
)
PUNCT = re.compile(r"\.,|\.\*\*\.|\s+,")


def strip_spans(line: str) -> str:
    return REF_TAG.sub("", CODE_SPAN.sub("", line))


def check_volume(num: str, zh_name: str, en_name: str) -> list[str]:
    issues: list[str] = []
    zp, ep = ZH / zh_name, EN / en_name
    if not zp.exists():
        return [f"missing Chinese volume: {zh_name}"]
    if not ep.exists():
        return [f"missing English volume: {en_name}"]
    try:
        zt, et = zp.read_text(encoding="utf-8"), ep.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return [f"encoding error in {en_name}: {exc}"]

    zl, el = zt.splitlines(), et.splitlines()
    zh2 = [m.group(1) for ln in zl if (m := H2.match(ln))]
    en2 = [m.group(1) for ln in el if (m := H2.match(ln))]
    if zh2 != en2:
        issues.append(f"section numbers differ: zh={zh2} en={en2}")
    if len(el) < len(zl) * 0.6:
        issues.append(f"English file much shorter ({len(el)} vs {len(zl)} lines) — possible summary instead of full translation")

    zt_rows = sum(1 for ln in zl if ln.lstrip().startswith("|"))
    et_rows = sum(1 for ln in el if ln.lstrip().startswith("|"))
    if abs(zt_rows - et_rows) > max(2, zt_rows * 0.05):
        issues.append(f"table row count differs: zh={zt_rows} en={et_rows}")

    zref = len(re.findall(r"\[引用[:：]", zt))
    eref = len(re.findall(r"\[Ref:", et))
    if abs(zref - eref) > max(3, zref * 0.1):
        issues.append(f"reference tag count differs: zh={zref} en={eref}")

    for i, ln in enumerate(zl, 1):
        if BAD_ZH.search(ln):
            issues.append(f"zh L{i} residual wording: {ln[:100]}")
    for i, ln in enumerate(el, 1):
        stripped = strip_spans(ln)
        if CJK.search(stripped) and "Corresponding Chinese edition" not in ln:
            issues.append(f"en L{i} unexpected Chinese: {ln[:100]}")
        if BAD_EN.search(stripped):
            issues.append(f"en L{i} non-report wording: {ln[:100]}")
        if PUNCT.search(ln):
            issues.append(f"en L{i} punctuation: {ln[:100]}")
    if "Corresponding Chinese edition" not in et:
        issues.append("missing cross-reference footer")
    return issues


def main() -> int:
    total = 0
    for num, zh_name, en_name in VOLUMES:
        issues = check_volume(num, zh_name, en_name)
        total += len(issues)
        status = "OK" if not issues else f"{len(issues)} issue(s)"
        print(f"[{num}] {en_name}: {status}")
        for issue in issues[:12]:
            print("    - " + issue)
        if len(issues) > 12:
            print(f"    ... {len(issues) - 12} more")
    print(f"\nTotal issues: {total}")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
