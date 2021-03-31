#!/usr/bin/env python3

from puzzle_solution import check_space_available, move_blank_space_if_possible, relative_location, possible_successors, are_all_successors_found

#Some tests thanks
assert check_space_available([-1,0]) == False
assert check_space_available([4,0]) == False
assert check_space_available([0,-1]) == False
assert check_space_available([0,4]) == False
assert check_space_available([2,2]) == True

test_board = {
    "tiles": [["1","2","3","4"],["5","6","7","8"],["9","10","11","12"],["13","14","15","16"]],
    "blank_space_location": [3,3]
}
new_test_board = move_blank_space_if_possible(test_board, relative_location["UP"])
assert new_test_board["tiles"] == [["1","2","3","4"],["5","6","7","8"],["9","10","11","16"],["13","14","15","12"]]
assert new_test_board["blank_space_location"] == [2,3]

test_board = {
    "tiles": [["1","2","3","4"],["5","6","7","8"],["9","10","11","16"],["13","14","15","12"]],
    "blank_space_location": [2,3]
}
new_test_board = move_blank_space_if_possible(test_board, relative_location["DOWN"])
assert new_test_board["tiles"] == [["1","2","3","4"],["5","6","7","8"],["9","10","11","12"],["13","14","15","16"]]
assert new_test_board["blank_space_location"] == [3,3]

test_board = {
    "tiles": [["1","2","3","4"],["5","6","7","8"],["9","10","11","12"],["13","14","15","16"]],
    "blank_space_location": [3,3]
}
new_test_board = move_blank_space_if_possible(test_board, relative_location["LEFT"])
assert new_test_board["tiles"] == [["1","2","3","4"],["5","6","7","8"],["9","10","11","12"],["13","14","16","15"]]
assert new_test_board["blank_space_location"] == [3,2]

test_board = {
    "tiles": [["1","2","3","4"],["5","6","7","8"],["9","10","11","12"],["13","14","16","15"]],
    "blank_space_location": [3,2]
}
new_test_board = move_blank_space_if_possible(test_board, relative_location["RIGHT"])
assert new_test_board["tiles"] == [["1","2","3","4"],["5","6","7","8"],["9","10","11","12"],["13","14","15","16"]]
assert new_test_board["blank_space_location"] == [3,3]

test_board = {
    "tiles": [["1","2","3","4"],["5","6","7","8"],["9","10","11","12"],["13","14","15","16"]],
    "blank_space_location": [3,3]
}
new_test_board = move_blank_space_if_possible(test_board, relative_location["RIGHT"])
assert new_test_board["tiles"] == test_board["tiles"]
assert new_test_board["blank_space_location"] == test_board["blank_space_location"] 

test_board = {
    "tiles": [["1","2","3","4"],["5","6","7","8"],["9","10","11","12"],["13","14","15","16"]],
    "blank_space_location": [3,3]
}
new_test_board = move_blank_space_if_possible(test_board, relative_location["DOWN"])
assert new_test_board["tiles"] == test_board["tiles"]
assert new_test_board["blank_space_location"] == test_board["blank_space_location"] 

test_board = {
    "tiles": [[16,2,3,4],["5","6","7","8"],["9","10","11","12"],[13,14,15,1]],
    "blank_space_location": [0,0]
}
new_test_board = move_blank_space_if_possible(test_board, relative_location["UP"])
assert new_test_board["tiles"] == test_board["tiles"]
assert new_test_board["blank_space_location"] == test_board["blank_space_location"] 

test_board = {
    "tiles": [[16,2,3,4],["5","6","7","8"],["9","10","11","12"],[13,14,15,1]],
    "blank_space_location": [0,0]
}
new_test_board = move_blank_space_if_possible(test_board, relative_location["LEFT"])
assert new_test_board["tiles"] == test_board["tiles"]
assert new_test_board["blank_space_location"] == test_board["blank_space_location"] 

print("It appears to work")

assert are_all_successors_found(2, [0,0], possible_successors) == True
assert are_all_successors_found(2, [0,3], possible_successors) == True
assert are_all_successors_found(2, [3,0], possible_successors) == True
assert are_all_successors_found(2, [3,3], possible_successors) == True
assert are_all_successors_found(1, [0,0], possible_successors) == False
assert are_all_successors_found(1, [0,3], possible_successors) == False
assert are_all_successors_found(1, [3,0], possible_successors) == False
assert are_all_successors_found(1, [3,3], possible_successors) == False

assert are_all_successors_found(3, [0,1], possible_successors) == True
assert are_all_successors_found(3, [0,2], possible_successors) == True
assert are_all_successors_found(3, [3,1], possible_successors) == True
assert are_all_successors_found(3, [3,2], possible_successors) == True
assert are_all_successors_found(3, [1,0], possible_successors) == True
assert are_all_successors_found(3, [2,0], possible_successors) == True
assert are_all_successors_found(3, [1,3], possible_successors) == True
assert are_all_successors_found(3, [2,3], possible_successors) == True

assert are_all_successors_found(2, [0,1], possible_successors) == False
assert are_all_successors_found(2, [0,2], possible_successors) == False
assert are_all_successors_found(2, [3,1], possible_successors) == False
assert are_all_successors_found(2, [3,2], possible_successors) == False
assert are_all_successors_found(2, [1,0], possible_successors) == False
assert are_all_successors_found(2, [2,0], possible_successors) == False
assert are_all_successors_found(2, [1,3], possible_successors) == False
assert are_all_successors_found(2, [2,3], possible_successors) == False