import pyautogui
from time import sleep

def posiçao():
    while True:
        sleep(0.3)
        pos = pyautogui.position()
        print(pos)



posiçao()