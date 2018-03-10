# importing PyAutoGui
import pyautogui as pg
import time

# Setting failsafe precaution
pg.PAUSE = 2
pg.FAILSAFE = True

# To open chrome
pg.hotkey('win','d')
time.sleep(.05)
pg.hotkey('win')
pg.typewrite('chrome', interval = 0.2)
pg.hotkey('enter')

# Entereing website details 
pg.typewrite('http://10.0.0.4:8081/PUMIS/', interval = 0.1)
pg.hotkey('enter')

# Maximizing the window
pg.hotkey('alt','space')
pg.press('down', presses = 5)
pg.hotkey('enter')

# Selecting the student section of the website
pos = pg.locateOnScreen(r'C:\Users\malga\Desktop\Projects\PyAutoGui\img\student.png')
x,y = pg.center(pos)
pg.moveTo(x, y, duration = 2)
pg.click(x, y)
time.sleep(3)

# Entering your credentials, replace X's with your username and password
pg.typewrite('XXXXXXXXXXXX', interval = 0.5)
pg.hotkey('tab')
pg.typewrite('XXXXXXX', interval = 0.5)
pg.hotkey('enter')
time.sleep(3)

# Checking actual attendance 
pos = pg.locateOnScreen(r'C:\Users\malga\Desktop\Projects\PyAutoGui\img\academic.png')
x,y = pg.center(pos)
pg.moveTo(x, y, duration = 2)
pos = pg.locateOnScreen(r'C:\Users\malga\Desktop\Projects\PyAutoGui\img\attend.png')
x,y = pg.center(pos)
pg.moveTo(x, y, duration = 2)
pg.click(x, y)
time.sleep(20)

# Logging out
pos = pg.locateOnScreen(r'C:\Users\malga\Desktop\Projects\PyAutoGui\img\hi.png')
x,y = pg.center(pos)
pg.moveTo(x, y, duration = 2)
pos = pg.locateOnScreen(r'C:\Users\malga\Desktop\Projects\PyAutoGui\img\logout.png')
x,y = pg.center(pos)
pg.moveTo(x, y, duration = 2)
pg.click(x, y)







