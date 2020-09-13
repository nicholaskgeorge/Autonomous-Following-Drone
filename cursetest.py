import curses
import ascii
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()

while True:
    stdscr.getch()
    if stdscr.getch()==119:
        print("up")
    if stdscr.getch()==97:
        print("left")
    if stdscr.getch()==115:
        print("down")
    if stdscr.getch()==100:
        print("right")
