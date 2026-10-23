# Python Debugging and Testing with AI

Assignment 8 – AI & Prompt Engineering (Module 2), JECRC University.

`grade_utils.py` started with several bugs. An AI assistant (Claude) was used to
find and fix them and to generate unit tests with Python's built-in `unittest`.

## Files

| File | Purpose |
| --- | --- |
| `grade_utils.py` | Helper functions: `average`, `grade`, `highest`, `percentage`, `remove_failed` |
| `test_grade_utils.py` | 27 unit tests: normal cases, boundary values and edge cases |

## Run the tests

```bash
python3 -m unittest -v test_grade_utils.py
```

## Result

- Original (buggy) code: 27 tests run, 14 failures and 2 errors
- Fixed code: all 27 tests pass

Commit history shows each step: original code, tests added, bugs fixed.

Author: Samyak Jain
