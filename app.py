import pyautogui
from time import sleep

#Abrir o Visual Studio Code
pyautogui.press('win')
sleep(0.5)
pyautogui.write('vscode')
sleep(0.5)
pyautogui.press('enter')
sleep(1)

#Por a musica pra tocar
pyautogui.press('win')
pyautogui.write('spotify')
pyautogui.press('enter')
sleep(5)
pyautogui.click(800, 795, duration=1)
sleep(1)

#Abrir o WhatsAPP
pyautogui.press('win')
sleep(0.5)
pyautogui.write('whatsapp')
sleep(0.5)
pyautogui.press('enter')
sleep(2)
pyautogui.hotkey('win', 'm')

#Abrir o Chrome
pyautogui.hotkey('win', 'r')
sleep(0.5)
pyautogui.write('chrome')
sleep(0.5)
pyautogui.click(170,810, duration=0.3)
sleep(3)
pyautogui.hotkey('ctrl', 'shift', 't')
sleep(5)

#Fechar o Chrome Vazio
pyautogui.hotkey('alt', 'tab')
sleep(0.5)
pyautogui.hotkey('alt', 'f4')