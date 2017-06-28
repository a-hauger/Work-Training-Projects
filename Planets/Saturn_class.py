#!/usr/bin/env python3
from planet_class import Planet

class Saturn(Planet):
    def __init__(self):
        Planet.__init__(self, "Saturn", 1427000000, 29.456)

        self.lengthOfDay = .417
        self.diameter = 120536

    def setLengthOfDay(self, lengthOfDay):
        self.lengthOfDay = lengthOfDay

    def setDiameter(self, diameter):
        self.diameter = diameter

    def getLengthOfDay(self):
        return (self.lengthOfDay)

    def getDiameter(self):
        return (self.diameter)

    def getInfo(self):
        return ("The planet " + self.getName() + " is " \
                + str(self.getDistanceToSun()) + "km to the sun and takes " \
                + str(self.getOrbitalPeriod()) + " Earth years to orbit the sun.  " \
                + self.getName() + " is " \
                + str(self.getDiameter()) + "km in diameter and takes " \
                + str(self.getLengthOfDay()) + "Earth days to rotate on its axis.")