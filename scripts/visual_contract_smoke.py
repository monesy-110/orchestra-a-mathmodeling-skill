from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "assets" / "shared-scripts"))

from drawio_check import check_flow  # noqa: E402
from figure_check import check_figure_script  # noqa: E402


def main() -> int:
    rounded = '<mxCell id="n1" value="step" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1"><mxGeometry x="0" y="0" width="100" height="40" as="geometry"/></mxCell>'
    straight = rounded.replace("rounded=1", "rounded=0")
    rounded_issues = check_flow(rounded, "rounded.drawio")
    straight_issues = check_flow(straight, "straight.drawio")
    assert any("矩形节点使用 rounded=1" in item for item in rounded_issues), rounded_issues
    assert not any("矩形节点使用 rounded=1" in item for item in straight_issues), straight_issues

    temp = ROOT.parent / "runtime_visual_contract_smoke.py"
    temp.write_text(
        "from 工具.plot_utils import setup_style, save_fig\n"
        "setup_style()\n"
        "fig, ax = plt.subplots()\n"
        "ax.plot([0, 1], [0, 1])\n"
        "ax.spines['top'].set_visible(False)\n"
        "ax.spines['right'].set_visible(False)\n"
        "fig.tight_layout()\n"
        "save_fig(fig, '图表/test.pdf')\n",
        encoding="utf-8",
    )
    issues = check_figure_script(str(temp))
    if temp.exists():
        temp.unlink()
    assert not any("视觉质量偏低" in item or "缺少渐变" in item for item in issues), issues

    # nature-figure 引擎双轨门禁：rcParams 初始化脚本在 gate 侧通过（setup_style 不再强制）
    nf_style = (
        "import matplotlib as mpl\n"
        "mpl.rcParams.update({'font.family': 'sans-serif', 'pdf.fonttype': 42})\n"
        "fig, ax = plt.subplots()\n"
        "ax.plot([0, 1], [0, 1])\n"
    )
    assert ("setup_style" in nf_style) or ("rcParams.update" in nf_style) or ("rcParams[" in nf_style), "nature-figure style init not recognized"
    legacy_style = "from 工具.plot_utils import setup_style\nsetup_style()\nfig, ax = plt.subplots()\n"
    assert ("setup_style" in legacy_style) or ("rcParams.update" in legacy_style) or ("rcParams[" in legacy_style), "legacy style init not recognized"
    bad_style = "import matplotlib.pyplot as plt\nfig, ax = plt.subplots()\n"
    assert not (("setup_style" in bad_style) or ("rcParams.update" in bad_style) or ("rcParams[" in bad_style)), "unstyled script should fail gate"

    print("visual contracts passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
