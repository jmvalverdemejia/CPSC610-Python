#!/usr/bin/env python3
"""Remove machine-specific kernel metadata from all course notebooks.

Safe to run multiple times. Strips absolute paths, usernames, and local
kernel specs so notebooks stay portable for students.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Portable kernelspec — no absolute paths or host-specific names
PORTABLE_KERNELSPEC = {
    "display_name": "Python 3 (ipykernel)",
    "language": "python",
    "name": "python3",
}

# Keep only portable language_info fields (drop version/path details)
PORTABLE_LANGUAGE_INFO = {
    "name": "python",
    "mimetype": "text/x-python",
    "file_extension": ".py",
    "pygments_lexer": "ipython3",
}


def clean_notebook(path: Path) -> bool:
    """Clean one notebook. Returns True if the file was modified."""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"  SKIP (unreadable): {path.relative_to(ROOT)} — {exc}")
        return False

    metadata = data.setdefault("metadata", {})
    original = json.dumps(metadata, sort_keys=True)

    # Replace kernelspec with a portable one
    metadata["kernelspec"] = dict(PORTABLE_KERNELSPEC)

    # Normalize language_info (drop interpreter path / version noise)
    lang = metadata.get("language_info")
    if isinstance(lang, dict):
        cleaned = dict(PORTABLE_LANGUAGE_INFO)
        # Keep version only if it is a simple string (optional educational hint)
        version = lang.get("version")
        if isinstance(version, str) and version and "/" not in version and "\\" not in version:
            cleaned["version"] = version
        metadata["language_info"] = cleaned
    else:
        metadata["language_info"] = dict(PORTABLE_LANGUAGE_INFO)

    # Drop keys that often embed machine-specific paths
    for key in (
        "interpreter",
        "vscode",
        "colab",
        "accelerator",
        "widgets",
        "kernel_info",
    ):
        metadata.pop(key, None)

    data["metadata"] = metadata

    if json.dumps(metadata, sort_keys=True) == original:
        return False

    path.write_text(
        json.dumps(data, indent=1, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return True


def main() -> int:
    notebooks = sorted(ROOT.glob("module*/**/*.ipynb"))
    # Also clean any root-level notebooks if present
    notebooks += sorted(ROOT.glob("*.ipynb"))

    if not notebooks:
        print("No notebooks found.")
        return 0

    changed = 0
    for nb in notebooks:
        # Skip checkpoint copies
        if ".ipynb_checkpoints" in nb.parts:
            continue
        if clean_notebook(nb):
            print(f"  cleaned: {nb.relative_to(ROOT)}")
            changed += 1
        else:
            print(f"  ok:      {nb.relative_to(ROOT)}")

    print(f"\nDone. Updated {changed} of {len(notebooks)} notebook(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
