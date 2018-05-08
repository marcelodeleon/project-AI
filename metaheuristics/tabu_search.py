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
    lastEval = problem.objective(current)
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
                        problem.objective(bestCandidate),
                        problem.objective(candidate)
                    ) > 0:
                bestCandidate = candidate

        if problem.compareEvaluations(
            problem.objective(best),
            problem.objective(bestCandidate)
        ) > 0:
            best = bestCandidate

        tabuList.append(bestCandidate)
        if len(tabuList) > tabuSize:
            tabuList.pop(0)
        yield (best, problem.objective(best))


def sum_squares():
    from .test_problems import SUM_SQUARES
    problem = SUM_SQUARES
    finalStep = list(tabu_search(problem, steps=10000))[-1]
    print(finalStep)


def eggholder():
    from .test_problems import EGGHOLDER
    problem = EGGHOLDER
    finalStep = list(tabu_search(problem, steps=10000))[-1]
    print(finalStep)
