#!/usr/bin/env python3

class Planet(object):
    def __init__(self, name, distance, orbitalPeriod):
        self.name = name
        self.distanceToSun = distance
        self.orbitalPeriod = orbitalPeriod

    def getName(self):
        return(self.name)

    def getDistanceToSun(self):
        return(self.distanceToSun)

    def getOrbitalPeriod(self):
        return(self.orbitalPeriod)

    def setName(self, name):
        self.name = name

    def setDistanceToSun(self, distance):
        self.distanceToSun = distance

    def setOrbitalPeriod(self, orbitalPeriod):
        self.orbitalPeriod = orbitalPeriod

    def getInfo(self):
        print("Your developer is silly and forgot the info.")