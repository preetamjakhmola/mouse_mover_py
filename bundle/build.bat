@echo off
echo Installing dependencies...
python -m pip install -r requirements_bundle.txt

echo Building executable...
python build_exe.py

echo Build complete! Check dist folder for MouseMover.exe
pause