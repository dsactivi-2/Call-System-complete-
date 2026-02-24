#!/usr/bin/env bash
# =============================================================================
# setup_local.sh – Bootstrap local development environment
# =============================================================================
set -euo pipefail

PYTHON="${PYTHON:-python3}"
VENV_DIR=".venv"

echo "==> Checking Python version..."
$PYTHON -c "import sys; assert sys.version_info >= (3,11), 'Python 3.11+ required'"

echo "==> Creating virtual environment in $VENV_DIR ..."
if [ ! -d "$VENV_DIR" ]; then
  $PYTHON -m venv "$VENV_DIR"
fi

echo "==> Activating virtual environment..."
# shellcheck disable=SC1091
source "$VENV_DIR/bin/activate"

echo "==> Upgrading pip..."
pip install --upgrade pip --quiet

echo "==> Installing project + dev dependencies..."
pip install -e ".[dev]" --quiet

echo "==> Copying .env.example to .env (if not present)..."
if [ ! -f ".env" ]; then
  cp .env.example .env
  echo "    Created .env – please fill in the required values."
else
  echo "    .env already exists – skipping."
fi

echo "==> Running smoke tests..."
pytest tests/ -q --tb=short

echo ""
echo "✅  Local setup complete!"
echo ""
echo "    Next steps:"
echo "    1. Edit .env with your credentials"
echo "    2. Start the API:    uvicorn apps.api.app.main:app --reload"
echo "    3. Start the worker: python -m apps.worker.main"
echo "    4. View API docs:    http://localhost:8000/docs"
