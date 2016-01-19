from lib.finch import Finch
import curses
from time import sleep

#Initalize finch
myFinch = Finch()

"""
Control Finch with keys
"""

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0, 10, "Hit 'q' to quit")
stdscr.refresh()

key = ''
padding = " " * 5
while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(20, 25, key)
    stdscr.refresh()

    if key == curses.KEY_UP:
        stdscr.addstr(1, 20, "Finch goes forward!" + padding)
        myFinch.wheels(1, 1)
        sleep(0.1)
        myFinch.halt()
    elif key == curses.KEY_DOWN:
        stdscr.addstr(1, 20, "Finch goes backwards!" + padding)
        myFinch.wheels(-1, -1)
        sleep(0.1)
        myFinch.halt()
    elif key == curses.KEY_LEFT:
    	stdscr.addstr(1, 20, "Finch goes left!" + padding)
        myFinch.wheels(0, 1)
        sleep(0.1)
        myFinch.halt()
    elif key == curses.KEY_RIGHT:
    	stdscr.addstr(1, 20, "Finch goes right!" + padding)
        myFinch.wheels(1, 0)
        sleep(0.1)
        myFinch.halt()

curses.endwin()

#Close connection with finch
myFinch.close()
