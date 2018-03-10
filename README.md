# AutoAttendance Checker
# Installastion 
1. Install Python 3.6 [here](https://www.python.org/downloads/release/python-364/).

2. Install PyAutoGui using [this](https://github.com/asweigart/pyautogui/blob/master/README.md) tutorial.

# Use
1. After Python and PyAutoGui are installed, make sure you have a Chrome installled on your computer. If not then you can [download](https://www.google.com/chrome/) it. Alternatively, you can replace `pg.typewrite('chrome', interval = 0.2)` with a `pg.typewrite('**Your browser choice**', interval = 0.2)
` 

2. Edit your enrollment number here
`pg.typewrite('XXXXXXXXXXXX', interval = 0.5)
`

and password here
`pg.typewrite('XXXXXXX', interval = 0.5)
`

3. The paramaters in the time.sleep() function depend on the speed of your interent. You can change the values as you wish.

# Precaustions
- Keep FAILSAFE = True as in case any problem arises then you just drag your cursor to the top left and the program will raise an exception.

**N.B:** Refer to [documentation](http://pyautogui.readthedocs.io/en/latest/) should you face any trouble.
