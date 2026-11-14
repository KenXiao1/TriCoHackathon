# QTrack

## Local Python environment

Use the project's uv environment (Python 3.12) for local validation:

```sh
uv sync --locked
uv run --locked python -c "import qiskit, qiskit_aer; print(qiskit.__version__, qiskit_aer.__version__)"
```

Qiskit, Aer, and the notebook kernel (`ipykernel`) are already declared in
`pyproject.toml` and pinned in `uv.lock`. In your notebook editor, select
`.venv/bin/python` as the kernel, then run the setup cell before the task cells
and their self-checks. For Python scripts, use `uv run --locked python script.py`.
