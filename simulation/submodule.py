import networkx as nx
import random as rnd
import matplotlib.pyplot as plt


class Submodule:

    def __init__(self, id, facilitytype, numGroups=0, Groups=[], People=[], Area=0, Contact=0, Mobility=0, Density=0, Cleanliness=0, Infected = []):
        # Either initialize parameterized or empty and fill in with methods.
        self.__id = id
        self.__facilitytype = facilitytype
        self.__Area = Area
        self.__Contact = Contact
        self.__Mobility = Mobility
        self.__Density = Density
        self.__Cleanliness = Cleanliness
        self.__numGroups = numGroups
        self.__Groups = Groups
        self.__People = People
        self.__Infected = Infected

    def clearPeople(self):
        self.__People = []
        self.__Infected = []

    def addPerson(self, person):
        self.__People.append(person)
        if person.getInfectionState():
            self.__Infected.append(person)

    def calcContact(self):
        contact = 0  # placeholder
        return contact

    def calcMobility(self):
        mobility = 0  # placeholder
        return mobility

    def calcDensity(self):
        density = 0  # placeholder
        return density

    def calcNumGroups(self):
        numGroups = 0  # placeholder
        return numGroups

    def createGroups(self):

        count = 0
        groups = []
        while count < len(self.__People):
            ran = min(rnd.randint(1, 2), len(self.__People) - count)
            group = []
            for i in range(ran):
                group.append(self.__People[count])
                count += 1
            groups.append(group)
        """
        groups = []
        group = []
        for each in self.__People:
            group.append(each)
        groups.append(group)
        """
        self.__numGroups = len(groups)
        self.__Groups = groups


    def calcCleanliness(self):
        cleanliness = 0  # placeholder
        return cleanliness

    def getInfected(self):
        infected = []
        for person in self.__People:
            if person.isInfected():
                infected.append(person)
        return infected

    # This is a potential new function to create the graph, which calcInfection will then traverse
    def createGraph(self):
        sizes = [0] * self.__numGroups
        idList = []
        p = []
        for i in range(self.__numGroups):
            sizes[i] = len(self.__Groups[i])

            for person in self.__Groups[i]:
                idList.append(person.getID())

            tmp_p = [0] * self.__numGroups
            for j in range(self.__numGroups):
                if j == i:
                    tmp_p[
                        j] = 1  # If you're in the same group as an infected person, this is the likelihood you are in contact
                else:
                    tmp_p[
                        j] = .05  # Likelihood of connections between groups, arbitrary formula
            p.append(tmp_p)
        #nx.draw(nx.stochastic_block_model(sizes, p, idList))
        #plt.show()
        #print(idList)
        return nx.stochastic_block_model(sizes, p, idList)

    # It seems for simplicity, it would make the most sense to calcInfection here
    def calcInfection(self, stochGraph):
        for person in self.__Infected:
            for i in list(stochGraph.neighbors(person.getID())):
                # TODO Make this more accurate
                randNum = rnd.randint(1, 101)
                if (randNum < 30):
                    for j in range(len(self.__People)):
                        if self.__People[j].getID() == i:
                            self.__People[j].setInfectionState(True)
                   # self.__People[self.__People.index(i)].setInfected(True)  # Set's person to be infected



