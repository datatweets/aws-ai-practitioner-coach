#!/usr/bin/env python3
"""Build a Claude-uploadable Skill ZIP using Anthropic's documented folder layout."""
from pathlib import Path
import zipfile

root = Path(__file__).resolve().parents[1]
folder_name = root.name
outputs = [root / "dist" / f"{folder_name}.zip", root / "downloads" / f"{folder_name}.zip"]

include_dirs = {"references", "templates"}
include_scripts = {"scripts/mastery.py"}

def should_include(rel: Path) -> bool:
    posix = rel.as_posix()
    if posix in include_scripts:
        return True
    return bool(rel.parts and rel.parts[0] in include_dirs)

for out in outputs:
    out.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        # Claude Help Center documents a ZIP containing one skill folder.
        # Inside that folder, use lowercase skill.md for Claude upload compatibility.
        zf.writestr(f"{folder_name}/skill.md", (root / "SKILL.md").read_text(encoding="utf-8"))
        for path in sorted(root.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(root)
            if not should_include(rel):
                continue
            zf.write(path, f"{folder_name}/{rel.as_posix()}")
    print(out)
