# Captcha Auto Filler Programm
# Credits- Rudra Shah
# Instagram Handle- @rudra_shah_

# This is just an sample script improvements will be added later.

# It is also possible iwth selenium

# Instruction before using:
"""
* Just Run this programm and switch to captcha page...Boom You computer is now under the control and will help you to fill all the captcha with 99% Accuracy.
* Don't forget to add your cordinates of captcha before starting the Programm!
* Before using this project for commercial means credits of owner is required to 
  be mentioned in that project else copyright claim can be made regards having MIT License. 
  MIT License is used for this open source project is not liable for any of causes. 
  The owner isn't responsible for any cause. This project is designed to show what CV i.e Text Recognition library can you do.
"""
import pytesseract
import pyautogui
import pyscreenshot
import time
import os
i = 0
last = ""
# Insert your co-ordinates of the box of captch as x1,y1,x2,y2
x1 = 0
y1 = 0
x2 = 0
y2 = 0
time.sleep(5)
while True:
    i+=1
    time.sleep(4.7)
    img = pyscreenshot.grab(bbox=(x1, y1, x2, y2))
    s = "cap{}.png".format(str(i))
    img.save(s)
    text = pytesseract.image_to_string(s)
    if(len(str(text))!=8):
        os.remove(s)
        break
    if(last!=text):
        print(text)
        time.sleep(1)
        pyautogui.click(704,504) # Enter your click cordinates here
        pyautogui.click(704,504)
        time.sleep(1)
        pyautogui.typewrite(text,0.5)
        time.sleep(0.3)
        pyautogui.keyDown("enter")
        time.sleep(1)
        last = text
        os.remove(s)
