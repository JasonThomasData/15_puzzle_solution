#!/usr/bin/env python3

import networkx as nx

#15 puzzle solution finder, using pathfinding


def initialise_new_board(board):
    new_board = {} 
    new_board["tiles"] = list()
    for row_state in board["tiles"]:
        new_board["tiles"].append(list(row_state))
    new_board["blank_space_location"] = list(board["blank_space_location"])
    return new_board

def switch_tile_and_blank_space(board, tile_location):
    blank_space_location = board["blank_space_location"]
    blank_space = board["tiles"][blank_space_location[0]][blank_space_location[1]]
    tile = board["tiles"][tile_location[0]][tile_location[1]]
    new_board = initialise_new_board(board)
    new_board["tiles"][blank_space_location[0]][blank_space_location[1]] = tile
    new_board["tiles"][tile_location[0]][tile_location[1]] = blank_space
    new_board["blank_space_location"] = tile_location
    return new_board

def get_proposed_new_space(blank_space_location, relative_location):
    proposed_new_space = []
    proposed_new_space.append(blank_space_location[0] + relative_location[0])
    proposed_new_space.append(blank_space_location[1] + relative_location[1])
    return proposed_new_space

def check_space_available(proposed_new_space):
    if proposed_new_space[0] < 0 or proposed_new_space[0] > 2:
        return False
    elif proposed_new_space[1] < 0 or proposed_new_space[1] > 2:
        return False
    return True

def move_blank_space_if_possible(board, relative_location):
    new_space_location = get_proposed_new_space(board["blank_space_location"], relative_location)
    if check_space_available(new_space_location):
        new_board = switch_tile_and_blank_space(board, new_space_location)
        return new_board
    else:
        return board

def tiles_to_state(tiles):
    state = ""
    for row in tiles:
        row_string = "|".join(row)
        state += row_string
        state += "|"
    return state

def are_all_successors_found(graph_edges_out_count, blank_space_location, possible_successors):
    if graph_edges_out_count < possible_successors[blank_space_location[0]][blank_space_location[1]]:
        return False
    else:
        return True

relative_location = {
    "UP": [-1, 0],
    "DOWN": [1, 0],
    "LEFT": [0, -1],
    "RIGHT": [0, 1]
}

possible_successors = [
    [2,3,3,2],
    [3,4,4,3],
    [3,4,4,3],
    [2,3,3,2]
]

processing_queue = []
explored_states = set()

"""
board = {
    "tiles": [
        [ "1",  "2",  "3",  "4"],
        [ "5",  "6",  "7",  "8"],
        [ "9", "10", "11", "12"],
        ["13", "14", "15", "16"]
    ],
    "blank_space_location": [3,3]
}
"""

board = {
    "tiles": [
        [ "1",  "2",  "3"],
        [ "4", "5",  "6"],
        [ "7", "8", "9"]
    ],
    "blank_space_location": [2,2]
}

def report_on_graph(graph):
    print(graph.number_of_edges())
    print(graph.number_of_nodes())

processing_queue.append(board)

# Board = the multimensional array of tiles and index of blank space (for efficiency)
# State = the string version of tiles[], each as a permutation derived from the original sequence/state
# Using board, get state. If state in graph has less than all its possible successors, derive (at most) next four boards
# Add those new boards to the queue
# Add edges between parent vertex and next verices (all states) to the graph
# Get a new board from the queue
# Note - it appears that networkX does not add duplicate edges, so we don't have to check

# Note - this is fine for the 8 puzzle, but the 15 puzzle is far too large with too many permutations to do this with Python in any effecient way
# Port to CPP if you really want to

if __name__ == "__main__":
    graph = nx.DiGraph() 

    while True:
        if len(processing_queue) % 5000 == 0:
            print("{} board states completed so far".format(len(explored_states)))
            print("{} board states to process".format(len(processing_queue)))

        try:
            board = processing_queue.pop(0)
        except IndexError:
            report_on_graph(graph)
            nx.write_gexf(graph, "8_puzzle_graph.gefx")
            exit(0)
        state = tiles_to_state(board["tiles"])
        try:
            assert state not in explored_states
        except AssertionError:
            continue

        for key in relative_location:
            new_board = move_blank_space_if_possible(board, relative_location[key])
            if new_board["blank_space_location"] != board["blank_space_location"]:
                new_state = tiles_to_state(new_board["tiles"])
                graph.add_edge(state, new_state)
                processing_queue.append(new_board)

        explored_states.add(state)

    state = tiles_to_state(board["tiles"])
    print(graph.out_edges(state))
    print(processing_queue)
