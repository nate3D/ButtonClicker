""""" ButtonClicker.py - An improved script to click a button on the screen. """

import argparse
import ctypes
import os
import signal
import sys
import time
from datetime import datetime

import pyautogui
import pygetwindow as gw


# Argument parser for command-line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Button Clicker Script")
    parser.add_argument(
        "--scan_interval",
        type=float,
        default=1,
        help="Interval in seconds to scan for the button.",
    )
    parser.add_argument(
        "--block_input",
        action="store_true",
        help="Block input during the button click.",
    )
    parser.add_argument(
        "--button_image",
        type=str,
        default="image.png",
        help="Path to the image of the button to be clicked.",
    )
    return parser.parse_args()


# Parse arguments
args = parse_arguments()

# Get the absolute path to the button image in the same directory as the script/executable
SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.argv[0]))
BUTTON_IMAGE = os.path.join(SCRIPT_DIR, args.button_image)
SCAN_INTERVAL = args.scan_interval
BLOCK_INPUT = args.block_input


def block_input(block: bool):
    """
    Blocks input from the mouse and keyboard using the BlockInput function from user32.dll.
    This function blocks input from the mouse and keyboard to prevent interference with the script.
    """
    try:
        ctypes.windll.user32.BlockInput(block)
        if block:
            print(f"[{timestamp()}] Input blocked.")
        else:
            print(f"[{timestamp()}] Input unblocked.")
    except OSError as e:
        print(f"[{timestamp()}] block_input() - WinError: {e}")


def click_button():
    """
    Simulates a button click by locating the button on the screen,
    clicking it, and then restoring the mouse position and window focus.
    """
    try:
        # Save the current mouse position
        original_position = pyautogui.position()
        # Get the currently active window
        active_window = gw.getActiveWindow()

        # Locate the button on the screen
        location = pyautogui.locateOnScreen(BUTTON_IMAGE, confidence=0.8)
        if location:
            # Block input to prevent interference with the script if enabled
            if BLOCK_INPUT:
                block_input(True)

            # Get the center of the button
            center = pyautogui.center(location)
            # Move to the center of the button and click
            pyautogui.click(center)
            print(f"[{timestamp()}] Button clicked!")

            # Return the cursor to its original position
            pyautogui.moveTo(original_position)

            # Restore focus to original window
            if active_window:
                print(f"[{timestamp()}] Restoring focus to {active_window.title}")
                active_window.activate()

            # Unblock input after clicking the button
            if BLOCK_INPUT:
                block_input(False)
        else:
            print(f"[{timestamp()}] Button not found.")
    except pyautogui.ImageNotFoundException:
        pass  # Ignore the exception if the button is not found
    except pyautogui.FailSafeException as e:
        print(f"[{timestamp()}] Fail-safe triggered: {e}")
    except pyautogui.PyAutoGUIException as e:
        print(f"[{timestamp()}] PyAutoGUIException triggered: {e}")
    except Exception as e:
        print(f"[{timestamp()}] Unexpected error: {e}")


def timestamp():
    """Returns the current timestamp as a formatted string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def signal_handler(sig, frame):
    """
    Handles termination signals to safely exit the script.
    """
    print(f"\n[{timestamp()}] Termination signal received. Exiting gracefully...")
    if BLOCK_INPUT:
        block_input(False)  # Ensure input is unblocked before exiting
    sys.exit(0)


# Register the signal handler for graceful shutdown
signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

# Main loop
if __name__ == "__main__":
    print(f"[{timestamp()}] Starting ButtonClicker script. Press Ctrl+C to exit.")
    while True:
        click_button()
        time.sleep(
            SCAN_INTERVAL
        )  # Wait SCAN_INTERVAL seconds before looking for the button again
