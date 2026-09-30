"""Sanity checks that the PowerPoint deck in this repo is a valid .pptx package.

Uses only the Python standard library. Run with:
    python -m pytest
or:
    python -m unittest discover -s tests
"""

import re
import unittest
import zipfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DECK = REPO_ROOT / "Beyond-Better-Models-Updated-v3-Auto.pptx"
SLIDE_PATTERN = re.compile(r"ppt/slides/slide\d+\.xml")


class TestPptx(unittest.TestCase):
    def test_deck_exists(self):
        self.assertTrue(DECK.is_file(), f"Missing deck: {DECK}")

    def test_is_valid_zip(self):
        self.assertTrue(zipfile.is_zipfile(DECK))
        with zipfile.ZipFile(DECK) as zf:
            self.assertIsNone(zf.testzip(), "Corrupt entry found in .pptx")

    def test_has_required_parts(self):
        with zipfile.ZipFile(DECK) as zf:
            names = set(zf.namelist())
        self.assertIn("[Content_Types].xml", names)
        self.assertIn("ppt/presentation.xml", names)

    def test_has_slides(self):
        with zipfile.ZipFile(DECK) as zf:
            slides = [n for n in zf.namelist() if SLIDE_PATTERN.fullmatch(n)]
        self.assertGreater(len(slides), 0, "Deck contains no slides")


if __name__ == "__main__":
    unittest.main()
