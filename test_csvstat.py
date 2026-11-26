#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Hayashi Masayuki
# SPDX-License-Identifier: MIT

import json
import subprocess
import unittest
from pathlib import Path

COMMAND = Path(__file__).resolve().parent / "csvstat"

class CsvstatTest(unittest.TestCase):
    def run_command(self, args, data):
        return subprocess.run([str(COMMAND), *args], input=data, text=True, capture_output=True)

    def test_basic_statistics(self):
        result = self.run_command(["2"], "a,2\nb,4\nc,6\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stderr, "")
        stats = json.loads(result.stdout)
        self.assertEqual((stats["count"], stats["min"], stats["max"], stats["mean"]), (3, 2.0, 6.0, 4.0))
        self.assertAlmostEqual(stats["rms"], (56 / 3) ** 0.5)

    def test_header_option(self):
        result = self.run_command(["1", "--header"], "value\n1\n3\n")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["mean"], 2.0)

    def test_quoted_field(self):
        result = self.run_command(["2"], 'sensor,"1.5"\nsensor,"2.5"\n')
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["mean"], 2.0)

    def test_empty_input(self):
        result = self.run_command(["1"], "")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("no numeric data", result.stderr)

    def test_non_numeric_value(self):
        result = self.run_command(["1"], "1\nabc\n")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("line 2", result.stderr)

    def test_missing_column(self):
        result = self.run_command(["3"], "1,2\n")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("does not exist", result.stderr)

    def test_non_finite_value(self):
        result = self.run_command(["1"], "nan\n")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("non-finite", result.stderr)

    def test_invalid_column(self):
        result = self.run_command(["0"], "1\n")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")
        self.assertIn("column must be 1 or greater", result.stderr)

if __name__ == "__main__":
    unittest.main()
