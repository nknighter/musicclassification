import random
import math


class Neuron(object):
    def __init__(self, weightsLength, potential):
        self.weights = [random.random() for i in range(weightsLength)]
        self.potential = potential

    def getPotential(self):
        return self.potential

    def setPotential(self, potential):
        self.potential = potential

    def getWeights(self):
        return self.weights

    def distanceTo(self, incomingVector):
        assert len(incomingVector) == len(self.weights)

        distance = 0
        for i in range(len(self.weights)):
            distance += (incomingVector[i] - self.weights[i]) ** 2
        return math.sqrt(distance)

    def setWeights(self, weights):
        self.weights = weights


    def diffTo(self, incomingVector):
        assert len(incomingVector) == len(self.weights)
        diff = []
        for i in range(len(incomingVector)):
            diff.append(incomingVector[i] - self.weights[i])
        return diff

    def __str__(self):
        return str(self.weights)
