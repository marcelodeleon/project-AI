""" # Test functions

Test functions for benchmarking optimization techniques.
"""
import random
from math import sin, sqrt, inf
from .problem import OptimizationProblem

# References:
# NOQA + [Test functions for optimization @ Wikipedia](https://en.wikipedia.org/wiki/Test_functions_for_optimization)
# NOQA + [Test functions and datasets @ Virtual Library of Simulation Experiments](https://www.sfu.ca/~ssurjano/optimization.html)


def __eggholder__(elem):
    (x1, x2) = elem

    return - ((x2 + 47) * sin(sqrt(abs(x2 + x1/2 + 47)))) - \
        (x1 * sin(sqrt(abs(x1 - (x2 + 47)))))


def __sum_squares__(elem):
    (x, y) = elem

    suma = 0
    for i in range(2):
        suma += i*x**2+i*y**2

    return suma

adjs = []  
    
def __graph_coloring__(elem):
    sameColor = 0
    for adj in adjs:
        if(elem[adj[0]] == elem[adj[1]]):
            sameColor += 0.5
            
    return sameColor
    

MIN_GRAPH_COLOR = 0
MAX_GRAPH_COLOR = 5
GRAPH_SIZE = 20
GRAPH_ADJ_PROB = 0.1

for i in range(GRAPH_SIZE):
    for j in range(GRAPH_SIZE):
        if(i != j):
            if(random.random() < GRAPH_ADJ_PROB):
                adjs.append((i,j))
                adjs.append((j,i))
        

SUM_SQUARES = OptimizationProblem(
    domains=((-10, +10),)*2,
    objective=__sum_squares__
)

EGGHOLDER = OptimizationProblem(
    domains=((-512, 512),)*2,
    objective=__eggholder__
)

GRAPHCOLORING = OptimizationProblem(domains= ((MIN_GRAPH_COLOR, MAX_GRAPH_COLOR),)*GRAPH_SIZE, objective=__graph_coloring__, target=-inf)
