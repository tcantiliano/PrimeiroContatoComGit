import pyautogui
import time

def dropPeixe():
    while True:
        img = pyautogui.locateCenterOnScreen('peixeCliente13.png',confidence=0.5)
        pyautogui.click(img.x, img.y, duration=0.15)

        pyautogui.dragTo(833,396, button='left',duration=0.15, mouseDownUp=True)

    # clicOk = pyautogui.locateCenterOnScreen('btnOk.PNG',confidence = 0.7)
    # pyautogui.click(clicOk.x, clicOk.y,duration=0.5)
dropPeixe()

def pescaria():
    for peixeloot in dropPeixe:
        rod = pyautogui.click(1220,710)
        rodClick = pyautogui.moveTo(1031,394, duration=0.25)
        rodClick_agua = pyautogui.click(rodClick)
        return
pescaria()