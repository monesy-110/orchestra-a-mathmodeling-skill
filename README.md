<p align="center">
  <img src="assets/branding/logo.svg" alt="Orchestra" width="460">
</p>

<p align="center"><em>Seven movements, one performance — orchestration for evidence-driven mathematical modeling.</em></p>

<p align="center">
  <img alt="Version" src="https://img.shields.io/badge/version-v1.2-C9A24B?labelColor=0B0F17&style=flat-square">
  <img alt="Core" src="https://img.shields.io/badge/Python-3.8%2B-3E6B8C?labelColor=0B0F17&style=flat-square">
  <img alt="PDF" src="https://img.shields.io/badge/LaTeX-XeLaTeX-A06A28?labelColor=0B0F17&style=flat-square">
  <img alt="Targets" src="https://img.shields.io/badge/Targets-CUMCM%20%7C%2051MCM%20%7C%20MCM%2FICM-4B5E7E?labelColor=0B0F17&style=flat-square">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-9A7424?labelColor=0B0F17&style=flat-square">
</p>

---

## Orchestra

数学建模研究既是科学，也是艺术。单项技术可以耀眼，但只有**编排**才能让问题理解、模型构造、真实计算、证据表达与论文交付彼此咬合，像一支乐团一样服务于同一场演出。

Orchestra 就是为这场演出设计的工程化系统：它把一次数学建模竞赛任务组织为可执行、可恢复、可审计的七阶段工作流，让每一步产出都能在上游找到证据，让最终论文的每个数字都能被他自己的程序复现。

项目优先面向 Codex 等 Skill 环境使用，兼容能够读取 Markdown 指令、访问工作区并执行本地命令的其他 AI 工具。Orchestra 只提供研究辅助——题意、数据、模型、程序、结果与最终材料必须由使用者核验。

---

## 总谱：音乐隐喻与工作流实体

一次竞赛，就是一场演出。Orchestra 的每个部件在乐团里都有它的位置：

| 音乐概念 | Orchestra 中的对应 | 落点 |
| --- | --- | --- |
| 总谱（Score） | 工作流清单与运行状态，定义"这一段谁进、何时进" | `assets/workflow_manifest.json` · `状态/工作流状态.json` |
| 指挥（Conductor） | 主控角色，编排阶段、执行门禁、推进核验点 | `scripts/stage_executor.py` · `scripts/pipeline_manager.py` |
| 声部（Sections） | 工作角色与复核角色，各司一职又彼此倾听 | `references/subagent-architecture.md` |
| 排练（Rehearsal） | 基线冒烟与回归门禁，确保乐段每个音符稳定 | `scripts/baseline_smoke.py` 等回归脚本 |
| 休止符（Rest） | 核验点 `checkpoint` —— 停顿、核对、再继续 | `stage_executor.py checkpoint` |
| 变奏（Variations） | 增强返工 `enhancement`：主题不变，表现手法演进 | `scripts/enhancement_audit.py` |
| 彩排（Dress Rehearsal） | 冠军模式多轮独立审稿，正式场合前的最后打磨 | `scripts/championship_review.py` |
| 安可（Encore） | 可选重跑与稳健性扩展，让主题多一个版本收尾 | 复现性检查与稳健性分析 |

---

## 奏鸣曲式：七乐章

七个乐章按古典奏鸣曲式组织：**呈示部**确立主题，**展开部**让主题发展、转调、对峙，**再现部**让主题回归，**终曲**收束全篇。乐章的先后由证据依赖决定——论文的完整性建立在证据的完整性之上。

| 乐章 | 奏鸣曲式 | 阶段 | 乐句的任务 |
| --- | --- | --- | --- |
| 序奏 | 调音与定调 | 工作区初始化 | 乐器就位、调性设定：竞赛类型、格式、模板基线 |
| 壹 | 呈示部·主部主题 | `DISCOVERY` | 题目到底在问什么？数据以何种模式存在？ |
| 贰 | 呈示部·副部主题 | `FORMULATION` | 用什么数学机制刻画它？模型身份与算法如何分离？ |
| 叁 | 展开部 | `COMPUTATION` | 主题在真实计算中发展：算出来了吗？验证了吗？ |
| 肆 | 展开部·变奏 | `EVIDENCE` | 结果如何变奏为可发表的图形、表格与证据链？ |
| 伍 | 展开部·对位 | `SCHEMATICS` | 对位声部行进：路线与系统逻辑如何被清晰表达？ |
| 陆 | 再现部 | `MANUSCRIPT` | 主题回归：以目标竞赛规范组织成完整文稿 |
| 柒 | 终曲（Coda） | `ASSURANCE` | 收束与和声解决：能编译、合规、可提交吗？ |

---

## 理念

**指挥的信念：证据优先。** 公式、数值、图表和结论都能追溯到题面、模型、程序或结果文件。上游证据存在根本问题时，系统把阶段回退修复，而不是用文字润色掩盖缺陷。

**三个档位，三种演出状态。** `baseline` 是排练——保持阶段与门禁稳定，保证流程可靠运行；`enhancement` 是变奏——针对薄弱项实施受控返工；`championship` 是彩排——在验收前执行多轮独立审稿与全文修订。

