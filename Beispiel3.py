import globalvars
from gamestate import *
import random

def play():
   obersterStock = getNumFloors() - 1
   zufaelligerStock = random.randint(0, obersterStock)
   setElevatorDestination(zufaelligerStock)


    

#------------ bitte drin lassen (aber anderweitig ignorieren
execfile ("functions.py")
