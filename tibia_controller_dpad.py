# Imports
from inputs import get_gamepad
import pyautogui

# Controller Configuration
btn_select = "BTN_SELECT"
btn_start = "BTN_START"
btn_y = "BTN_NORTH"
btn_x = "BTN_WEST"
btn_a = "BTN_SOUTH"
btn_b = "BTN_EAST"
trigger_power = 200
dpad_x_axis = "ABS_HAT0X"
dpad_y_axis = "ABS_HAT0Y"
btn_lb = "BTN_TL"
btn_rb = "BTN_TR"
btn_lt = "ABS_Z"
btn_rt = "ABS_RZ"
right_stick_x_axis = "ABS_RX"
right_stick_y_axis = "ABS_RY"
left_stick_x_axis = "ABS_X"
left_stick_y_axis = "ABS_Y"

# Main
def main():
    print('[TibiaController] State: Main')
    while True:
        events = get_gamepad()
        for event in events:
            # Character Movement
            if event.code == dpad_x_axis and event.state == 1:
                pyautogui.keyDown('right')
            if event.code == dpad_x_axis and event.state == 0:
                pyautogui.keyUp('right')
            if event.code == dpad_x_axis and event.state == -1:
                pyautogui.keyDown('left')
            if event.code == dpad_x_axis and event.state == 0:
                pyautogui.keyUp('left')
            if event.code == dpad_y_axis and event.state == -1:
                pyautogui.keyDown('up')
            if event.code == dpad_y_axis and event.state == 0:
                pyautogui.keyUp('up')
            if event.code == dpad_y_axis and event.state == 1:
                pyautogui.keyDown('down')
            if event.code == dpad_y_axis and event.state == 0:
                pyautogui.keyUp('down')
            if event.code == btn_lb and event.state == 1:
                pyautogui.press('home')
            if event.code == btn_rb and event.state == 1:
                pyautogui.press('pgup')
            if event.code == btn_rt and event.state > trigger_power:
                pyautogui.press('pgdn')
            if event.code == btn_lt and event.state > trigger_power:
                pyautogui.press('end')
            # Hotkeys
            if event.code == btn_x and event.state == 1:
                pyautogui.press('f1')
            if event.code == btn_a and event.state == 1:
                pyautogui.press('f2')
            if event.code == btn_select and event.state == 1:
                pyautogui.click()
            if event.code == btn_start and event.state == 1:
                pyautogui.press('space')
            # Character Rotation
            if event.code == btn_y and event.state == 1:
                pyautogui.keyDown('ctrl')
            if event.code == btn_y and event.state == 0:
                pyautogui.keyUp('ctrl')
            # Change Modes
            if event.code == btn_b and event.state == 1:
                battle()

# Battle
def battle():
    print('[TibiaController] State: Battle')
    while True:
        events = get_gamepad()
        for event in events:
            # Character Movement
            if event.code == dpad_x_axis and event.state == 1:
                pyautogui.keyDown('right')
            if event.code == dpad_x_axis and event.state == 0:
                pyautogui.keyUp('right')
            if event.code == dpad_x_axis and event.state == -1:
                pyautogui.keyDown('left')
            if event.code == dpad_x_axis and event.state == 0:
                pyautogui.keyUp('left')
            if event.code == dpad_y_axis and event.state == -1:
                pyautogui.keyDown('up')
            if event.code == dpad_y_axis and event.state == 0:
                pyautogui.keyUp('up')
            if event.code == dpad_y_axis and event.state == 1:
                pyautogui.keyDown('down')
            if event.code == dpad_y_axis and event.state == 0:
                pyautogui.keyUp('down')
            # Hotkeys
            if event.code == btn_x and event.state == 1:
                pyautogui.press('f1')
            if event.code == btn_a and event.state == 1:
                pyautogui.press('f2')
            if event.code == btn_y and event.state == 1:
                pyautogui.press('f3')
            if event.code == btn_rb and event.state == 1:
                pyautogui.press('f4')
            if event.code == btn_rt and event.state > trigger_power:
                pyautogui.press('f5')
            if event.code == btn_lb and event.state == 1:
                pyautogui.press('f6')
            if event.code == btn_lt and event.state > trigger_power:
                pyautogui.press('f7')
            if event.code == btn_select and event.state == 1:
                pyautogui.click()
            if event.code == btn_start and event.state == 1:
                pyautogui.press('space')
            # Change Modes
            if event.code == btn_b and event.state == 1:
                main()

# Startup
if __name__ == "__main__":
    main()