@echo off
setlocal EnableExtensions

REM ============================================================
REM  CPSC 610 — Python for Data Analysis
REM  Windows setup (safe to run more than once)
REM ============================================================

cd /d "%~dp0"
if errorlevel 1 (
  echo ERROR: Could not change to the course folder.
  goto :fail
)

echo.
echo ========================================
echo  CPSC 610 Course Setup (Windows)
echo ========================================
echo.
echo Course folder:
echo   %CD%
echo.

REM --- Ensure uv is available ---------------------------------
where uv >nul 2>&1
if errorlevel 1 (
  echo uv not found. Installing uv...
  powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://astral.sh/uv/install.ps1 | iex"
  if errorlevel 1 (
    echo ERROR: Could not install uv.
    echo Try again with an internet connection, or install uv from https://docs.astral.sh/uv/
    goto :fail
  )

  REM Refresh PATH for this window (uv is not on PATH until a new window opens)
  if exist "%USERPROFILE%\.local\bin\uv.exe" set "PATH=%USERPROFILE%\.local\bin;%PATH%"
  if exist "%USERPROFILE%\.cargo\bin\uv.exe" set "PATH=%USERPROFILE%\.cargo\bin;%PATH%"
  if exist "%LOCALAPPDATA%\uv\uv.exe" set "PATH=%LOCALAPPDATA%\uv;%PATH%"

  where uv >nul 2>&1
  if errorlevel 1 (
    echo ERROR: uv was installed, but this window cannot find it yet.
    echo Close this window, then run SETUP-WINDOWS.bat again.
    goto :fail
  )
) else (
  echo Found uv:
  uv --version
)

echo.
echo Installing Python 3.12 and course packages...
echo This may take a few minutes the first time.
echo Running it again is safe.
echo.

uv python install 3.12
if errorlevel 1 (
  echo ERROR: Could not install Python 3.12.
  goto :fail
)

uv sync --python 3.12
if errorlevel 1 (
  echo ERROR: Could not install the course packages.
  goto :fail
)

".venv\Scripts\python.exe" -m ipykernel install --user --name=cpsc610-python --display-name="Python (CPSC 610)"
if errorlevel 1 (
  echo ERROR: Could not register the Jupyter kernel.
  goto :fail
)

echo.
echo ========================================
echo  Setup complete!
echo ========================================
echo.
echo Next steps:
echo   1. Open this whole course folder in VS Code
echo      (File ^> Open Folder... and choose this folder)
echo   2. If VS Code asks, install the Python and Jupyter extensions
echo   3. Open the notebook for this week and run the cells
echo.
echo If a notebook asks for a kernel, choose Python (CPSC 610).
echo.
pause
endlocal
exit /b 0

:fail
echo.
echo ========================================
echo  Setup failed.
echo ========================================
echo.
echo Read the message above, then run SETUP-WINDOWS.bat again.
echo.
pause
endlocal
exit /b 1
