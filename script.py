import pytesseract
from PIL import Image
import os

a = 0

# Path to the Teressac Python library executable file 
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Image given with text
img = Image.open('d:/Users/User/Desktop/Images/image.png')

# Image converted to text
text = pytesseract.image_to_string(img)

# String to char
text_char = [char for char in text]

print(text_char)

# Open a VBS file for writing mode
f1 = open('d:/Users/User/Desktop/VBS/vbs_file.vbs','w')
f1.write('set wshshell = wscript.CreateObject("wScript.Shell")\n')
f1.write('WScript.Sleep 1000\n')

# Handling text to VBScript
for char in text_char:
    if a == 0:
        if char == ' ':
            f1.write('wshshell.sendkeys " "\n')
        elif char == '\n':
            f1.write('wshshell.sendkeys " "\n')
        elif ord(char) == 124:
            f1.write('wshshell.sendkeys "I"\n')
        elif char == '"':
            a = 1
        elif char == '”':
            a = 1
        else:
            f1.write('wshshell.sendkeys "'+ char +'"\n')
    else:
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
            f1.write('wshshell.sendkeys "'+ t +'""'+'\n')
            t = '""'
        
    f1.write('WScript.Sleep 1\n')
            
f1.close()

# VBScript file execution
os.startfile("d:/Users/User/Desktop/Python/a.vbs")





