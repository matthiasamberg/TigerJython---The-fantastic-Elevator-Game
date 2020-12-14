# coding=UTF-8

    

# code zum starten des Spiels - bitte ignorieren
import os, sys

def setElevatorDestination(floor):
    if gs.elevators[0].state != "waitingForCommand":
        msg="The Elevator is busy (Did you call setElevatorDestination() twice in the play() function?)"
        msgDlg(msg,title="Error")
        print (msg)
        gs.reset()
    if floor < 0 or floor >= getNumFloors():
        message="This floor does not exist while calling setElevatorDestination(): "+str(floor)
        msgDlg(message,title="Error!")
        print (message)
        gs.reset()
    gs.elevators[0].setDestinationFloor(floor)


def getNumFloors():
    return gs.getNumFloors()

def getTopFloor():
    return gs.getNumFloors()-1

def getCurrentFloor():
    return gs.elevators[0].getCurrentFloor()


def getNumberOfPassengersWithDestination(floorNum):
    passengers=gs.elevators[0].getPassengers()
    count=0
    for person in passengers:
        if person.getEndFloor()==floorNum:
            count+=1
    return count

def getNumberOfPassengers():
    return len(gs.elevators[0].getPassengers())

def getNumberOfWaitingPassengers(floorNum):
    return len(gs.floors[floorNum].getWaitingPersons())

def isElevatorFull():
    return len(gs.elevators[0].getPassengers()) == gs.elevators[0].getMaxPassengers()

def isElevatorEmpty():
    return len(gs.elevators[0].getPassengers()) == 0

# returns the closest floor number (not current floor) where passengers are waiting or -1 if there are no passengers anywhere
def closestFloorWithWaitingPassengers():
    currentFloor = getCurrentFloor()
    floorDistance = 99
    resultFloor =-1
    for i in range(0,getNumFloors()):
        if i == currentFloor:
            continue
        if getNumberOfWaitingPassengers(i) > 0:
            distance=abs(currentFloor-i)
            if distance < floorDistance:
                floorDistance=distance
                resultFloor = i
    return resultFloor
                
# returns the closest floor where passengers in the elevator want to exit
def closestDestinationFloor():
    currentFloor = getCurrentFloor()
    floorDistance = 99
    resultFloor =-1
    for i in range(0,getNumFloors()):
        if i == currentFloor:
            continue
        if getNumberOfPassengersWithDestination(i) > 0:
            distance=abs(currentFloor-i)
            if distance < floorDistance:
                floorDistance=distance
                resultFloor = i
    return resultFloor

# ignore...   
    
globalvars.playfunction = play
globalvars.gs = GameState()
globalvars.gs.setup()
gs = globalvars.gs

# while not isDisposed():
#    delay(100)