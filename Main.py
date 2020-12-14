import globalvars
from gamestate import *
import random


# das ist der Code aus Beispiel3.py
# Der Lift fährt zufällig irgend ein Stockwerk an

def play():
   obersterStock = getNumFloors() - 1
   zufaelligerStock = random.randint(0, obersterStock)
   setElevatorDestination(zufaelligerStock)

   


#------------ bitte drin lassen (aber anderweitig ignorieren)
execfile ("functions.py")
