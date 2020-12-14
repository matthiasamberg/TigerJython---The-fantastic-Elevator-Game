from gamegrid import *
from elevatoractor import ElevatorActor
from mockactor import MockActor
from personactor import PersonActor


class PelevatorGraphics:

    def __init__(self, gameState):
        self.gameState = gameState
        self.numFloors = gameState.getNumFloors()

        self.numElevators = len(gameState.getElevators())

        self.elevatorActors = []
        self.personActors = []

        self.floorColors = [Color.orange, Color.blue,
                            Color.magenta, Color.green, Color.cyan, Color(0x006400),Color.yellow,Color(0xB03060),Color.black,Color.red,Color.DARK_GRAY,
                            Color.pink,Color(0xA52A2A),Color(0xBA55D3),Color(0x00FA9A)]
        for elevatorId in range(0, self.numElevators):
            self.elevatorActors.append(ElevatorActor(
                self, gameState.getElevators()[elevatorId]))

        self.floorHeight = self.elevatorActors[0].height
        self.windowHeight = self.floorHeight*self.numFloors
        self.windowWidth = 600
        makeGameGrid(self.windowWidth, self.windowHeight, 1, None)

        self.background = getBg()
        self.background.setBgColor(Color.white)

        self.mockActor = MockActor()
        addActor(self.mockActor, Location(-5, -5))

        for elevatorActor in self.elevatorActors:
            addActor(elevatorActor, Location(-1000, -1000))

        self.setupBg()
        registerNavigation(resetted=gameState.reset)

    def start(self):
        show()
        setSimulationPeriod(20)
        doRun()

    def getWindowHeight(self):
        return self.windowHeight

    def getWindowWidth(self):
        return self.windowWidth

    def getFloorHeight(self):
        return self.floorHeight

    def addPerson(self, person):
        personActor = PersonActor(self, person)
        addActor(personActor, Location(-1000, -1000))
        self.personActors.append(person)

    def getElevatorActor(self, elevator):
        for elevatorActor in self.elevatorActors:
            if elevatorActor.getElevator() == elevator:
                return elevatorActor

    def setupBg(self):
        self.background.clear()
        # draw a line for each floor
        for floor in range(0, self.numFloors):
            floorY = self.windowHeight - floor * self.floorHeight
            self.background.setPaintColor(self.floorColors[floor % len(self.floorColors)])
            # draw 'two' lines.. should be a rect, I know..
            self.background.drawLine(0, floorY, self.windowWidth, floorY)
            self.background.drawLine(0, floorY-1, self.windowWidth, floorY-1)
            self.background.drawLine(0, floorY-2, self.windowWidth, floorY-2)

    def dispose(self):
        dispose()



def play():
   if elevatorIsFull():
       naechsterStock = closestDestinationFloor()
       setElevatorDestination(naechsterStock)
