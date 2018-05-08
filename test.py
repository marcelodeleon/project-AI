from metaheuristics import *

TEST_TIMES = 50
    
def calc_stats(meta1, meta2, problem, objective):
    meta1_stats = 0
    meta2_stats = 0

    for i in range(TEST_TIMES):
        initial = problem.randomElement()
        meta1_stats += meta1(initial)[1]
        meta2_stats += meta2(initial)[1]
        
    return (meta1_stats/TEST_TIMES, meta2_stats/TEST_TIMES)

#TEST SUM SUM_SQUARES
print(calc_stats(hill_climbing.sum_squares, tabu_search.sum_squares, test_problems.SUM_SQUARES, 0))

#TEST EGGHOLDER
print(calc_stats(hill_climbing.eggholder, tabu_search.eggholder, test_problems.EGGHOLDER, -959.6407))

#TEST GRAPH COLORING
print(calc_stats(hill_climbing.graph_coloring, tabu_search.graph_coloring, test_problems.GRAPHCOLORING, 0))