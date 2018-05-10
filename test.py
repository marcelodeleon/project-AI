from metaheuristics import *

TEST_TIMES = 50
    
def calc_stats(meta1, meta2):
    print("{} {:>45} {:>45} {:>45}".format(meta1.__module__ + "_fitness", meta1.__module__ + "_evaluations", meta2.__module__ + "_fitness", meta2.__module__ + "_evaluations"))
    for i in range(TEST_TIMES):
        print("{:>35} {:>45} {:>45} {:>45}".format(meta1()[1], meta1()[2], meta2()[1], meta2()[2]))

def print_title(title):
    print("-"*180)
    print("{:^100}".format(title))
    print("-"*180)

#TEST SUM_SQUARES
print_title("SUM_SQUARES")
calc_stats(particle_swarm.sum_squares, tabu_search.sum_squares)

#TEST EGGHOLDER
print_title("EGGHOLDER")
calc_stats(particle_swarm.eggholder, tabu_search.eggholder)

#TEST GRAPH COLORING
print_title("GRAPH COLORING")
calc_stats(particle_swarm.graph_coloring, tabu_search.graph_coloring)