from neuron import Neuron
import math

class KohonenNet(object):
    def __init__(self, neuronsNum, vectorSize):
        self.neurons = [Neuron(vectorSize, 1.0 / neuronsNum) for i in range(neuronsNum)]
        self.iterations = 0
        self.minPotential = 0.75

    def getLearningCoefficient(self):
        return 0.3 * (0.9999) ** self.iterations

    def getNeurons(self):
        return self.neurons

    def getNearestTo(self, incomingVector):
        neurons = [i for i in self.neurons if i.getPotential() > self.minPotential]
        if len(neurons) == 0:
            nearest = self.neurons[0]
        else:
            nearest = neurons[0]

        for neuron in neurons:
            if neuron.distanceTo(incomingVector) < nearest.distanceTo(incomingVector):
                nearest = neuron
        return nearest

    def getNearestNumTo(self, incomingVector):
        i = 1
        nearest = self.neurons[0]
        for neuron in self.neurons:
            i += 1
            if neuron.distanceTo(incomingVector) < nearest.distanceTo(incomingVector):
                nearest = neuron

        return i

    def changePotentials(self, winner):
        for neuron in self.neurons:
            potential = neuron.getPotential()
            if neuron == winner:
                neuron.setPotential(potential - self.minPotential)
            else:
                neuron.setPotential(potential + 1.0 / len(self.neurons))

    def teach(self, incomingVector):
        self.iterations += 1
        incomingVector = self.normalize(incomingVector)
        winner = self.getNearestTo(incomingVector)
        diff = winner.diffTo(incomingVector)
        newWeights = winner.getWeights()[:]
        for i in range(len(newWeights)):
            newWeights[i] += self.getLearningCoefficient() * diff[i]
        winner.setWeights(newWeights)
        self.changePotentials(winner)

    def handle(self, incomingVector):
        incomingVector = self.normalize(incomingVector)

        return self.getNearestNumTo(incomingVector)

    def normalize(self, incomingVector):
        #return incomingVector
        summ = 0
        for i in incomingVector:
            summ += i ** 2
        normalized = [i / math.sqrt(summ) for i in incomingVector]
        #normalized = []
        #for i in incomingVector:
        #    if i == 255:
        #        normalized.append(1.0)
        #    else:
        #       normalized.append(0.0)
        return normalized

