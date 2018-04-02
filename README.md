# AutoAttendance Checker
This is a script that will automatically check your college attendance on PUMIS for Parul University students.
# Installastion 
1. Install Python 3.6 [here](https://www.python.org/downloads/release/python-364/).

2. Install PyAutoGui using [this](https://github.com/asweigart/pyautogui/blob/master/README.md) tutorial.

# Use
1. After Python and PyAutoGui are installed, make sure you have a Chrome installled on your computer. If not then you can [download](https://www.google.com/chrome/) it. Alternatively, you can replace `pg.typewrite('chrome', interval = 0.2)` with a `pg.typewrite('**Your browser choice**', interval = 0.2)`i.e for <br>- Microsoft Edge, `pg.typewrite('edge', interval = 0.2)` will work. <br>- Firefox, `pg.typewrite('firefox', interval = 0.2)` will work.<br>   
Currently only these browsers on the Windows OS are supported.<br><br>
`interval` is the amount of time it will take for each letter to typed, add a lower value to make the typing faster and a higher one to make it slower. I used `interval = 0.2` as it is more realistic.
            


2. Edit your 12 digit enrollment number here (*This is the number that appears on your Id Card*) e.g 170303105785
`pg.typewrite('XXXXXXXXXXX', interval = 0.5)` <br>and your PUMIS password here
`pg.typewrite('XXXXXXX', interval = 0.5)`


3. Output


4. The paramaters in the `time.sleep()` function depend on the speed of your interent. You can change the values as you wish.

# Precaustions
- Keep FAILSAFE = True as in case any problem arises then you just drag your cursor to the top left and the program will raise an exception.

**N.B:** Refer to [documentation](http://pyautogui.readthedocs.io/en/latest/) should you face any trouble.
