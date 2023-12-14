import numpy as np
import queue


def add_free_items(old_item):
    """this function will add the free items in matrix

    Args:
        old_item (str): matrix items with letters

    Returns:
        int: cost matrix items
    """
    Coffee = 10
    Biscuit = 5
    Ice_cream = 12
    
    if "C" == old_item[-1]:
        return str(int(old_item[:-1]) - Coffee)
    elif "B" == old_item[-1]:
        return str(int(old_item[:-1]) - Biscuit)
    elif "I" == old_item[-1]:
        return str(int(old_item[:-1]) - Ice_cream)
    elif "R" == old_item[-1]:
        return str(old_item[:-1])
    elif "T" == old_item[-1]:
        return str(old_item[:-1])
    else:
        return old_item



def find_successors(matrix, position):
    positions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    moves = ["L", "R", "U", "D"]
    successors = []
    for direction, pos in enumerate(positions):
        new_x, new_y = position[0] + pos[0], position[1] + pos[1]
        if 0 <= new_x < matrix.shape[0] and 0 <= new_y < matrix.shape[1] and matrix[new_x, new_y] != "X":
            successors.append(moves[direction])
    return successors




#Rows = int(input("Give the number of rows:"))
#Columns = int(input("Give the number of columns:"))
#matrix = np.array([list(map(str, input().split())) for _ in range(Rows)])
#print(matrix)

#cost_matrix = list(map(lambda row: list(map(add_free_items, row)), matrix))
#print(cost_matrix)

matrix = np.array([["2R", "X", "5T"], ["4C", "3", "7I"]])
print(matrix)
cost_matrix = list(map(lambda row: list(map(add_free_items, row)), matrix))
print(cost_matrix)
print(find_successors(matrix, (1, 0)))