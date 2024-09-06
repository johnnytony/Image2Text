import pytesseract
from PIL import Image
import os
import subprocess
import time

a = 0

# If Tesseract was installed via Homebrew, no path needed
# Uncomment and adjust if needed
# pytesseract.pytesseract.tesseract_cmd = '/usr/local/bin/tesseract'

# Image given with text
img = Image.open('image.png')

# Image converted to text
text = pytesseract.image_to_string(img)

# String to char
text_char = [char for char in text]

print(text_char)

# Open an AppleScript file for writing mode
with open('applescript_file.applescript', 'w') as f1:
    f1.write('delay 1\n')  # Equivalent to WScript.Sleep 1000

    # Handling text to AppleScript
    for char in text_char:
        if a == 0:
            if char == ' ':
                f1.write('tell application "System Events" to keystroke " "\n')
            elif char == '\n':
                f1.write('tell application "System Events" to keystroke " "\n')
            elif ord(char) == 124:  # '|'
                f1.write('tell application "System Events" to keystroke "I"\n')
            elif char == '"':
                a = 1
            elif char == '”':
                a = 1
            else:
                f1.write(f'tell application "System Events" to keystroke "{char}"\n')
        else:
            t = ""
            if char == '\n':
                t += " "
            elif ord(char) == 124:
                t += "I"
            elif char == "”":
                t += '"'
            else:
                t += char

            if char == '"' or char == "”":
                a = 0
                f1.write(f'tell application "System Events" to keystroke "{t}"\n')
        
        f1.write('delay 0.001\n')  # Sleep for 1 ms

# Run the generated AppleScript
subprocess.call(['osascript', 'applescript_file.applescript'])
