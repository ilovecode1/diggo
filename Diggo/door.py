#door.py

def read():

    try:
         import pygame
    except ImportError:
        print("Module pygame does not exist!")
        sys.exit()
    try:
         import sys
    except ImportError:
        print("Module sys does not exist!")
        sys.exit()
    try:
         import pygame.locals
    except ImportError:
        print("Module pygame.locals does not exist!")
        sys.exit()
    try:
         import random
    except ImportError:
        print("Module random does not exist!")
        sys.exit()
  
    try:
        # for Python2
        from Tkinter import *   ## notice capitalized T in Tkinter 
    except ImportError:
        # for Python3
        from tkinter import *
    try:
        import dumbmenu
    except ImportError:
        print("Module dumbmenu does not exist!")
        sys.exit()
    try:
        import time
    except ImportError:
        print("Module time does not exist!")
        sys.exit()
    try:
        import os
        from os.path import exists
    except ImportError:
            print("Module os does not exist!")
            sys.exit()
    print("door load complete!")
