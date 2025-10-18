#!/usr/bin/env python3
"""Clean Jupyter notebooks by removing metadata.widgets entries.

This script backs up each notebook as .bak, removes top-level metadata.widgets
and any cell.metadata.widgets, and writes the cleaned notebook back.

Usage:
  python tools/clean_notebooks.py modelTraining.ipynb
  python tools/clean_notebooks.py *.ipynb

"""

import nbformat
import sys
from pathlib import Path

def clean_notebook(path: Path):
    backup = path.with_suffix(path.suffix + '.bak')
    if not backup.exists():
        path.replace(backup)
    else:
        # If backup already exists, work on the given file directly but still keep a numbered backup
        i = 1
        while backup.exists():
            backup = path.with_suffix(path.suffix + f'.bak{i}')
            i += 1
        path.replace(backup)

    nb = nbformat.read(backup, as_version=4)

    # remove top-level metadata.widgets if present
    if 'widgets' in nb.metadata:
        del nb.metadata['widgets']

    # remove metadata.widgets from each cell
    for cell in nb.cells:
        md = cell.get('metadata')
        if isinstance(md, dict) and 'widgets' in md:
            del md['widgets']

    nbformat.write(nb, path)
    print(f"Cleaned: {path} (backup: {backup.name})")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python tools/clean_notebooks.py <notebook1.ipynb> [notebook2.ipynb ...]")
        sys.exit(1)

    for pattern in sys.argv[1:]:
        for p in Path('.').glob(pattern):
            if p.is_file() and p.suffix == '.ipynb':
                try:
                    clean_notebook(p)
                except Exception as e:
                    print(f"Failed to clean {p}: {e}")