# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from .ga import TS_prototyping
from .segmentsf import dtw




class NC:
    """ Class that contains the Nearest Centroid algorithm, which classifies a set of time series according to the
    centroid of the class closest to each series.
    """

    def __init__(self, ga='simple', params_ga={}, verbose=0):
        """
        :param ga: The genetic algorithm that is used.
        :param params_ga: Parameters of genetic algorithm.
        :param verbose
        """
        self.verbose = verbose
        self.ga = ga
        self.params_ga = params_ga

    def fit(self, X, y):
        """ Function that calculates the centroids of each class.

        :param X: Series.
        :param y: Class to which each series belongs.
        """
        if not isinstance(X, np.ndarray):
            X = np.array(X)

        self.classes = np.unique(y)
        self.centroids = []
        inertia_total = 0

        for i, c in enumerate(self.classes):
            GA = TS_prototyping(**self.params_ga)
            
            mask = y == c
            S = X[mask]
            centroid, inertia, _ = GA.calculate_centroids(S=S)
            self.centroids.append(centroid)

            if self.verbose > 1:
                self._plot(i, centroid)
            if self.verbose > 0:
                self._print(i, inertia)

            inertia_total += inertia
            self.inertia = inertia_total


    def predict(self, X):
        """ Function that calculates the class to which each series of a set of series X belongs. Each series is
        assigned the class of the nearest centroid.
    
        :param X
        """
        if not self.centroids:
            raise Exception('Error: Fit the data first')
    
        if not isinstance(X, np.ndarray):
            X = np.array(X)
    
        self.labels = np.zeros(len(X))
        for i, x in enumerate(X):
            dists = [dtw.dtw(x, c)[0] for c in self.centroids]
            class_index = np.argmin(dists)
            self.labels[i] = self.classes[class_index]
    
    
    def fit_predict(self, X_train, y, X_test):
        """
        Función que calcula los centroides y posteriormente clasifica un conjunto de series. Para ello, llama en primer
        lugar a :meth:`fit` y después a :meth:`predict`.
    
        :param X_train
        :param y_train
        :param X_test
    
        :return: Class of each series of X_test
        """
        self.fit(X_train, y)
        return self.predict(X_test)
    
   
    
    def score(self, X_test, y):
        """ Function that calculates the accuracy of the classification.
    
        :param X_test
        :param y
    
        :return: Accuracy.
        """
        self.predict(X_test)
        return (self.labels == y).sum() / float(y.shape[0])
    
    
    def _print(self, n, inertia):
        print('Error class[{}]: {:.3f}'.format(n, inertia))
        print('-' * 25)
    
    
    def _plot(self, n, c):
        plt.plot(c)
        plt.title('Centroid {}'.format(n))
        plt.show()
