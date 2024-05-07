import pyautogui as pg
import keyboard

keyboard.wait('g')
pg.PAUSE = 3

while True:    
    pg.press('F11')
    pg.click(x=910, y=446)

# print(pg.position())