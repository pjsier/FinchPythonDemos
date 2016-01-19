from lib.finch import Finch
import curses
from time import sleep

#Initalize finch
myFinch = Finch()

"""
Control Finch with keys
"""

# Initialize the library. Return a WindowObject which represents the whole screen.
window = curses.initscr()
curses.cbreak()
window.keypad(1)

window.addstr(0, 0, "Hit 'q' to quit")
window.move(2, 0)
window.refresh()

key = ''
while key != ord('q'):
    key = window.getch()
    window.addch(2, 0, key)
    window.refresh()

    if key == curses.KEY_UP:
        window.clrtobot()
        window.addstr(2, 0, "Finch goes forward!")
        myFinch.wheels(1, 1)
        sleep(0.1)
        myFinch.halt()

    elif key == curses.KEY_DOWN:
        window.clrtobot()
        window.addstr(2, 0, "Finch goes backwards!")
        myFinch.wheels(-1, -1)
        sleep(0.1)
        myFinch.halt()

    elif key == curses.KEY_LEFT:
        window.clrtobot()
        window.addstr(2, 0, "Finch goes left!")
        myFinch.wheels(0, 1)
        sleep(0.1)
        myFinch.halt()

    elif key == curses.KEY_RIGHT:
        window.clrtobot()
        window.addstr(2, 0, "Finch goes right!")
        myFinch.wheels(1, 0)
        sleep(0.1)
        myFinch.halt()

curses.endwin()

#Close connection with finch
myFinch.close()
