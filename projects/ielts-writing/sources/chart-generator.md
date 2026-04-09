---
type: doc
title: "Task 1 Chart Generator — How to Use"
created: 2026-04-09
tags: [ielts, writing, task1, tools]
status: active
lang: en
---

# Task 1 Chart Generator

## Location

`D:\ANHDUC\Path_finder\scripts\gen_task1_charts.py`
Output dir: `D:\ANHDUC\Path_finder\scripts\charts\`

## Run Demo (5 sample charts)

```bash
cd D:/ANHDUC/Path_finder
source venv/Scripts/activate
python scripts/gen_task1_charts.py
```

Outputs: `task1_line_graph.png`, `task1_bar_chart.png`, `task1_pie_chart.png`, `task1_table.png`, `task1_process.png`

## Generate a Custom Challenge

```python
from scripts.gen_task1_charts import gen_challenge

path = gen_challenge(spec_dict, "my_output.png")
```

## Spec Formats

### Line Graph
```python
{
    "type": "line",
    "title": "...",
    "years": [2000, 2001, ..., 2020],       # x-axis
    "series": {
        "Label A": [val, val, ...],          # one list per line
        "Label B": [val, val, ...],
    },
    "ylabel": "% of Population",            # optional, default "Value"
}
```

### Bar Chart
```python
{
    "type": "bar",
    "title": "...",
    "categories": ["Cat1", "Cat2", "Cat3"],  # x-axis groups
    "groups": {
        "Group A": [val, val, val],          # one list per colour group
        "Group B": [val, val, val],
    },
    "ylabel": "Hours per week",             # optional
}
```

### Pie Chart
```python
{
    "type": "pie",
    "title": "...",
    "labels": ["Coal", "Oil", "Gas", ...],  # slice labels (shared across panels)
    "panels": {
        "2000": [50, 25, 15, 8, 2],         # one entry = one pie chart
        "2020": [20, 18, 22, 15, 25],       # two entries = side-by-side
    },
}
```

### Table
```python
{
    "type": "table",
    "title": "...",
    "col_labels": ["Country", "Col B", "Col C"],
    "rows": [
        ["Row1ColA", "Row1ColB", "Row1ColC"],
        ["Row2ColA", "Row2ColB", "Row2ColC"],
    ],
}
```

### Process Diagram (8 stages, snake 4x2 layout)
```python
{
    "type": "process",
    "title": "...",
    "stages": [
        "Stage1", "Stage2", "Stage3", "Stage4",   # row 1, left -> right
        "Stage5", "Stage6", "Stage7", "Stage8",   # row 2, right -> left
    ],
}
```

## Constraints

- Process diagram: exactly 8 stages (snake 4x2 layout is hardcoded)
- Pie chart: up to 8 slices (colour palette limit)
- Bar chart: auto-scales bar width to group count
- All PNGs saved to `scripts/charts/` at 150 dpi

## Demo Data

The `DEMO_SPECS` dict in the script contains the full data for all 5 sample charts.
These match the vault sample files in `projects/ielts-writing/samples/task1-*.md`.
