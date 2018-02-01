import pyautogui as pg
import time

pg.PAUSE = 2
pg.FAILSAFE = True

pg.hotkey('win','d')
time.sleep(.05)
pg.hotkey('win')
pg.typewrite('chrome', interval = 0.2)
pg.hotkey('enter')
pg.typewrite('http://10.0.0.4:8081/PUMIS/', interval = 0.1)
pg.hotkey('enter')
pg.hotkey('alt','space')
pg.press('down', presses = 5)
pg.hotkey('enter')
pos = pg.locateOnScreen(r'C:\Users\malga\Desktop\Projects\PyAutoGui\img\student.png')
x,y = pg.center(pos)
pg.moveTo(x, y, duration = 2)
pg.click(x, y)
<<<<<<< HEAD
<<<<<<< HEAD
time.sleep(3)
pg.typewrite('150303105160', interval = 0.5)
pg.hotkey('tab')
pg.typewrite('8581', interval = 0.5)
=======
time.sleep(40)
pg.typewrite('XXXXXXXXXXXX', interval = 0.5)
pg.hotkey('tab')
pg.typewrite('XXXXXXX', interval = 0.5)
>>>>>>> cd775571ae807706a826690fcea369727ed1976c
=======
time.sleep(40)
pg.typewrite('XXXXXXXXXXXX', interval = 0.5)
pg.hotkey('tab')
pg.typewrite('XXXXXXX', interval = 0.5)
>>>>>>> cd775571ae807706a826690fcea369727ed1976c
pg.hotkey('enter')
time.sleep(3)
pos = pg.locateOnScreen(r'C:\Users\malga\Desktop\Projects\PyAutoGui\img\academic.png')
x,y = pg.center(pos)
pg.moveTo(x, y, duration = 2)
pos = pg.locateOnScreen(r'C:\Users\malga\Desktop\Projects\PyAutoGui\img\attend.png')
x,y = pg.center(pos)
pg.moveTo(x, y, duration = 2)
pg.click(x, y)
time.sleep(20)
pos = pg.locateOnScreen(r'C:\Users\malga\Desktop\Projects\PyAutoGui\img\hi.png')
x,y = pg.center(pos)
pg.moveTo(x, y, duration = 2)
pos = pg.locateOnScreen(r'C:\Users\malga\Desktop\Projects\PyAutoGui\img\logout.png')
x,y = pg.center(pos)
pg.moveTo(x, y, duration = 2)
pg.click(x, y)







