#!/usr/bin/env python3

import sys
import networkx as nx

if len(sys.argv) == 3:
    state = sys.argv[1]
    graph_file = sys.argv[2]
else:
    exit(1)

row_length = 3
solution = "1|2|3|4|5|6|7|8|9|"

graph = nx.read_gexf(graph_file)

steps_to_solve = nx.shortest_path(graph, state, solution)

for i, permutation in enumerate(steps_to_solve):
    print("--- {}".format(i))
    permutation_list = permutation.split("|")
    if permutation_list[-1] == "":
        permutation_list = permutation_list[:-1]
    line_to_print = ""
    while len(permutation_list) > 1:
        for i in range(row_length):
            line_to_print = line_to_print + permutation_list.pop(0)
        print(line_to_print)
        line_to_print = ""

