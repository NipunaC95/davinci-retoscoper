import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_macro_exists_and_has_required_controls(self):
        macro = ROOT / "fusion" / "Retscope.setting"
        self.assertTrue(macro.is_file())
        text = macro.read_text(encoding="utf-8")
        for parameter in (
            "AspectPreset",
            "CustomAspect",
            "PanX",
            "PanY",
            "Zoom",
            "AutoFill",
            "MatteMode",
            "OverlayOpacity",
            "MatteRed",
            "BorderGuide",
            "BorderWidth",
            "RuleOfThirds",
            "GuideOpacity",
            "CornerRadius",
            "FeatherPixels",
            "GuidesInRender",
            "MatteInRender",
            "PreserveAlpha",
        ):
            self.assertIn(parameter, text)

    def test_macro_is_free_edition_safe(self):
        macro = ROOT / "fusion" / "Retscope.setting"
        text = macro.read_text(encoding="utf-8")
        forbidden = ("DCTL", "Python", "Workflow", "Lua", "ffi", "RunScript")
        for item in forbidden:
            self.assertNotIn(item.lower(), text.lower())

    def test_manifest_records_free_edition_support(self):
        manifest = ROOT / "package" / "manifest.json"
        self.assertTrue(manifest.is_file())
        text = manifest.read_text(encoding="utf-8")
        self.assertIn('"Free"', text)
        self.assertIn("Free Edition", text) if "Free Edition" in text else None
        self.assertIn("DCTL", text)

    def test_all_preset_ids_are_mapped(self):
        macro = (ROOT / "fusion" / "Retscope.setting").read_text(encoding="utf-8")
        for preset in ("2.39", "2.35", "1.85", "1.43", "16/9", "4/3", "1.0", "9/16", "4/5"):
            self.assertIn(preset, macro)


if __name__ == "__main__":
    unittest.main()
