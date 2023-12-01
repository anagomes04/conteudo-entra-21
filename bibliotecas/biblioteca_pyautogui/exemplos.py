import pyautogui
# pyautogui.mouseInfo()
pyautogui.PAUSE = 2
pyautogui.hotkey('win', 'd')
lixeira = pyautogui.locateOnScreen('lixeira2.png')
pyautogui.rightClick(lixeira)
pyautogui.click(116,139)
pyautogui.press('enter')
