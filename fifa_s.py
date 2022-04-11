import pyautogui
import time
import pydirectinput
import random
import keyboard

print('F3 시작 / F4 중지 (멈출 때 까지 눌러주세요)')

while True:
    if keyboard.is_pressed('F3'): #F3 시작
        while True:
            if keyboard.is_pressed('F4'): #F4 중지
                break
            else:
                time.sleep(random.randint(1, 2))
                pydirectinput.keyDown("s")
                time.sleep(0.25)
                pydirectinput.keyUp("s")
                pydirectinput.keyDown("space")
                time.sleep(0.25)
                pydirectinput.keyUp("space")
                pydirectinput.keyDown("s")
                time.sleep(0.25)
                pydirectinput.keyUp("s")
                pydirectinput.keyDown("space")
                time.sleep(0.25)
                pydirectinput.keyUp("space")
                pydirectinput.keyDown("s")
                time.sleep(0.25)
                pydirectinput.keyUp("s")
                pydirectinput.keyDown("space")
                time.sleep(0.25)
                pydirectinput.keyUp("space")
                pydirectinput.keyDown("esc")
                time.sleep(0.25)
                pydirectinput.keyUp("esc")


