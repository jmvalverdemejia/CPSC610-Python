#!/bin/bash
# ============================================================
#  CPSC 610 — Python for Data Analysis
#  macOS setup (safe to run more than once)
# ============================================================

set -u
set -o pipefail

# Move to the folder that contains this script (handles spaces in paths)
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

die() {
  echo ""
  echo "ERROR: $*"
  echo ""
  echo "========================================"
  echo " Setup failed."
  echo "========================================"
  echo ""
  echo "Read the message above, then run SETUP-MAC.command again."
  echo ""
  read -r -p "Press Enter to close..." || true
  exit 1
}

echo ""
echo "========================================"
echo " CPSC 610 Course Setup (macOS)"
echo "========================================"
echo ""
echo "Course folder:"
echo "  $SCRIPT_DIR"
echo ""

# --- Ensure uv is available -----------------------------------
if ! command -v uv >/dev/null 2>&1; then
  echo "uv not found. Installing uv..."
  curl -LsSf https://astral.sh/uv/install.sh | sh || die "Could not install uv. Check your internet connection and run this script again."

  # Common install locations for this Terminal window
  export PATH="$HOME/.local/bin:$HOME/.cargo/bin:$PATH"

  if ! command -v uv >/dev/null 2>&1; then
    die "uv was installed, but this Terminal cannot find it yet. Quit Terminal, open it again, then run SETUP-MAC.command."
  fi
else
  echo "Found uv:"
  uv --version || die "uv is installed, but 'uv --version' failed."
fi

echo ""
echo "Installing Python 3.12 and course packages..."
echo "This may take a few minutes the first time."
echo "Running it again is safe."
echo ""

uv python install 3.12 || die "Could not install Python 3.12."
uv sync --python 3.12 || die "Could not install the course packages."

"$SCRIPT_DIR/.venv/bin/python" -m ipykernel install --user --name=cpsc610-python --display-name="Python (CPSC 610)" \
  || die "Could not register the Jupyter kernel."

echo ""
echo "========================================"
echo " Setup complete!"
echo "========================================"
echo ""
echo "Next steps:"
echo "  1. Open this whole course folder in VS Code"
echo "     (File > Open Folder... and choose this folder)"
echo "  2. If VS Code asks, install the Python and Jupyter extensions"
echo "  3. Open the notebook for this week and run the cells"
echo ""
echo "If a notebook asks for a kernel, choose Python (CPSC 610)."
echo ""
read -r -p "Press Enter to close..." || true
exit 0
