import numpy as np



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
        return int(old_item[:-1]) + Coffee
    elif "B" == old_item[-1]:
        return int(old_item[:-1]) + Biscuit
    elif "I" == old_item[-1]:
        return int(old_item[:-1]) + Ice_cream
    elif "R" == old_item[-1]:
        return int(old_item[:-1])
    elif "T" == old_item[-1]:
        return int(old_item[:-1])
    else:
        return old_item    



Rows = int(input("Give the number of rows:"))
Columns = int(input("Give the number of columns:"))
matrix = np.array([list(map(str, input().split())) for _ in range(Rows)])
print(matrix)

cost_matrix = matrix = list(map(lambda row: list(map(add_free_items, row)), matrix))
print(cost_matrix)
