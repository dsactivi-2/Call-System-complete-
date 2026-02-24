# Contributing to the AI Call Agent System

Thank you for contributing! Please read these guidelines before opening a PR.

---

## Ground Rules

1. **No direct pushes to `main`.**  
   All changes must go through a Pull Request, even trivial ones.

2. **CI must be green.**  
   The PR cannot be merged until all required status checks pass:
   - `Python (ruff + pytest)` (both matrix versions)
   - `CodeQL Security Analysis`

3. **At least one review required.**  
   A PR requires approval from at least one code owner (`@dsactivi-2`) before merging.

4. **Linear history preferred.**  
   Use "Squash and merge" or "Rebase and merge" – avoid plain merges to keep `git log` clean.

---

## Branching Convention

| Branch | Purpose |
|--------|---------|
| `main` | Production-ready code; protected |
| `develop` | Integration branch (optional); protected |
| `feat/<short-description>` | New features |
| `fix/<short-description>` | Bug fixes |
| `chore/<short-description>` | Tooling, dependencies, refactors |
| `docs/<short-description>` | Documentation-only changes |

---

## Development Workflow

### 1. Set up your environment

```bash
# Clone and enter repo
git clone <repo-url>
cd Call-System-complete-

# Create & activate virtual environment
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e ".[dev]"

# Configure env vars
cp .env.example .env
```

### 2. Create a branch

```bash
git checkout -b feat/your-feature
```

### 3. Make your changes

- Follow the existing code style (enforced by `ruff`).
- Add tests for new functionality.
- Update documentation if needed.

### 4. Run checks locally

```bash
# Lint
ruff check .

# Format
ruff format .

# Type check
mypy apps/ services/

# Tests
pytest
```

### 5. Push and open a PR

```bash
git push origin feat/your-feature
# Then open a PR on GitHub against `main`
```

Fill in the [PR template](.github/PULL_REQUEST_TEMPLATE.md) completely.

---

## Adding a New Integration

1. Create a new directory under `services/integrations/<name>/`.
2. Add a `__init__.py` with a module docstring describing the provider.
3. Implement a connector that inherits from the appropriate `Base*Connector`.
4. Register the connector in the factory function.
5. Add smoke tests in `tests/`.
6. Document config variables in `.env.example`.

---

## Adding a New Service

1. Create a directory under `services/<service_name>/`.
2. Add `__init__.py` with TODO docstring.
3. Add a core module (e.g. `processor.py`, `handler.py`).
4. Add tests under `tests/`.
5. Update `docs/architecture.md` if the architecture changes.

---

## Code Style

- **Formatter / Linter**: `ruff` (config in `pyproject.toml`)
- **Type hints**: required for all public functions
- **Docstrings**: Google style
- **Line length**: 100 characters
- **Imports**: sorted by `ruff` (isort rules)

---

## Questions?

Open a GitHub Discussion or ping `@dsactivi-2` in the PR.
