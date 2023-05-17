#create a program that prints a random sentence and calculates the users typed words per minute
#pass through functions stdscr to gain access to the screen and access functions that write on the screen using the curses module

import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    #program will wait for user input before exiting
    stdscr.getkey()


def display_text(stdscr, current, target, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        #store each character in target text
        correct_char = target[i]
        #default color of character / reference pairing
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        #display    
        stdscr.addstr(0, i, char, color)

#import random text from file
def load_text():
    #open in 'r' mode (readmode), you can open a file in 'w' mode (writemode) to write onto text file
    #context manager that ensures the file will be closed after being opened 'with' 
    #'f' is the file object and accessible inside of 'with'
    #readlines gives a list of all lines in the file to return back into the program
    with open("random.txt","r") as f:
        lines = f.readlines()
        #will choose one random line from text file, .strip gets rid of any whitespace characters
        return random.choice(lines).strip()


def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    #stores current time 
    start_time = time.time()
    #do not delay waiting for the user to enter a key
    stdscr.nodelay(True) 

    
    while True: 
        #if the time elapsed is below 1, the default time elapsed will be 1 to avoid diving by zero error as a default 
        time_elapsed = max(time.time() - start_time, 1)

        #average word length of 5 characters
        wpm = round((len(current_text)/ (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, current_text, target_text, wpm)
        stdscr.refresh()

        #convert list for current text to a string to compare to target text
        #.join takes a list as an argument and call it on an empty string
        #combines every character with the empty string (delimiter or septerator)
        if "".join(current_text) == target_text:
            #want to wait for user to hit a key to indicate they are complete.
            #If nodelay is still true, the computer will not wait for the user to enter and an error will occur
            stdscr.nodelay(False)
            break

        #blocker - program will wait for user input before exiting - will throw an exception(error) if user does not enter a key because of no delay
        #if the program throws an exception(error) for no key press, the program will 'except' and continue by going back to the beginning of the while loop
        try: 
            key = stdscr.getkey()
        except: 
            continue

        #check ASCII value of character for exit
        if ord(key) == 27:
            break

        #if user hits the backspace key, remove the last character input to avoid text errors
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        #user can only add more text to list if the length is less than target text to avoid index error to ensure you are not typing more than the target text
        elif len(current_text) < len(target_text):
            current_text.append(key)

        
        

def main(stdscr):
   
    #pairing with a forecolor green and background color white represented by the ID 1
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    #call functions
    start_screen(stdscr)

    #while loop for user to play again
    while True:
        wpm_test(stdscr)
        #exit message for user
        stdscr.addstr(2, 0 , "You have completed the text. Press any key to continue... Press EXIT to quit")
        key = stdscr.getkey()

        #check ASCII value for escape key
        if ord(key) == 27:
            break

    
  
#takes main function and runs it through the wrapper function that executes attributes related to the curses module
wrapper(main)

