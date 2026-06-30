#!/bin/bash
# Thin wrapper — all logic lives in Python
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_DIR="$SCRIPT_DIR/.venv"
REQUIREMENTS="$SCRIPT_DIR/devops/cdk/requirements.txt"

# Create .venv if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
  echo "Creating virtual environment at $VENV_DIR ..."
  python3 -m venv "$VENV_DIR"
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Install/update requirements if requirements.txt is newer than the venv marker
MARKER="$VENV_DIR/.requirements_installed"
if [ ! -f "$MARKER" ] || [ "$REQUIREMENTS" -nt "$MARKER" ]; then
  echo "Installing dependencies from $REQUIREMENTS ..."
  pip install --upgrade pip -q
  pip install -r "$REQUIREMENTS" -q
  touch "$MARKER"
fi

python3 "$SCRIPT_DIR/devops/cdk/deploy.py" "$@"
