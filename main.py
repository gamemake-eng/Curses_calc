import curses
import sys
from curses.textpad import Textbox, rectangle
def main(scr):
    d = ""
    ans=0
    i = 0
    cols = [[curses.COLOR_GREEN, curses.COLOR_WHITE], [curses.COLOR_RED]]
    curses.init_pair(3,curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.init_pair(2,curses.COLOR_RED, curses.COLOR_WHITE)
    while True:
        curses.init_pair(1,cols[i][0],cols[0][1])
        scr.clear()
        curses.start_color()
        scr.addstr(0,0,'ENTER A CALCULATION "Ctrl-G to enter"', curses.color_pair(1))
        scr.addstr(1,0,d,curses.color_pair(3))
        edit = curses.newwin(60,60,2,0)
        
        scr.refresh()

        box= Textbox(edit)
        box.edit()

        e = box.gather()
        try:
            a = eval(e)
            d="Ans: {}".format(a)
            ans=a
            i=0
        except Exception as e:
            curses.beep()
            scr.clear()
            
            scr.addstr(0,0,"ERR: "+str(e)+"\n\nPRESS ANY KEY TO CONTINUE",curses.color_pair(2))
            scr.getkey()
            i=1
        



curses.wrapper(main)
