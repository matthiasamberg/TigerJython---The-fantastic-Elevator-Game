import globalvars
from gamestate import *
import random

direction = "up"
def play():
    global direction #diese Variable ist 'global' d.h. überall im Programm zugreifbar.
    
    if direction == "up":
        naechsterStock = getCurrentFloor() + 1
    
    setElevatorDestination(naechsterStock)


    

#------------ bitte drin lassen (aber anderweitig ignorieren
execfile ("functions.py")
