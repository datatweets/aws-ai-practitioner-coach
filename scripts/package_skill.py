#!/usr/bin/env python3
"""Build a Claude-uploadable ZIP containing only Skill runtime files."""
from pathlib import Path
import zipfile

root = Path(__file__).resolve().parents[1]
dist = root / "dist"
dist.mkdir(exist_ok=True)
out = dist / f"{root.name}.zip"

# Keep the uploaded Skill focused. Repository/CI/setup-only files stay on GitHub.
include_files = {"SKILL.md"}
include_dirs = {"references", "templates"}
include_scripts = {"scripts/mastery.py"}

def should_include(rel: Path) -> bool:
    posix = rel.as_posix()
    if posix in include_files or posix in include_scripts:
        return True
    return bool(rel.parts and rel.parts[0] in include_dirs)

with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for path in sorted(root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(root)
        if not should_include(rel):
            continue
        archive_name = Path(root.name) / rel
        zf.write(path, archive_name.as_posix())

print(out)
