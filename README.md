# CPSC 610 — Python for Data Analysis

A beginner course in VS Code. One setup script installs Python and the course packages. Every week uses that same setup.

## What you need

- A computer running **Windows** or **macOS**
- [VS Code](https://code.visualstudio.com/) installed
- An internet connection the first time you run setup

## Start here

1. Unzip this folder somewhere easy to find, such as **Documents**.
2. Run setup once:
   - **Windows:** double-click `SETUP-WINDOWS.bat`. If Windows warns you, choose **More info** → **Run anyway**.
   - **macOS:** right-click `SETUP-MAC.command` and choose **Open**. The first time, macOS may ask you to confirm.
3. Wait until the window says **Setup complete!**
4. In VS Code, choose **File → Open Folder…** and open this **whole course folder**. Do not open only `module01`, `module02`, or another single week.
5. If VS Code asks, install the recommended **Python** and **Jupyter** extensions.
6. Open that week’s notebook and run the cells.

If a notebook asks you to pick a kernel, choose **Python (CPSC 610)**.

You can run the setup script again whenever you need to. It will not break anything.

## Where each week goes

Each week has its own folder: `module01` through `module10`. Put that week’s notebook and data files inside the matching folder. You do not need to run setup again just to add those files.

```
CPSC610-Python/
├── SETUP-WINDOWS.bat          ← Windows: double-click once
├── SETUP-MAC.command          ← macOS: right-click → Open, once
├── pyproject.toml             ← course packages
├── uv.lock
├── README.md
├── .vscode/                   ← tells VS Code which Python to use
├── .venv/                     ← created by setup; do not edit or delete
└── module01/ … module10/
```

## If something goes wrong

| What you see | What to do |
|--------------|------------|
| The window says **Setup failed.** | Read the lines above that message, then run the same setup script again. |
| A notebook asks which kernel to use | Choose **Python (CPSC 610)**. |
| Packages are missing | Run the setup script again, then close and reopen VS Code. |
