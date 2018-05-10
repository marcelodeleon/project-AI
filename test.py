from metaheuristics import *

TEST_TIMES = 50
    
def calc_stats(meta1, meta2, problem, objective):
    meta1_stats = []
    meta2_stats = []

    for i in range(TEST_TIMES):
        meta1_stats.append(meta1())
        meta2_stats.append(meta2())
        
    return (meta1_stats, meta2_stats)
    
def print_stats(stats):
    print("particle_swarm \t tabu_search")
    for x,y in zip(stats[0], stats[1]):
        print(str(x).replace(".",",")+"\t"+str(y).replace(".",","))

#TEST SUM_SQUARES
print("SUM_SQUARES")
print_stats(calc_stats(particle_swarm.sum_squares, tabu_search.sum_squares, test_problems.SUM_SQUARES, 0))

#TEST EGGHOLDER
print("EGGHOLDER")
print_stats(calc_stats(particle_swarm.eggholder, tabu_search.eggholder, test_problems.EGGHOLDER, -959.6407))

#TEST GRAPH COLORING
print("GRAPH COLORING")
print_stats(calc_stats(particle_swarm.graph_coloring, tabu_search.graph_coloring, test_problems.GRAPHCOLORING, 0))