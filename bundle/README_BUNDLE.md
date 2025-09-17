# Building Standalone Executable

## PyInstaller Build (Requires Long Path Support)
If Windows Long Path support is enabled:

### Quick Build
Run `build.bat` to automatically install dependencies and build the executable.

### Manual Build
1. Install dependencies:
   ```bash
   python -m pip install -r requirements_bundle.txt
   ```

2. Build executable:
   ```bash
   python build_exe.py
   ```

## Alternative: Batch File Launcher
If PyInstaller installation fails due to path length issues:

- Use `run_mouse_mover.bat` - Double-click to run the script
- Requires Python to be installed on target machine
- Simpler distribution method

## Output
- **PyInstaller**: `dist/MouseMover.exe` (standalone)
- **Batch**: `run_mouse_mover.bat` (requires Python)