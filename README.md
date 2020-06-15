# TibiaController

Play Tibia (https://www.tibia.com/) using a controller! Great for relaxed beastiary farming or levelling a new character while sitting on your couch.

This is modified version of zooyl's TibiaController python script found on his github page: https://github.com/zooyl/TibiaController

## FAQ

Q1. Does it interfere with BattlEye?
A1. No, it does not interfere with BattlEye.

Q2. Will I get banned using this?
A2. No, as stated in A1, it does not interfere with BattlEye at all so there is no reason for you to get banned. However, to cover myself I take no responsibility should you happen to get banned using it.

Q3. What controllers are support?
A3. Xbox 360 and Xbox One

Q4. Will you add Playstation controller support?
A4. No. I don't have any Playstation controllers to do this.

## Installation

1. Install python (https://www.python.org/downloads/)
	- Make sure you add python to PATH (tickbox at bottom of installer before clicking 'install now')
2. Run install_requirements.bat to install all the required packages from requirements.txt
	- Optionally you can install it manually.
	
## Default Controller Configuration

B			= Main/Battle Mode Swap
X			= F1
A			= F2
Y			= F3 (Battle) & Ctrl (Main)
RB			= F4 (Battle) & PgUp (Main)
RT			= F5 (Battle) & PgDn (Main)
LB			= F6 (Battle) & Home (Main)
LT			= F7 (Battle) & End  (Main)
Dpad Up		= Walk North
Dpad Right	= Walk East
Dpad Down	= Walk South
Dpad Left	= Walk West
Right Stick	= Nothing
Left Stick	= Nothing (tibia_controller_dpad) & Walk North, East, South and West (tibia_controller_stick.py)
Start		= Spacebar (target creature)
Select		= Left Click (loot creature)

## Using TibiaController

1. Run command prompt as administrator.
	You can do this by pressing start and typing cmd then right-click on it and click on run as administrator.
		OR
	You can press start and type cmd then shift + left click on it.
2. Navigate to the folder location in command prompt.
	i.e. cd C:\Users\Username\Documents\TibiaController\
3. Enter the following:
		python tibia_controller_dpad.py
4. Press enter and if your controller is detected you will see the following:
	[TibiaController] State: Main
5. You can now use your controller for Tibia.

## Credits

zooyl
	Original TibiaController python script
CipSoft GmbH
	Tibia MMORPG