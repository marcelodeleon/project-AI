from metaheuristics import *

tests = [
    hill_climbing.sum_squares,
    random_restart_hill_climbing.sum_squares
]

for test in tests:
    print(test.__module__ + " - " + test.__name__)
    test()
