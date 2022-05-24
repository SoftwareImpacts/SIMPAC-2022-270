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

.. code-block:: python

	>>> from ga_segments.ga import GA_segments
	>>> import pandas as pd
	
	>>> series = pd.read_csv('./data/50words_TRAIN', header=None).values[:, 1:]
	
	>>> ga = GA_segments()
	>>> centroid, best_fitness, log = ga.calculate_centroids(series)
	
	
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
 
 @article{LEONALCAIDE202074,
title = {An evolutionary approach for efficient prototyping of large time series datasets},
journal = {Information Sciences},
volume = {511},
pages = {74-93},
year = {2020},
issn = {0020-0255},
doi = {https://doi.org/10.1016/j.ins.2019.09.044},
url = {https://www.sciencedirect.com/science/article/pii/S0020025519308965},
author = {Pablo Leon-Alcaide and Luis Rodriguez-Benitez and Ester Castillo-Herrera and Juan Moreno-Garcia and Luis Jimenez-Linares},
keywords = {Time series summarization, Genetic algorithms, Elastic distances, Data mining},
}

## Documents related ##

This library was initialy a Final Degree Project and you can find the documentation of the development in the next link:

* Final Degree Project Documentation (Spanish)

Later it was extented as part of a Master's thesis that can be found in the next link:



### Scientific papers ###

There are also some papers related to this library that can be seen bellow:

Characterisation of mobile-device tasks by their associated cognitive load through EEG data processing
eeglib: computational analysis of cognitive performance during the use of video games
