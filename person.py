class Person:
    def __init__(self, gameState, startFloor, endFloor):
        self.gameState = gameState
        self.location = "startFloor"
        self.startFloor = startFloor
        self.endFloor = endFloor
        self.elevator = None

    def getStartFloor(self):
        return self.startFloor

    def getEndFloor(self):
        return self.endFloor

    def getLocation(self):
        return self.location

    def getWaitingPosition(self):
        return self.gameState.getWaitingPosition(self)

    def setLocationElevator(self, elevator):
        self.location = "elevator"
        self.elevator = elevator

    def getElevator(self):
        return self.elevator

    def unload(self):
        self.location = "endFloor"
        self.elevator = None
