from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


renderer = load_module("render_sheet_values", ROOT / "scripts" / "render_sheet_values.py")
validator = load_module("validate_result", ROOT / "scripts" / "validate_result.py")


class RenderSheetValuesTests(unittest.TestCase):
    def test_fetch_history_parent_only_and_both_unmapped_sides(self):
        payload = {
            "rows": [
                {
                    "physical_row": 8,
                    "crime_status": "crime",
                    "article": {"status": "fetched"},
                    "good_categories": {"Organized Contraband Smuggling": []},
                    "bad_categories": {"Excluded": ["Out of US"]},
                    "unmapped_candidates": [
                        {
                            "gap_type": "subcategory",
                            "parent_category": "Organized Contraband Smuggling",
                            "candidate_name": "Rare antiquities smuggling",
                            "evidence": "organized concealed shipment",
                        }
                    ],
                    "unmapped_bad_candidates": [
                        {
                            "gap_type": "subcategory",
                            "parent_category": "Excluded",
                            "candidate_name": "Unlisted routing flag",
                            "evidence": "manual confirmation needed",
                        }
                    ],
                    "confidence": 0.82,
                    "evidence": ["cross-border cargo", "foreign incident confirmed"],
                    "needs_review": True,
                }
            ]
        }
        rendered = renderer.render(payload)
        row = rendered["values"][0]
        self.assertEqual(row[1], "Organized Contraband Smuggling")
        self.assertEqual(row[2], "Excluded: Out of US")
        self.assertEqual(row[3], "Yes")
        self.assertIn("cross-border cargo", row[4])
        self.assertEqual(rendered["range"], "K8:P8")
        self.assertEqual(len(row), 6)
        self.assertIn("Good subcategory under Organized Contraband Smuggling", row[5])
        self.assertIn("Bad subcategory under Excluded", row[5])

    def test_renderer_rejects_declared_scope_mismatch(self):
        payload = {
            "scope": {"start_row": 8, "end_row": 9},
            "rows": [
                {
                    "row": 8,
                    "crime_status": "noncrime",
                    "article": {"status": "not_needed"},
                    "good_categories": {},
                    "bad_categories": {},
                    "confidence": 0.9,
                    "evidence": "human-interest story",
                }
            ],
        }
        with self.assertRaisesRegex(ValueError, "declared physical scope"):
            renderer.render(payload)

    def test_failed_article_attempt_renders_yes_and_hides_confidence(self):
        payload = {
            "rows": [
                {
                    "row": 11,
                    "crime_status": "needs_article",
                    "article": {"status": "fetch_failed"},
                    "good_categories": {},
                    "bad_categories": {},
                    "confidence": 0.2,
                    "evidence": "publisher blocked the assigned URL",
                    "needs_review": True,
                }
            ]
        }
        row = renderer.render(payload)["values"][0]
        self.assertEqual(row[3], "Yes")
        self.assertEqual(row[4], "publisher blocked the assigned URL")
        self.assertEqual(len(row), 6)
        self.assertNotIn(0.2, row)


class ValidateResultTests(unittest.TestCase):
    def validate_rows(self, rows):
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "result.json"
            path.write_text(json.dumps({"rows": rows}), encoding="utf-8")
            return validator.validate(path)

    def base_row(self, **overrides):
        row = {
            "row": 2,
            "crime_status": "crime",
            "good_categories": {},
            "bad_categories": {},
            "unmapped_candidates": [],
            "unmapped_bad_candidates": [],
            "confidence": 0.9,
            "evidence": "supported evidence",
            "needs_review": False,
        }
        row.update(overrides)
        return row

    def test_bad_only_crime_is_valid(self):
        row = self.base_row(bad_categories={"Prostitution / Commercial Sex": ["Prostitution / Commercial Sex"]})
        self.assertEqual(self.validate_rows([row]), [])

    def test_unmapped_candidate_requires_review(self):
        row = self.base_row(
            good_categories={"Theft, Fraud & Financial Crime": []},
            unmapped_candidates=[{"candidate_name": "Rare property theft", "evidence": "property taken"}],
        )
        self.assertIn("unmapped candidate requires needs_review", "\n".join(self.validate_rows([row])))

    def test_forced_trafficking_is_valid(self):
        row = self.base_row(
            good_categories={"Human Trafficking, Forced Labor & Exploitation": ["Labor Trafficking / Forced Labor"]},
            evidence="workers were coerced into forced labor through debt bondage",
        )
        self.assertEqual(self.validate_rows([row]), [])

    def test_voluntary_prostitution_cannot_be_good_trafficking(self):
        row = self.base_row(
            good_categories={"Human Trafficking, Forced Labor & Exploitation": []},
            evidence="adult voluntary prostitution and commercial sex",
        )
        self.assertIn("lacks force/coercion/exploitation evidence", "\n".join(self.validate_rows([row])))

    def test_organized_contraband_requires_operation_evidence(self):
        valid = self.base_row(
            good_categories={"Organized Contraband Smuggling": ["Weapons or Firearms Smuggling"]},
            evidence="organized cross-border firearms smuggling operation",
        )
        self.assertEqual(self.validate_rows([valid]), [])
        invalid = self.base_row(
            good_categories={"Organized Contraband Smuggling": []},
            evidence="person possessed one illegal firearm locally",
        )
        self.assertIn("lacks smuggling-operation evidence", "\n".join(self.validate_rows([invalid])))

    def test_failed_article_attempt_requires_review(self):
        row = self.base_row(
            crime_status="needs_article",
            article={"status": "infrastructure_error"},
            needs_review=False,
        )
        self.assertIn("failed article attempt requires needs_review", "\n".join(self.validate_rows([row])))

    def test_animal_related_bad_category_is_valid_and_additive(self):
        row = self.base_row(
            good_categories={"Assault, Weapons & Violent Crime": ["Assault / Battery"]},
            bad_categories={"Animal-Related Stories": ["Animal Cruelty / Abuse"]},
            article={"status": "not_needed"},
            evidence="suspect assaulted a person and deliberately injured the victim's dog",
        )
        self.assertEqual(self.validate_rows([row]), [])


if __name__ == "__main__":
    unittest.main()
