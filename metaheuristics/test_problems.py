""" # Test functions

Test functions for benchmarking optimization techniques.
"""
from math import sin, sqrt
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

SUM_SQUARES = OptimizationProblem(
    domains=((-10, +10),)*2,
    objective=__sum_squares__
)

EGGHOLDER = OptimizationProblem(
    domains=((-512, 512),)*2,
    objective=__eggholder__
)

# TODO: Coloreo de grafos
