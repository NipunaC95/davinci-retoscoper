#!/usr/bin/env python3

import json
import shutil
import sys
from pathlib import Path
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SOURCE_MACRO = ROOT / "fusion" / "Retscope.setting"
DIST = ROOT / "dist" / "Retscope21.drfx"


def main() -> int:
    if not SOURCE_MACRO.is_file():
        print(f"Missing macro: {SOURCE_MACRO}", file=sys.stderr)
        return 1

    if DIST.exists():
        shutil.rmtree(DIST)

    effect_dir = DIST / "Effects" / "Retscope"
    macro_dir = DIST / "Fusion" / "Macros"
    effect_dir.mkdir(parents=True)
    macro_dir.mkdir(parents=True)

    shutil.copy2(SOURCE_MACRO, effect_dir / "Retscope.setting")
    shutil.copy2(SOURCE_MACRO, macro_dir / "Retscope.setting")
    shutil.copy2(ROOT / "drfx" / "Effects" / "Retscope" / "manifest.xml", effect_dir / "manifest.xml")
    shutil.copy2(ROOT / "assets" / "preview.svg", effect_dir / "preview.svg")

    manifest = json.loads((ROOT / "package" / "manifest.json").read_text(encoding="utf-8"))
    (DIST / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    archive = ROOT / "dist" / "Retscope21.drfx"
    zip_path = ROOT / "dist" / "Retscope21.drfx.zip"
    if zip_path.exists():
        zip_path.unlink()
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as archive_file:
        for path in DIST.rglob("*"):
            if path.is_file():
                archive_file.write(path, path.relative_to(DIST))

    print(f"Built {DIST}")
    print(f"Built {zip_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
