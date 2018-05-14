from random import randint
import pyautogui
import time
t=0
def refresh ():
    pyautogui.hotkey('winleft','printscreen')
    for i in range (5):
        pyautogui.click(252,14)
        time.sleep(0.2)
    pyautogui.click(230,50)
    pyautogui.typewrite('https://www.youtube.com/watch?v=jZ9d64ljYrA')
    pyautogui.typewrite(['enter'])
    time.sleep(300)
def comment ():
    x=""
    for i in range (10):
        x=x+chr(randint(97,122))
    pyautogui.click(720,0,button='left')
    pyautogui.moveTo(1429,85)
    pyautogui.mouseDown(button='left')
    time.sleep(5)
    pyautogui.mouseUp(button='left')
    pyautogui.click(584,751,button='left')
    pyautogui.typewrite(x)
    time.sleep(0.5)
    pyautogui.click(900,775,button='left')
while True:
    comment()
    t=t+1
    if t==500:
        refresh()
        t=0
