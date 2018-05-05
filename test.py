from metaheuristics import *

tests = [

    tabu_search.sum_squares,
    hill_climbing.sum_squares,
    tabu_search.eggholder,
    hill_climbing.eggholder
]

for test in tests:
    print(test.__module__ + " - " + test.__name__)
    test()
