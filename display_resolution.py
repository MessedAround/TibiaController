# Imports
from inputs import get_gamepad
import pyautogui

# Check Resolution
def resolution():
    print('[TibiaController] State: Checking Resolution')
    while True:
        events = get_gamepad()
        for event in events:
            if event.code == "BTN_SOUTH" and event.state == 1:
                print(pyautogui.position())

# Startup
if __name__ == "__main__":
    resolution()