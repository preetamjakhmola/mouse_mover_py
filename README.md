# Mouse Mover - Keep System Active

A Python script that prevents your system from going to sleep and keeps applications like Zoom active by moving the mouse randomly.

## Features

- **Random Movement**: Moves mouse to random screen positions for 30 seconds
- **Variable Sleep**: Sleeps for random intervals between 5-30 seconds
- **Natural Behavior**: Varying movement speeds and pauses to avoid detection
- **Safe Exit**: Proper cleanup when stopped with Ctrl+C

## Requirements

- Python 3.x
- pyautogui library

## Installation

1. Install Python dependencies:
```bash
python -m pip install pyautogui
```

Or using requirements file:
```bash
python -m pip install -r requirements.txt
```

## Usage

### Start the application:
```bash
python mouse_mover.py
```

### Stop the application:
Press `Ctrl+C` in the terminal

### Force stop if running in background:
```bash
# Find Python processes
tasklist | findstr python

# Kill specific process (replace PID with actual process ID)
taskkill /PID <PID> /F
```

## How it Works

1. **Active Phase**: Moves mouse randomly across screen for 30 seconds
   - Random coordinates within screen bounds
   - Variable movement duration (0.2-0.8 seconds)
   - Random pauses between moves (0.5-2 seconds)

2. **Sleep Phase**: Waits for random interval (5-30 seconds)
   - Unpredictable timing to avoid pattern detection

3. **Repeat**: Cycles between active and sleep phases

## Use Cases

- Prevent system sleep during long meetings
- Keep Zoom/Teams status active
- Maintain system activity during downloads
- Avoid screen savers during presentations

## Safety Notes

- Script disables pyautogui failsafe for uninterrupted operation
- Always use Ctrl+C to stop properly
- Check for background processes if mouse continues moving after stopping