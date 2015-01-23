from finch_api import Finch
import curses
from time import sleep

#Initalize finch
finch = Finch()

"""
Control Finch with keys
"""

#Flash light to let user know it's their turn
for x in range(1,2):
    finch.led(255,255,255)
    sleep(0.5)
    finch.led(0,0,0)
    sleep(0.5)

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr(0,10,"Hit 'q' to quit")
stdscr.refresh()

key = ''
while key != ord('q'):
    key = stdscr.getch()
    stdscr.addch(20,25,key)
    stdscr.refresh()

    if key == curses.KEY_UP: 
        stdscr.addstr(1, 20, "Finch goes forward!")
        finch.wheels(1,1)
        sleep(0.1)
        finch.halt()
    elif key == curses.KEY_DOWN: 
        stdscr.addstr(1, 20, "Finch goes backwards!")
        finch.wheels(-1,-1)
        sleep(0.1)
        finch.halt()
    elif key == curses.KEY_LEFT:
    	stdscr.addstr(1, 20, "Finch goes left!")
        finch.wheels(0,1)
        sleep(0.1)
        finch.halt()
    elif key == curses.KEY_RIGHT:
    	stdscr.addstr(1, 20, "Finch goes right!")	
        finch.wheels(1,0)
        sleep(0.1)
        finch.halt()

curses.endwin()

#Close connection with finch
finch.close()