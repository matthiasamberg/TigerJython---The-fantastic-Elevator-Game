from gamegrid import *
import os

class ElevatorActor(Actor):
    def __init__(self, pelevatorGraphics, elevator):
        self.pelevatorGraphics = pelevatorGraphics
        self.elevator = elevator
        self.id = elevator.getElevatorId()

        Actor.__init__(self, os.getcwd()+"/sprites/Elevator.png")
        self.halfWidth = int(self.getWidth(0)/2)
        self.halfHeight = int(self.getHeight(0)/2)
        self.height = self.getHeight(0)

    def getElevator(self):
        return self.elevator

    def act(self):
        self.setX(150+self.getWidth(0)*self.id)
        self.setY(int(-1+self.pelevatorGraphics.getWindowHeight(
        ) - self.pelevatorGraphics.getFloorHeight()*self.elevator.getCurrentFloor() - self.halfHeight))

    def positionPerson(self, personActor):
        passengers = self.elevator.getPassengers()
        index = self.elevator.getPassengers().index(personActor.getPerson())
        personActor.setX(int(self.getX() + index // 3 *
                             (personActor.getWidth(0)+2) - self.halfWidth/2))
        personActor.setY(int(self.getY() - self.halfHeight /
                             2 + index % 3 * (personActor.getHeight(0)+2)))
