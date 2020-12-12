from population import Population
from submodule import Submodule
import json
import random
class Module:

    def __init__(self, State, County, Interventions):
        self.__State = State
        self.__County = County

    def createPopulation(self):
        print("createPop function")
        return Population(self.__State, self.__County).get_dict()


    def createSubmodules(self):
        with open("submodules.json") as file:
            subdict = json.load(file)

        subList = []
        for each in subdict:
            subList.append(Submodule(each, each[0]))
        return subList
    # TODO

    def movePop(self, TOD, DOW, population, facilities):
        for each in facilities:
            each.clearPeople()
        for each in population:
            fac = (random.randint(0, 19))
            facilities[fac].addPerson(population[each])
