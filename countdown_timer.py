#!/usr/bin/python3
# Windowed countdown timer
# USAGE: update the duration variable on line 9.
# Author: Raresteak
# https://github.com/raresteak
import time
from tkinter import *
# Countdown timer duration in seconds
duration = 3600


def stopwatch(sec):
    while sec:
        if (sec <= duration/2):
            # Update window color to yellow as warning half time has expired.
            theWindow.configure(bg='yellow')
            theWindow.update()
        if (sec == 1):
            # update window color to red, time is expired
            theWindow.configure(bg='red')
            theWindow.update()
            windowContents = Label(theWindow, text="Time is up!")
            windowContents.pack()
        minn, secc = divmod(sec, 60)
        timeformat = '{:02d}:{:02d}'.format(minn, secc)
        theWindow.title("Time remaining: " + timeformat)
        theWindow.update()
        time.sleep(1)
        sec -= 1


theWindow = Tk()
theWindow.attributes('-topmost', 1)
theWindow.geometry("300x30+680+0")
theWindow.configure(bg='green')
stopwatch(duration)
theWindow.mainloop()