# Import
from inputs import get_gamepad

# Check Controller Codes and States
def controller_code_and_state():
    # Check Inputs
    while True:
        events = get_gamepad()
        for event in events:
            print("[TibiaController] Code: ", event.code, " State: ", event.state)

# Startup
if __name__ == "__main__":
    controller_code_and_state()
