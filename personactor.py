from gamegrid import *
import random


class PersonActor(Actor):
    def __init__(self, pelevatorGraphics, person):
        self.pelevatorGraphics = pelevatorGraphics
        self.person = person
        bitmap = GGBitmap(10, 10)
        bitmap.setPaintColor(
            pelevatorGraphics.floorColors[person.getEndFloor() % len(pelevatorGraphics.floorColors)])
        bitmap.fillCircle(Point(5, 5), 5)
        Actor.__init__(self, bitmap.getBufferedImage())

    def act(self):
        if self.person.getLocation() == "startFloor":
            waitingPosition = self.person.getWaitingPosition()
            self.setX(100 - waitingPosition * self.getWidth(0))
            self.setY(int(self.pelevatorGraphics.getWindowHeight(
            ) - self.pelevatorGraphics.getFloorHeight()*self.person.getStartFloor() - self.getHeight(0)))
        elif self.person.getLocation() == "elevator":
            elevatorActor = self.pelevatorGraphics.getElevatorActor(
                self.person.getElevator())
            elevatorActor.positionPerson(self)
        elif self.person.getLocation() == "endFloor":
            self.setY(int(self.pelevatorGraphics.getWindowHeight(
            ) - self.pelevatorGraphics.getFloorHeight()*self.person.getEndFloor() - self.getHeight(0)))
            self.setX(int(self.getX()+random.random()*3))
            if self.getX() > self.pelevatorGraphics.getWindowWidth()+10:
                # destroy self!
                removeActor(self)

    def getPerson(self):
        return self.person
