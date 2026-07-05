import json
from pathlib import Path

path = Path(r"c:\Users\Sarim Ahmed\NO_SYNC\week1_data_cleaning\notebooks\week1_data_cleaning.ipynb")
nb = json.loads(path.read_text(encoding="utf-8"))
cells = nb["cells"]

intro_cell = None
import_cell = None

for i, cell in enumerate(cells):
    src = "".join(cell.get("source", []))
    if "# Vortex Tech AI/ML Internship - Week 1" in src:
        intro_cell = i
    if "import os" in src and "import pandas as pd" in src:
        import_cell = i

if intro_cell is None or import_cell is None:
    raise SystemExit("Could not find the intro or import cell")

ordered = [cells[intro_cell], cells[import_cell]] + [c for i, c in enumerate(cells) if i not in {intro_cell, import_cell}]
nb["cells"] = ordered
path.write_text(json.dumps(nb, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print("Notebook reordered successfully")
