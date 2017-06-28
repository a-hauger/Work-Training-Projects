#!/usr/bin/env python3
from Mercury_class import Mercury
from Venus_class import Venus
from Earth_class import Earth
from Mars_class import Mars
from Jupiter_class import Jupiter
from Saturn_class import Saturn
from Uranus_class import Uranus
from Neptune_class import Neptune
from Pluto_class import Pluto

import argparse

class SolarSystem(object):
    def __init__(self):
        self.mercury = Mercury()
        self.venus = Venus()
        self.earth = Earth()
        self.mars = Mars()
        self.jupiter = Jupiter()
        self.saturn = Saturn()
        self.uranus = Uranus()
        self.neptune = Neptune()
        self.pluto = Pluto()

        self.planetList = [self.mercury, self.venus, self.earth, self.mars, self.jupiter, self.saturn, self.uranus, self.neptune, self.pluto]

    def numOrbits(self, numDays):
        print("The following are the number of orbits each planet has achieved"\
              "based on the number of days input into the command line:\n"\
              + "\tMercury: " + str(numDays/self.mercury.getOrbitalPeriod()) + " orbits.\n"\
              + "\tVenus: " + str(numDays/self.venus.getOrbitalPeriod()) + " orbits.\n"\
              + "\tEarth: " + str(numDays/self.earth.getOrbitalPeriod()) + " orbits.\n"\
              + "\tMars: " +str(numDays/self.mars.getOrbitalPeriod()) + " orbits.\n"\
              + "\tJupiter: " + str(numDays/self.jupiter.getOrbitalPeriod()) + " orbits.\n"\
              + "\tSaturn: " + str(numDays/self.saturn.getOrbitalPeriod()) + " orbits.\n"\
              + "\tUranus: " + str(numDays/self.uranus.getOrbitalPeriod()) + " orbits.\n"\
              + "\tNeptune: "+ str(numDays/self.neptune.getOrbitalPeriod()) + " orbits.\n"\
              + "\tPluto: " + str(numDays/self.pluto.getOrbitalPeriod()) + " orbits.\n")


    def getSolarSystemInfo(self):
        return ("The information about our solar system is as follows:\n"
                + "\t" + self.mercury.getInfo() + "\n"
                + "\t" + self.venus.getInfo() + "\n"
                + "\t" + self.earth.getInfo() + "\n"
                + "\t" + self.mars.getInfo() + "\n"
                + "\t" + self.jupiter.getInfo() + "\n"
                + "\t" + self.saturn.getInfo() + "\n"
                + "\t" + self.uranus.getInfo() + "\n"
                + "\t" + self.neptune.getInfo() + "\n"
                + "\t" + self.pluto.getInfo() + "\n")

    def getPlanetList(self):
        return (self.planetList)

    def getPlanetName(self, searchName):
        nameIndex = self.getPlanetList().index(searchName)
        returnName = self.planetList[nameIndex]
        return(returnName)


def main():
    parser = argparse.ArgumentParser(description = 'Parsing Command Line Arguments')
    parser.add_argument('--numOrbits', metavar = 'DAYS', type = int, nargs = 1, help = 'A tool to determine the number of orbits all planets have achieved based on user input')
    parser.add_argument('--ssInfo', help = 'Displays information for all planets in the Solar System, repeats INT times', action = 'store_true')
    parser.add_argument('-i', '--planet', metavar = 'NAME', nargs = 1, help = 'Displays information for a specific planet based on user input')
    parser.add_argument('-l', '--lengthofday', metavar = 'PLANET', nargs = 1, help = 'Displays information for a specific planet length of day')
    parser.add_argument('-o', '--orbitalperiod', metavar = 'PLANET', nargs = 1, help = 'Displays information for a specific planet orbital period')
    parser.add_argument('-e', '--diameter', metavar = 'PLANET', nargs = 1, help = 'Displays the information for a specific planet equatorial diameter')
    parser.add_argument('-d', '--distance', metavar = 'PLANET', nargs = 1, help = 'Displays the informatino for a specific planet distance from sun')

    args = parser.parse_args()

    solar = SolarSystem()

    if(args.numOrbits):
        days = args.numOrbits[0]
        print(str(solar.numOrbits(days)))

    if(args.ssInfo):
        print(solar.getSolarSystemInfo())

    if(args.planet):
        plan = args.planet[0]
        for planet in solar.planetList:
            if plan.lower() == planet.getName().lower():
                print(planet.getInfo())

    if(args.lengthofday):
        plan = args.lengthofday[0]
        for planet in solar.planetList:
            if plan.lower() == planet.getName().lower():
                print("The length of " + plan.lower() + "'s day is " + str(planet.getLengthOfDay()) + " Earth days.")

    if(args.orbitalperiod):
        plan = args.orbitalperiod[0]
        for planet in solar.planetList:
            if plan.lower() == planet.getName().lower():
                print("The length of " + plan.lower() + "'s orbital period is " + str(planet.getOrbitalPeriod()) + " Earth years.")


    if(args.diameter):
        plan = args.diameter[0]
        for planet in solar.planetList:
            if plan.lower() == planet.getName().lower():
                print("The diameter of " + plan.lower() + " is " + str(planet.getDiameter()) + " km.")

    if(args.distance):
        plan = args.distance[0]
        for planet in solar.planetList:
            if plan.lower() == planet.getName().lower():
                print("The distance of " + plan.lower() + " to the sun is " + str(planet.getDistanceToSun()) + " km.")

    return

if (__name__ == "__main__"):
    main()