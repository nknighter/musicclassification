import numpy as np
import neurolab as nl
import numpy.random as rand
import glob
from KohonenNet import KohonenNet
from collections import OrderedDict

neuronsLen = 96
statsNum = 3
neurons = [[0, 25] for i in range(neuronsLen)]

dataFile = open('data.txt')

# Initialize data
data = dataFile.read()
data = data.split('\n')
data = np.array([[float(x) for x in row.split(' ')] for row in data[:-1]])

transposed = data.transpose()
meanVal = 1
for i in range(len(transposed)):
    if i % statsNum == 0:
        meanVal = np.mean(transposed[i])
    transposed[i] /= meanVal

data = transposed.transpose()
print data

# Network initialize
net = nl.net.newc(neurons, 5)
error = net.train(data, epochs=500)
#net = KohonenNet(5, neuronsLen)
#for i in range(200):
#    for vector in data:
#        net.teach(vector)

# Network processing
#for vector in data:
#    print net.handle(vector)
result = net.sim(data)
fileNames = glob.glob('./src_wav/*.wav')

info = []
infoFile = open('info.txt', 'w')
for i in range(len(result)):
    k = 0
    for j in range(len(result[i])):
        if result[i][j] == 1.0:
            k = j + 1
            break
    info.append({'name': fileNames[i][10:], 'cluster': k})

sortedInfo = OrderedDict()
for v in info:
    if v['cluster'] in sortedInfo:
        sortedInfo[v['cluster']].append(v['name'])
    else:
        sortedInfo[v['cluster']] = [v['name']]

res = [{'cluster': k, 'names': v} for k, v in sortedInfo.items()]
for cluster in res:
    infoFile.write(str(cluster['cluster']) + '--------------------------------\n')
    for name in cluster['names']:
        infoFile.write(name + '\n')

infoFile.close()
dataFile.close()