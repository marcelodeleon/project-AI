# -*- coding: utf-8 -*-


def surroundings(center, radius, domains):
    """
    The surroundings of a `center` is a list of new centers, all equal to the
    center except for one value that has been increased or decreased by
    `radius`.
    """

    return [center[0:i] + (center[i] + d,) + center[i + 1:]
            for i in range(len(center)) for d in (-radius, +radius)
            if center[i] + d >= domains[i][0] and
            center[i] + d <= domains[i][1]]


def tabu_search(problem, steps=100, delta=1, initial=None, tabuSize=5):
    """ Tabu Search optimization implemented as a generator function."""

    current = initial or problem.randomElement()
    lastEval = problem.evaluate(current)
    current = (current, lastEval)

    tabuList = []
    bestCandidate = current[0]
    best = current[0]
    tabuList.append(bestCandidate)

    yield current

    for step in range(steps):
        neighborHood = surroundings(bestCandidate, delta, problem.domains)
        bestCandidate = neighborHood[0]

        for candidate in neighborHood:
            if candidate not in tabuList and \
                    problem.compareEvaluations(
                        problem.evaluate(bestCandidate),
                        problem.evaluate(candidate)
                    ) > 0:
                bestCandidate = candidate

        if problem.compareEvaluations(
            problem.evaluate(best),
            problem.evaluate(bestCandidate)
        ) > 0:
            best = bestCandidate

        tabuList.append(bestCandidate)
        if len(tabuList) > tabuSize:
            tabuList.pop(0)
        yield (best, problem.evaluate(best), problem.evaluation_count)


def sum_squares(initial=None):
    from .test_problems import SUM_SQUARES
    problem = SUM_SQUARES
    finalStep = list(tabu_search(problem, steps=10000, initial=initial))[-1]
    return finalStep


def eggholder(initial=None):
    from .test_problems import EGGHOLDER
    problem = EGGHOLDER
    finalStep = list(tabu_search(problem, steps=10000, initial=initial))[-1]
    return finalStep


def graph_coloring(initial=None):
    from .test_problems import GRAPHCOLORING
    problem = GRAPHCOLORING
    finalStep = list(tabu_search(problem, steps=10000, initial=initial))[-1]
    return finalStep
