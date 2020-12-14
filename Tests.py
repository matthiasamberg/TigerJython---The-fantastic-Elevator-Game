import globalvars
from gamestate import *
import random



def play():
    # eine mögliche Destination (wenn wir keine bessere finden 
    # ist das nächste Stockwerk, wo jemand wartet
    destination = closestFloorWithWaitingPassengers()
    
    # falls niemand wartet, gab die obige Funktion -1 zurück, 
    # dass müssen wir hier behandeln:
    if destination == -1:
        destination = 0
        
    # falls aber der Lift voll ist, fahren wir an den nächsten Ort
    # wo jemand aussteigen möchte:
    if isElevatorFull() :         
        destination = closestDestinationFloor()
        
    setElevatorDestination(destination)
    

#------------ bitte drin lassen (aber anderweitig ignorieren
execfile ("functions.py")
