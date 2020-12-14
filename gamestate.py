from pelevatorgraphics import PelevatorGraphics
from elevator import Elevator
from person import Person
from seededrandom import SeededRandom
from floor import Floor
import globalvars
import time


class GameState:

    def __init__(self):
        global gs
        gs = self
        self.numFloors = 15
        self.numElevators = 1
        self.elevators = []
        self.floors = []
        self.ticks = 0

    def setup(self):

        for i in range(0, self.numFloors):
            self.floors.append(Floor(i))

        for elevatorID in range(0, self.numElevators):
            self.elevators.append(Elevator(elevatorID, self))

        self.graphics = PelevatorGraphics(self)

        # create some persons initially
        for i in range(0, 3):
            self.addPerson()

        self.graphics.start()

    def addPerson(self):
        startFloor = globalvars.seededRandom.getRandInt(-4, self.numFloors-1)
        startFloor = max(0, startFloor)
        while True:
            endFloor = globalvars.seededRandom.getRandInt(0, self.numFloors-1)
            if endFloor != startFloor:
                break

        person = Person(self, startFloor, endFloor)
        self.graphics.addPerson(person)
        self.floors[startFloor].addWaitingPerson(person)

    def getNumFloors(self):
        return self.numFloors

    def getWaitingPersons(self):
        count = 0
        for floor in self.floors:
            count += len(floor.getWaitingPersons())
        return count

    def step(self):
        self.ticks += 1
        # just stop if game ended
        if self.ticks == 10000:
            transportedPersons = 0
            for elevator in self.elevators:
                transportedPersons += elevator.getTransportedPersons()
            msgDlg("You transported "+str(transportedPersons), title="Time's up!")
            print("You transported "+str(transportedPersons))
            self.reset()

        if self.ticks >= 10000:
            time.sleep(0.05)
            return

        if (self.ticks % 80 == 0):
            self.addPerson()

        if len(self.elevators) == 1:
            if self.elevators[0].state == "waitingForCommand":
                globalvars.playfunction()

        for elevator in self.elevators:
            elevator.run()

    def getElevators(self):
        return self.elevators

    def getWaitingPosition(self, person):
        floor = self.floors[person.getStartFloor()]
        return floor.getWaitingPosition(person)

    def getNextWaitingPerson(self, floorNum):
        return self.floors[floorNum].getNextWaitingPerson()

    def reset(self):
        self.graphics.dispose()
