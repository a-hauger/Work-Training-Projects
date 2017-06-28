#!/usr/bin/env python3
from planet_class import Planet

class Mercury(Planet):
    def __init__(self):
        Planet.__init__(self, "Mercury", 58000000, .2409)

        self.lengthOfDay = 58
        self.diameter = 4879.4

    def setLengthOfDay(self, lengthOfDay):
        self.lengthOfDay = lengthOfDay

    def setDiameter(self, diameter):
        self.diameter = diameter

    def getLengthOfDay(self):
        return(self.lengthOfDay)

    def getDiameter(self):
        return(self.diameter)

    def getInfo(self):
        return("The planet " + self.getName() + " is " \
               + str(self.getDistanceToSun()) + "km to the sun and takes "\
               + str(self.getOrbitalPeriod()) + " Earth years to orbit the sun.  " \
               + self.getName() + " is " \
               + str(self.getDiameter()) + "km in diameter and takes " \
               + str(self.getLengthOfDay()) + "Earth days to rotate on its axis.")
