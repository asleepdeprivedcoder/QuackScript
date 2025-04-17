#No disclaimer, have fun!
import time
import usb_hid
import board
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

# Initialize keyboard and layout
keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Wait for a moment to switch to the target window
time.sleep(0.1)

# Open the Run dialog (Windows + R)
keyboard.press(Keycode.WINDOWS)
keyboard.press(Keycode.R)
keyboard.release_all()

# Wait for the Run dialog to open
time.sleep(1)

# Type the URL
Prompt = "https://www.youtube.com/watch?v=xvFZjo5PgG0"
layout.write(Prompt)

# Press Enter to open the URL
keyboard.press(Keycode.ENTER)
keyboard.release_all()

# Wait for page to load
time.sleep(2)

# Press Space to play video
keyboard.press(Keycode.SPACE)
keyboard.release_all()
