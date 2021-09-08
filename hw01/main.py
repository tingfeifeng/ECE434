#! /usr/bin/env python
import curses

mark = 'x'

def main(stdscr):
    stdscr.addstr("Welcome to the game! Use WASD for control, q to quit, and c to clear\nPress any key to continue")
    ch = stdscr.getch()
    stdscr.clear()
    height, width = stdscr.getmaxyx()
    x = 0
    y = 0

    while(1):
        stdscr.addstr(y, x, mark)
        stdscr.move(y, x)
        ch = stdscr.getch()
        if (ch == ord('q')):
            break;
        elif (ch == ord('w') and y > 0):
            y = y - 1
        elif (ch == ord('s') and y < height-1):
            y = y + 1
        elif (ch == ord('a') and x > 0):
            x = x - 1
        elif (ch == ord('d') and x < width-1):
            x = x + 1
        elif (ch == ord('c')):
              stdscr.clear()
              y = 0
              x = 0


curses.wrapper(main)
