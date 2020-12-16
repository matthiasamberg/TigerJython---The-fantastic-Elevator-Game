import globalvars
from gamestate import *
import random


# In diesem Programm gibt es noch einen Fehler:
# Der Lift will immer weiter nach oben fahren, 
# auch wenn er schon zuoberst angelangt ist.
def play():
    naechsterStock = getCurrentFloor() + 1
    
    
    setElevatorDestination(naechsterStock)
   



## Der Ausgangscode als Kopiervorlage:
#def play():
#    naechsterStock = getCurrentFloor() + 1
#    setElevatorDestination(naechsterStock)




#------------ bitte drin lassen (aber anderweitig ignorieren
execfile ("functions.py")


