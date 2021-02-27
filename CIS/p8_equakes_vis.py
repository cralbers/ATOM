'''
CIS 210 Project 8: World Wide Earthquake Watch
Author: Cora Albers
Credits:
Description:
'''
import math
import random

def readFile(filename):
    with open(filename, 'r') as dataFile:

        dataDict = {}

        key = 0
        aLine = dataFile.readline()
        while aLine != '':
            key = key + 1
            score = int(aLine)
            dataDict[key] = [score]

            aLine = dataFile.readLine()

    return dataDict




def euclidD(point1, point2):
    total = 0
    for index in range(len(point1)):
        diff = (point1[index]-point2[index]) ** 2
        total = total + diff

    euclidDistance = math.sqrt(total)
    return euclidDistance

def createCentroids(k, dataDict):
    centroids = []
    centroidCount = 0
    centroidKeys = [] # list of unique keys

    while centroidCount < k:
        rKey = randome.randint(1, len(dataDict))
        if rKey not in centroidKeys:
            centroids.append(dataDict[rKey])
            centroidKeys.append(rKey)
            centroidCount = centroidCount + 1

    return centroids

def createClusters(k, centroids, dataDict, repeats):
    for aPass in range(repeats):
        print('****PASS', aPass + 1, '****')
        clusters = [] # create list of k empty lists
        for i in range(k):
            clusters.append([])
        for aKey in dataDict: # calculate distance to centroid
            distances = []
            for clusterIndex in range(k):
                dToC = euclidD(dataDIct[aKey], centroids[clusterIndex])
                distances.append(dToC)

            minDist = min(distances)
            index = distances.index(minDist)

            clusters[index].append(aKey)

        dimensions = len(dataDict[1])
        for clusterIndex in range(k):
            sums = [0] * dimensions
            for aKey in clusters[clusterIndex]:
                dataPoints = dataDict[aKey]
                for ind in range(len(dataPoints)):
                    sums[ind] = sums[ind] + dataPoints[ind]
            for ind in range(len(sums)):
                clusterLen = len(clusters[clusterIndex])
                if clusterLen != 0:
                    sums[ind] = sums[ind] / clusterLen

            centroids[clusterIndex] = sums

        for c in clusters:
            print('CLUSTER')
            for key in c:
                print(dataDict[key], end = ' ')
            print()

    return clusters
