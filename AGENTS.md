# Project Guidelines

- Manage the environment with `uv sync --locked` and run Python with `uv run --locked python`. Check dependencies in this environment rather than the system Python.
- Select `.venv/bin/python` as the notebook kernel. After changing a task, run the setup cell, relevant functions, and their self-checks; report what was verified.
- Keep changes scoped to the current task. Preserve other contributors' code, Markdown, AI use disclosures, and valid outputs.
- Keep `.ipynb` files valid JSON and avoid unrelated formatting changes. Resolve merge conflicts cell by cell, preserving valid changes from both sides.
- Before committing, review `git status`, the diff, and `git diff --check`; check remote updates and resolve conflicts. Stage only relevant files. Push only when requested.
