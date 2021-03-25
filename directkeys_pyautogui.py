import time
import pyautogui

def countdown(x):
    for i in list(range(x))[::-1]:
        print(i+1)
        time.sleep(1)

def jump():
    pyautogui.keyDown('w')
    print("keyDown Jump")
    time.sleep(1)
    pyautogui.keyUp('w')

def left():
    pyautogui.keyDown('a')
    print("keyDown Left")
    time.sleep(0.6)
    pyautogui.keyUp('a')

def right():
    pyautogui.keyDown('d')
    print("keyDown Right")
    time.sleep(0.6)
    pyautogui.keyUp('d')

def jump_left():
    pyautogui.keyDown('w')
    pyautogui.keyDown('a')
    time.sleep(0.5)
    pyautogui.keyUp('a')
    pyautogui.keyUp('w')

def jump_right():
    pyautogui.keyDown('w')
    pyautogui.keyDown('d')
    time.sleep(0.5)
    pyautogui.keyUp('d')
    pyautogui.keyUp('w')

def reset():
    print("reset")
    pyautogui.keyDown('r')
    pyautogui.keyUp('r')

options = {0 : reset,
           1 : jump,
           2 : left,
           3 : right,
           4 : jump_left,
           5 : jump_right}

'''for i in list(range(10))[::-1]:
    time.sleep(1)
    left()
    time.sleep(0.75)
    right()
    time.sleep(1)
    jump()
    time.sleep(3)
    reset()
'''
