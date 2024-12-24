import pyautogui 
from time import sleep

pyautogui.click(1041,15, duration=1) #(1041, 15) clica em uma determina coordenada, click at the specified coordinates
pyautogui.click(567,187, duration=1)
pyautogui.click(549,240, duration=1)
pyautogui.write('Esse post foi feito automaticamente por um script de Python. \nUsando a biblioteca pyautogui.', interval=0.25)
pyautogui.click(1357,726, duration=0.5)
sleep(1)
    