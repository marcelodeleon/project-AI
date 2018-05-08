# -*- coding: utf-8 -*-

def surroundings(center, radius, domains):
    """ The surroundings of a `center` is a list of new centers, all equal to the center except for
    one value that has been increased or decreased by `radius`.
    """
    return [center[0:i] + (center[i] + d,) + center[i + 1:]
               for i in range(len(center)) for d in (-radius, +radius)
               if center[i] + d >= domains[i][0] and center[i] + d <= domains[i][1]
           ]

def hill_climbing(problem, steps=100, delta=1, initial=None):
    """ Hill climbing optimization implemented as a generator function.
    """
    current = initial or problem.randomElement()
    lastEval = problem.objective(current)
    current = (current, lastEval)
    yield current
    for step in range(steps):
        nexts = problem.evaluated(surroundings(current[0], delta, problem.domains))
        current = nexts[0]
        if problem.compareEvaluations(lastEval, current[1]) > 0:
            lastEval = current[1]
        else:
            break # local optimum has been reached
        yield current

def sum_squares(initial=None):
    from .test_problems import SUM_SQUARES
    problem = SUM_SQUARES
    finalStep = list(hill_climbing(problem, steps=10000, initial=initial))[-1]
    return finalStep


def eggholder(initial=None):
    from .test_problems import EGGHOLDER
    problem = EGGHOLDER
    finalStep = list(hill_climbing(problem, steps=10000, initial=initial))[-1]
    return finalStep
    
def graph_coloring(initial=None):
    from .test_problems import GRAPHCOLORING
    problem = GRAPHCOLORING
    finalStep = list(hill_climbing(problem, steps=10000, initial=initial))[-1]
    return finalStep
