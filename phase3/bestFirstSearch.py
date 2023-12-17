import numpy as np
from queue import Queue, LifoQueue, PriorityQueue
import time
import functions.functions as f

# def bestFirstSearch(matrix) :
#
#     """This is a Uniform-cost search algorithm that returns the shortest path from start point to any other points of the matrix
#     """
#     start = time.time()
#     pq = PriorityQueue()
#     path = ""
#     pq.put((f.heuristic(matrix, path), path))
#     visited = set()
#     visited_items = ""
#     while not pq.empty():
#         cost, path = pq.get()
#         if f.is_job_done(matrix, path):
#             f.print_matrix(matrix)
#             return ((500 - f.calculate_cost(matrix, path)), path, (time.time() - start))
#         i, j = f.find_location(matrix, path)
#         if (i, j, visited_items) in visited:
#             continue
#         visited_items += f.item_check(matrix, path)
#         visited.add((i, j, visited_items))
#         for move in ["L", "R", "U", "D"]:
#             newpath = path + move
#             if move in f.find_successors(matrix, f.find_location(matrix, path)):
#                 pq.put(((f.heuristic(matrix, newpath)), newpath))
#     end = time.time()
#     return "No routes found!"
#
# choise = str(input("Do you want to enter the matrix manually(True) or use the samples(False)?"))
# if choise == "True":
#     Rows = int(input("Give the number of rows:"))
#     Columns = int(input("Give the number of columns:"))
#     matrix = np.array([list(map(str, input().split())) for _ in range(Rows)])
# elif choise == "False":
#     sample_number = int(input("(3, 3) -> 0\n(3, 5) -> 1\n(6, 5) -> 2\nchoose one of those samples:"))
#     if sample_number == 0:
#         matrix = np.array([["5", "2T", "1"], ["2R", "5", "X"], ["4C", "3T", "7I"]])
#     elif sample_number == 1:
#         matrix = np.array([["5", "3C", "9I", "25", "1"], ["2R", "X", "3T", "X", "5T"], ["4C", "4", "2", "3", "7I"]])
#     elif sample_number == 2:
#         matrix = np.array([["4", "2C", "1", "15", "1B"], ["5", "4", "5", "X", "X"]
#                          , ["2", "2", "1", "1R", "1T"], ["5", "2", "1", "1", "X"]
#                          , ["50", "2", "1C", "1", "X"], ["2T", "2", "1", "1", "1"]])
#
# print(bestFirstSearch(matrix));

# matrix = np.array([["4", "2C", "1", "15", "1B"], ["5", "4", "5", "X", "X"]
#                  , ["2", "2", "1", "1R", "1T"], ["5", "2", "1", "1", "X"]
#                  , ["50", "2", "1C", "1", "X"], ["2T", "2", "1", "1", "1"]])
matrix = np.array([["5", "2T", "1"], ["2R", "5", "X"], ["4C", "3T", "7I"]])

f.print_matrix(matrix)
print(f.heuristic(matrix, "URD"))