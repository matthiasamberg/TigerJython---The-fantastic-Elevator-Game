import globalvars
from gamestate import *
import random

# Persistente Variablen in der play() Funktion, sollten vor der Funktion gesetzt werden
# und mit global innerhalb der Funktion bezeichnet werden


richtung="up"

def play():
    # Deklarieren Sie Ihre Variable(n) als 'global', damit diese so funktionieren wie Sie es gewohnt sind:
    global richtung
    print(richtung) # gibt das erste mal "up" aus.. und beim nächsten mal "down"
    richtung="down"

   

#------------ bitte drin lassen (aber anderweitig ignorieren)
execfile ("functions.py")
