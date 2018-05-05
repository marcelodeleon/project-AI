from metaheuristics import *

tests = [
    hill_climbing.eggholder,
    random_restart_hill_climbing.eggholder,

]

for test in tests:
    print(test.__module__ + " - " + test.__name__)
    test()
