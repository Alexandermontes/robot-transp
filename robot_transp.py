import pandas as pd
import random
import os
import pyautogui
import pyperclip
import time

time.sleep(1)
pyautogui.hotkey('alt','tab')
time.sleep(1)
pyautogui.typewrite('LM01')
pyautogui.hotkey('enter')
time.sleep(2)
pyautogui.typewrite('2')
pyautogui.hotkey('enter')

for n in range(15):
    time.sleep(2)
    pyautogui.typewrite('3')
    pyautogui.hotkey('enter')
    time.sleep(15)
    pyautogui.typewrite('0004')
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')
    time.sleep(1)
    tienda=['P172', 'P184',	'P187',	'P190',	'P193',	'P196',	'P203',	'P206',	'P215',	'P221',	'P230',	'P235',	'P237',	'P238',	'P239','P241',	'P242',	'P243',	'P245',	'P247',	'P254',	'P255',	'P256',	'P268',	'P269']
    ubic = random.choice(tienda)
    pyautogui.typewrite(ubic)
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('tab')
    time.sleep(1)
    pyautogui.typewrite('7')
    time.sleep(1)
    pyautogui.hotkey('tab')

    df1=pd.read_excel('E:/SET_DATOS/trans/materiales.xls', sheet_name='Hoja1')
    columna1=df1.iloc[:,9]
    for i in range(0,len(columna1)):
        dato = int(columna1[i])
        pyperclip.copy(str(dato))
        time.sleep(1)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.hotkey('enter')
        time.sleep(1)
        if i>5:
            break

    time.sleep(2)
    pyautogui.hotkey('f5')
    time.sleep(1)
    pyautogui.hotkey('f1')

    time.sleep(20)
    pyautogui.hotkey('shift','tab')
    pyautogui.hotkey('shift','tab')
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.moveTo(19,216)
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey('shift','tab')
    pyautogui.hotkey('shift','tab')
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('shift','tab')
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.moveTo(19,306)
    pyautogui.click()
    time.sleep(1)
    pyautogui.hotkey('shift','tab')
    pyautogui.hotkey('shift','tab')
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('tab')
    pyautogui.typewrite('1')
    time.sleep(1)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('enter')
    time.sleep(15)
    pyautogui.hotkey('f3')


'''
path ="C:\\Program Files (x86)\\SAP\\FrontEnd\\SapGui\saplogon.exe"
os.startfile(path)

time.sleep(5)
pyautogui.hotkey('alt','space')
time.sleep(1)

pyautogui.typewrite('x')
pyautogui.moveTo(600,340,duration=2)
pyautogui.doubleClick()
time.sleep(2)
pyautogui.typewrite('omontes')
pyautogui.hotkey('tab')
pyautogui.typewrite('Om500808')
pyautogui.moveTo(20,50,duration=2)
pyautogui.click()
time.sleep(1)
pyautogui.hotkey('enter')
time.sleep(1)
pyautogui.typewrite('IW28')
pyautogui.moveTo(20,50,duration=2)
pyautogui.click()
time.sleep(2)
pyautogui.hotkey('f8')
time.sleep(2)
pyautogui.moveTo(50,180,duration=2)
pyautogui.hotkey('ctrl', 'y')
pyautogui.dragTo(300, 600, duration=2 )
pyautogui.hotkey('ctrl', 'c')

path    ="C:\\Program Files (x86)\\Microsoft Office\\Office14\\OUTLOOK.exe"
os.startfile(path)
time.sleep(3)
pyautogui.hotkey('alt','space')
time.sleep(1)
pyautogui.typewrite('x')
pyautogui.moveTo(25,60,duration=2)
pyautogui.click()
time.sleep(2)
pyautogui.moveTo(70,300,duration=2)
pyautogui.click()
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.hotkey('shift','tab')
pyautogui.hotkey('shift','tab')
pyautogui.hotkey('shift','tab')
pyautogui.typewrite('alexanderabella')
pyperclip.copy("@")
pyautogui.hotkey("ctrl", "v")
pyautogui.typewrite('gmail.com')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.hotkey('tab')
pyautogui.typewrite('avisos de mantenimiento')
pyautogui.moveTo(20,200,duration=2)
pyautogui.click()'''
