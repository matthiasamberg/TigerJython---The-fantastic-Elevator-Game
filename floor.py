class Floor:
    def __init__(self, floorNum):
        self.floorNum = floorNum
        self.waitingPersons = []

    def addWaitingPerson(self, person):
        self.waitingPersons.append(person)

    def removeWaitingPerson(self, person):
        self.waitingPersons.remove(person)

    def getWaitingPersons(self):
        return self.waitingPersons

    def getNextWaitingPerson(self):
        if len(self.waitingPersons) > 0:
            person = self.waitingPersons.pop(0)
            return person
        return None

    def getWaitingPosition(self, person):
        return self.waitingPersons.index(person)
