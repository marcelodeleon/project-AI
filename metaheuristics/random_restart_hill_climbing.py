from .hill_climbing import surroundings
from .hill_climbing import hill_climbing

def random_restart_hill_climbing(problem, steps=100, delta=1, initial=None, restart_count=10):
    final_step = None
    for step in hill_climbing(problem, steps, delta, initial):
        final_step = step
        yield step

    i = 1
    while(problem.evaluate(final_step[0]) and restart_count > 0):
        for step in hill_climbing(problem, steps, delta, initial):
            final_step = step
            yield step

        i+=1
        restart_count -= 1

def sum_squares():
    from .test_problems import SUM_SQUARES
    problem = SUM_SQUARES
    finalStep = list(random_restart_hill_climbing(problem, steps=10000))
    print(finalStep)
