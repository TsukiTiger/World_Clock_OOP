from tkinter import *
from Clock import Clock
import time

window = Tk()
window.geometry("250x310")
window.title("World Clock")

clock0 = Clock(window, "America", "Los_Angeles", 0)
clock1 = Clock(window, "Asia", "Hong_Kong", 1)
clock2 = Clock(window, "Europe", "London", 2)


def updateTime():
    clock0.updateTime()
    clock1.updateTime()
    clock2.updateTime()


while True:
    updateTime()
    window.update_idletasks()
    window.update()
    time.sleep(0.1)