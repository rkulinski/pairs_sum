# Unique sum pairs finder
Given an unsorted array A[]. The task is to print all unique pairs in the unsorted array with equal sum.

# Pull requests checks
GitHub Actions Checks: Every pull request undergoes automated checks via GitHub Actions, including:
- Formatting and Lint Check
- Test Suite
- Mypy Verification

# How to run
Sample run with example
```
uv run main.py
```

# Tests
```
uv run pytest test_main.py
```

# Dependencies
This project is using `uv`.

https://docs.astral.sh/uv/

# Formatting
This project is using `ruff` for formatting and linting and `mypy` for type checking.

Use this command to format code
```
uv run ruff check --fix
```

Use this command to run type checks
```
uv run mypy . --strict
```
