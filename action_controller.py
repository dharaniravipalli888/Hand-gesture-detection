import pyautogui
import os
from datetime import datetime

# -----------------------------
# PyAutoGUI Settings
# -----------------------------
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.1

# -----------------------------
# Screenshot Folder
# -----------------------------
SCREENSHOT_FOLDER = "screenshots"
os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)


def perform_action(label):
    """
    Perform system action based on detected gesture.
    """

    # Current mouse position
    x, y = pyautogui.position()

    # -----------------------------
    # Palm -> Screenshot
    # -----------------------------
    if label == "01_palm":

        filename = datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"

        filepath = os.path.join(SCREENSHOT_FOLDER, filename)

        pyautogui.screenshot(filepath)

        print("Screenshot Saved")


    # -----------------------------
    # Fist -> Left Click
    # -----------------------------
    elif label == "02_fist":

        pyautogui.click()

        print("Mouse Left Click")


    # -----------------------------
    # Thumbs Up -> Volume Up
    # -----------------------------
    elif label == "03_thumbs-up":

        pyautogui.press("volumeup")

        print("Volume Increased")


    # -----------------------------
    # Thumbs Down -> Volume Down
    # -----------------------------
    elif label == "04_thumbs-down":

        pyautogui.press("volumedown")

        print("Volume Decreased")


    # -----------------------------
    # Index Right -> Move Right
    # -----------------------------
    elif label == "05_index-right":

        pyautogui.moveTo(x + 50, y, duration=0.1)

        print("Cursor Right")


    # -----------------------------
    # Index Left -> Move Left
    # -----------------------------
    elif label == "06_index-left":

        pyautogui.moveTo(x - 50, y, duration=0.1)

        print("Cursor Left")


    # -----------------------------
    # No Gesture
    # -----------------------------
    elif label == "07_no-gesture":

        print("No Gesture")


    # -----------------------------
    # Unknown Gesture
    # -----------------------------
    else:

        print("Unknown Gesture:", label)