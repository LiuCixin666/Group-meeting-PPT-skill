# ppt-high-fidelity-reconstruction

一个用于把概念图、截图、论文插图或旧幻灯片**坐标级重建为可编辑 PowerPoint** 的 Codex Skill。

它面向科研汇报、方法流程、探测器示意、统计卡片、流程图和公式页等高保真场景，强调：

- 参考图是最终视觉目标，不是重新设计的灵感图；
- 文本、卡片、箭头、表格和简易图表保持可编辑；
- 复杂科学插图、论文结果图、logo 和精细图标采用受控裁剪；
- 坐标表驱动生成，导出预览并用 overlay/diff 检查；
- 迭代时冻结正确区域，只修正明确问题。

## 安装

个人全局安装时，将整个目录复制到：

```text
$HOME/.agents/skills/ppt-high-fidelity-reconstruction/
```

若只供某个仓库使用，则放在仓库根目录：

```text
<repository>/.agents/skills/ppt-high-fidelity-reconstruction/
```

Codex 会自动发现新增或更新的 Skill；若未出现，重启 Codex。

## 调用示例

```text
使用 $ppt-high-fidelity-reconstruction，依据 concept.png 将该页 1:1 重建为
10 × 7.5 in 的可编辑 PPTX。复杂英文插图保留原图，其他元素全部可编辑；
输出预览、overlay、坐标表和检查报告。
```

```text
使用 $ppt-high-fidelity-reconstruction 迭代 existing.pptx。
只修复图标还原、文字遮挡和连接线走向，其他区域保持冻结。
```

## 目录

```text
ppt-high-fidelity-reconstruction/
├─ SKILL.md
├─ agents/openai.yaml
├─ references/
│  ├─ workflow.md
│  ├─ concept-image-authoring.md
│  ├─ schemas.md
│  ├─ style-and-typography.md
│  ├─ checking.md
│  └─ windows-powerpoint.md
└─ scripts/
   ├─ init_task.py
   ├─ crop_icons.py
   ├─ compare_previews.py
   └─ inspect_pptx.py
```

## 依赖

- Python 3.9+
- Pillow（图像裁剪、预览对比）
- Windows 高保真输出推荐安装 Microsoft PowerPoint 与 `pywin32`
- 跨平台可使用 `python-pptx`，但原生公式和部分高级样式能力较弱

## 边界

本 Skill 不适用于普通文字型演示文稿、自由发挥式视觉重设计，也不会用整页截图伪装成可编辑 PPT。科学机制、公式、数值和引用必须来自用户材料或可验证来源。