---

## 配器法：技术栈（九个声部组）

| 声部组 | 技术 | 用途 |
| --- | --- | --- |
| 弦乐群 · 核心运行时 | Python 3.8+（推荐 3.10 / 3.11） | 初始化、阶段状态机、门禁、审稿与回归脚本 |
| 木管组 · 科学计算 | NumPy · Pandas · SciPy · scikit-learn · statsmodels · NetworkX | 数据处理、预测、评价、优化、统计分析与图论 |
| 竖琴 · 数据读取 | openpyxl · xlrd | `.xlsx` / `.xls` 赛题附件 |
| 铜管组 · 证据可视化 | Matplotlib · Seaborn · SciencePlots · adjustText | 数据图、诊断图、标签避让与论文图形 |
| 定音鼓 · PDF 路线 | XeLaTeX · BibTeX · TikZ · ctex | LaTeX 编译、结构图与提交质量检查 |
| 双簧管 · DOCX 路线 | python-docx · Pillow · pypdf · LibreOffice | Word 导出、图片尺寸与页数门禁 |
| 打击乐 · 系统制图 | DrawIO Desktop CLI / TikZ | `.drawio` 或 TikZ 技术路线图 |
| 乐务 · 视觉核验 | Poppler (`pdftoppm`) | PDF 图形渲染为 PNG 逐项检查 |
| 舞台 · 运行环境 | Git Bash / WSL · Git · TeX Live 或 MiKTeX | 仓库脚本、模板宏包与跨平台执行 |

完整安装与自检见 [`ENVIRONMENT.md`](ENVIRONMENT.md)。

---

## 排练与演出：快速开始

```bash
# 1. 调音：初始化研究工作区（竞赛支持 cumcm / 51mcm / mcm-icm；格式支持 pdf / docx）
python scripts/workspace_init.py --workspace ../contest-workspace --competition cumcm --output-format pdf

# 2. 看总谱：查看当前阶段与状态
python scripts/stage_executor.py current --workspace ../contest-workspace

# 3. 开场：开始当前阶段（系统自动同步所需工具、参考资料与模板）
python scripts/stage_executor.py begin DISCOVERY --workspace ../contest-workspace

# 4. 乐章收束：验证 → 门禁 → 完成 → 休止符（核验点）
python scripts/stage_executor.py validate  DISCOVERY --workspace ../contest-workspace
python scripts/stage_executor.py gate_check DISCOVERY --workspace ../contest-workspace
python scripts/stage_executor.py complete  DISCOVERY --workspace ../contest-workspace --artifacts "问题分析.md"
python scripts/stage_executor.py checkpoint DISCOVERY --workspace ../contest-workspace --action approve --note "reviewed"
```

在 Codex / Skill 环境中，直接把本仓库（`D:\orchestra`）配置为全局 Skill，然后发送：

```text
开始处理我上传的数学建模赛题。
竞赛类型：CUMCM
模式：冠军模式
论文撰写方式：LaTeX
```

---

## 演出状态

| 状态 | 命令行 | 说明 |
| --- | --- | --- |
| 变奏（enhancement） | `python scripts/pipeline_manager.py set-phase enhancement --workspace ..` | 基线之上做受控改进，不能绕过基线证据 |
| 彩排（championship） | `python scripts/pipeline_manager.py set-mode championship --workspace ..` | 论文完成后至少三轮独立审稿，P0 归零、P1 ≤ 2、综合分 ≥ 85 方可提交 |

---

## 乐谱目录

```text
orchestra/
├── SKILL.md          # Skill 入口与总执行规则
├── ENVIRONMENT.md    # 环境安装、依赖分层与自检
├── agents/           # Skill 界面配置
├── assets/           # 工作流清单、竞赛配置、模板和共享工具
├── references/       # 工作流指南、知识库和阶段协议
└── scripts/          # 初始化、状态机、门禁、审稿和回归脚本
```

| 主题 | 文档 |
| --- | --- |
| 总流程与阶段映射 | [`references/workflow-map.md`](references/workflow-map.md) |
| 阶段门禁与人工核验 | [`references/gate-matrix.md`](references/gate-matrix.md) |
| 阶段控制与增强操作 | [`references/phase-control.md`](references/phase-control.md) |
| 冠军审稿方法 | [`references/championship-review-method.md`](references/championship-review-method.md) |
| 声部角色契约 | [`references/subagent-architecture.md`](references/subagent-architecture.md) |
| 竞赛机器配置 | [`assets/competition_profiles.json`](assets/competition_profiles.json) |

---

## 边界

- 自动门禁只能检查已编码的合同，无法证明题意、模型、数据或结论绝对正确；
- 外部资料、参考文献、数据集与竞赛规则必须回到原始来源核验；
- `championship` 是内部质量模式名称，不代表获奖、录用或任何第三方评价；
- 最终提交前必须完成人工通读、匿名检查与格式确认。

---

<p align="center">
  <img src="assets/branding/mark.svg" alt="" width="72">
</p>

<p align="center"><strong>Orchestra</strong> · MIT License · 七个乐章，一场演出；让研究可复现，让论文有据可循</p>
