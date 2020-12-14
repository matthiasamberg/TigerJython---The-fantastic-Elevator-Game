from random import randint


class Elevator:

    def __init__(self, elevatorId, gameState):
        self.gameState = gameState
        self.id = elevatorId
        self.currentFloor = 0.0
        self.maxSpeed = 0.13
        self.speed = 0.0
        self.destinationFloor = 0
        self.state = "loading"  # up down unloading loading waiting
        self.delay = 10
        self.maxPassengers = 6
        self.passengers = []
        self.transportedPersons = 0

    def getSpeed(self):
        return self.speed

    def getCurrentFloor(self):
        return self.currentFloor

    def getElevatorId(self):
        return self.id

    def getMaxPassengers(self):
        return self.maxPassengers

    def getDistanceToDestinationFloor(self):
        return abs(self.currentFloor - self.destinationFloor)

    def setDestinationFloor(self, floor):
        self.destinationFloor = floor
        self.state = "moving"

    def checkArrival(self):
        if self.getDistanceToDestinationFloor() < 0.03:
            self.speed = 0
            self.currentFloor = int(self.destinationFloor)
            self.state = "unloading"
            self.delay = 20

    def getPassengers(self):
        return self.passengers

    def run(self):
        if self.delay > 0:
            self.delay -= 1
            return

        if self.state == "moving":
            if self.getDistanceToDestinationFloor() > 0.7:
                self.speed = min(self.speed + 0.005, self.maxSpeed)
            elif self.getDistanceToDestinationFloor() < 0.6:
                self.speed = max(self.speed - 0.01, 0.03)

            if self.currentFloor < self.destinationFloor:
                self.currentFloor += self.speed
            elif self.currentFloor > self.destinationFloor:
                self.currentFloor -= self.speed

            self.checkArrival()
        elif self.state == "unloading":
            unloading = False
            for person in self.passengers:
                if not unloading and person.getEndFloor() == self.currentFloor:
                    # unload that person
                    self.passengers.remove(person)
                    person.unload()
                    self.transportedPersons += 1
                    self.delay = 15
                    unloading = True
            if not unloading:
                self.delay = 5
                self.state = "loading"

        elif self.state == "loading":
            if len(self.passengers) < self.maxPassengers:
                # load another person (if persons available)
                person = self.gameState.getNextWaitingPerson(
                    int(self.currentFloor))
                if person != None:
                    self.passengers.append(person)
                    person.setLocationElevator(self)
                else:
                    self.state = "waitingForCommand"
            else:
                self.state = "waitingForCommand"
            self.delay = 10

    def getCurrentFloor(self):
        return self.currentFloor

    def getTransportedPersons(self):
        return self.transportedPersons

    def getPassengers(self):
        return self.passengers
