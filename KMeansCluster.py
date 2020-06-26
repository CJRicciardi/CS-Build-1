# CS-Date-Science-Build-Week-1/KMeansCluster.py

import numpy as np
import matplotlib.pyplot as plt, mpl_toolkits.mplot3d
import pandas as pd
import copy


class KMeans:
    def __init__(self, k=3, max_iterations=500):
        self.k = k
        self.max_iterations = max_iterations

    def fit(self, data):

        cols = data.columns.values.tolist()

        a = cols[0]
        b = cols[1]
        x = data[a].tolist()
        y = data[b].tolist()
    
        # first find the min and max values for both x and y
        xmin = min(x)
        xmax = max(x)
        ymin = min(y)
        ymax = max(y)

        # then randomly assign self.k self.centroids that fit with in the min/max of x        and y
        self.centroids = {}
        self.closeRoid = {}

        for i in range(self.k):
            self.centroids[i] = [np.random.randint(xmin, xmax), np.random.randint        (ymin, ymax)]
            self.closeRoid[i] = []

        # then loop through all of the data, assigning each point to the        centroid it is closest to

        for i in range(len(x)):
            xy = [x[i], y[i]]
            distance = []
            for j in range(self.k):
                distance.append(np.sqrt(
                    ((xy[0]-self.centroids[j][0])**2) + ((xy[1]-self.centroids[j][1])     **2)
                ))
            self.closeRoid[distance.index(min(distance))].append(xy)

        # print(len(x))
        # print('self.centroids:', self.centroids)
        # print('self.closeRoid:', self.closeRoid)

        # next find the average location of the data points for each cluster        to establish a new centroid.

        # originalRoid = copy.deepcopy(self.closeRoid)

        # insert while loop here oldRoid = self.closeRoid and max_iterations != 0
        runcount = copy.copy(self.max_iterations)

        while runcount > 0:

            oldRoid = copy.deepcopy(self.closeRoid)

            for i in range(self.k):
                xtotal = 0
                ytotal = 0
                for j in range(len(self.centroids[i])):
                    xtotal += self.closeRoid[i][j][0]
                    ytotal += self.closeRoid[i][j][1]
                self.centroids[i] = [xtotal/len(self.centroids[i]), ytotal/len        (self.centroids[i]   )]

            # print('new self.centroids:', self.centroids)

            for n in range(self.k):
                self.closeRoid[n] = []

            # print('self.closeRoid', self.closeRoid)

            # print(originalRoid == self.closeRoid)

            for i in range(len(x)):
                xy = [x[i], y[i]]
                distance = []
                for j in range(self.k):
                    distance.append(np.sqrt(
                        ((xy[0]-self.centroids[j][0])**2) + ((xy[1]-self.centroids[j]     [1]) **2)
                    ))
                self.closeRoid[distance.index(min(distance))].append(xy)

            if self.closeRoid == oldRoid:
                break
                # return print('Centroids: \n', self.centroids, '\nClose Data:       \n', self.closeRoid)

            else:
                runcount -= 1

        print('Centroids: \n', self.centroids, '\nData By Centroid: \n', self.closeRoid, '\n Runcount: ', runcount)

    def pred(self, x, y):
        xy = [x, y]
        distance = []
        for j in range(self.k):
            distance.append(np.sqrt(
                ((xy[0]-self.centroids[j][0])**2) + ((xy[1]-self.centroids[j][1])     **2)
            ))
        return print(distance.index(min(distance)))