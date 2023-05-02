
from gamegrid import *
import globalvars
import os

# only used to get the 'act' callback from the engine and pass it on to the gamestate class


class MockActor(Actor):
    def __init__(self):
        Actor.__init__(self, os.getcwd()+"/sprites/Elevator.png")
        self.hide()

    def act(self):
        globalvars.gs.step()
