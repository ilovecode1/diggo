############################################################################################################################
#
#                               PyLaunch 1.1.7 the new smart launch for Diggo
#                                        & Pylaunch API 0.1
#
############################################################################################################################

try:
   from Diggo2D import *
   import sys
   import time
   import os
   
except:
    print("A Needed Module does not exist!")
    time.sleep(2)
    sys.exit()

def idleorcommandline():
   'If idleorcommandline returns True its IDLE if False its command line!'
   a = sys.executable
   m = '\\'
   m = m[0]
   while True:
       b = len(a)
       c = a[(b - 1)]
       if c == m:
           break
       a = a[:(b - 1)]
   if sys.executable == a + 'pythonw.exe':
       return True
   else:
       return False

def osfinder():
   'returns os name'
   if os.name == "posix":
       return("posix")
       
   elif os.name in ("nt"):
       return("nt")

   elif os.name in ("dos"):
       return("dos")
       
   elif os.name in ("ce"):
       return("ce")
   else:
      return("fail")
   
def game():

   print("Activating PyLaunch 1.0...")
   time.sleep(2)
   ioc = idleorcommandline()
   if ioc == True:
       print('Running in Python IDLE but, Diggo works best in terminal!')
   else:
       print('Running in Command line')
   time.sleep(1)
   print("Warning if there is a code problem game will not start!")
   time.sleep(3)
   os = osfinder()
   if os == "posix":
       print("OS name posix.")
       time.sleep(2)
       
   elif os == ("nt"):
       print("OS name nt")
       time.sleep(2)

   elif os == ("dos"):
       print("OS name dos")
       time.sleep(2)
       
   elif os == ("ce"):
       print("OS name ce")
       time.sleep(2)

   else:
       print("Your OS does not work with Pylaunch 1.0 nor Diggo!")
       time.sleep(3)
       sys.exit()

   if (DIRT == 0):
       if (GRASS == 1):
           if (WATER == 2):
               if (COAL == 3):
                   if (LAVA == 4):
                       if (TNT == 5):
                           if (red == 255,0,0):
                               if (green == 0,255,0):
                                   if (blue == 0,0,255):
                                       if (BLACK == (0,0,0)):
                                           if (BROWN == (153,76,0)):
                                               if (GREEN == (0,255,0)):
                                                   if (BLUE == (0,0,255)):
                                                       print("No problems starting program...")
                                                       time.sleep(1)
                                                       main()
                                                       print("Shutting Down...")
                                                       time.sleep(2)
                                                       print("Bye!")
                                                       time.sleep(2)
  


print("This Program is made with PyLaunch 1.0 API!")
if __name__ == '__main__':
   game()
