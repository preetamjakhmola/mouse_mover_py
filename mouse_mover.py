import pyautogui
import random
import time
import signal
import sys

# Disable pyautogui failsafe
pyautogui.FAILSAFE = False

# Global flag to control the loop
running = True

def signal_handler(sig, frame):
    global running
    running = False
    print("\nStopping mouse mover...")
    sys.exit(0)

# Set up signal handler for Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

def move_mouse_randomly():
    
    global running
    screen_width, screen_height = pyautogui.size()
    
    while running:
        if not running:
            break
            
        # Move mouse randomly for 30 seconds
        end_time = time.time() + 30
        while time.time() < end_time and running:
            x = random.randint(0, screen_width - 1)
            y = random.randint(0, screen_height - 1)
            pyautogui.moveTo(x, y, duration=random.uniform(0.2, 0.8))
            if not running:
                break
            time.sleep(random.uniform(0.5, 2))
        
        if not running:
            break
            
        # Sleep for random interval between 5-30 seconds
        sleep_time = random.randint(25, 60)
        print(f"waiting for {sleep_time} seconds...")
        
        # Sleep in small chunks to allow for quick exit
        for _ in range(sleep_time):
            if not running:
                break
            time.sleep(1)

if __name__ == "__main__":
    print("app is running... Press Ctrl+C to stop.")
    try:
        move_mouse_randomly()
    except KeyboardInterrupt:
        running = False
        print("\nApp is stopped.")
    finally:
        running = False
        print("Cleanup complete.")