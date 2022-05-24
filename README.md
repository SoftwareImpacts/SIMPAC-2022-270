# TS_Evolutionary_Prototyping
A Python module for finding the prototype in large sets of time series

The implemented software allows to find it from a set of time series using the dynamic time warping (DTW) as the distance measure between series and does not restrict the search space for the prototype to the series of the input set. The software also includes use cases for the library using it in applications of clustering and classification. 

## Main Features ##

Enumerating keywords

## Installation ##

pip ...

## Dependencies ##

* numpy
* pandas
* deap
* scikit-learn
* matplotlib

# Getting Started

Bellow there is a Quickstart Guide to EvolutionaryPrototypingTS.

## Basic example ##
 
Next piece of code shows a basic usage of the library. In it is shown how to import a file and x

..code-block:: python
'''python

	>>> from ga_segments.ga import GA_segments
	>>> import pandas as pd
	
	>>> series = pd.read_csv('./data/50words_TRAIN', header=None).values[:, 1:]
	
	>>> ga = GA_segments()
	>>> centroid, best_fitness, log = ga.calculate_centroids(series)
'''
	
	
Example of use of Nearest Centroid algorithm with GA-Segments:

.. code-block:: python

	>>> from ga_segments.nc import NC
	>>> import pandas as pd
	>>> from sklearn.model_selection import train_test_split
	
	>>> series = pd.read_csv('./data/50words_TRAIN', header=None)
	>>> x, y = series[:, 1:], series[:, 0]
	>>> x_train, x_val, y_train, y_val = train_test_split(x, y, test_size=0.2)
	
	>>> nc = NC()
	>>> nc.fit(x_train, y_train)
	>>> nc.predict(x_val)
	>>> nc.labels
  
  
 ## Citing ## 
 
 If TS_Evolutionary_Prototyping has been useful in your research, please, consider citing the next article:
 
[An evolutionary approach for efficient prototyping of large time series datasets; Information Sciences
Volume 511, February 2020, Pages 74-93](https://www.sciencedirect.com/science/article/pii/S0020025519308965)

