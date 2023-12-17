import numpy as np
from queue import PriorityQueue
import time
import functions.functions as f

def bestFirstSearch(matrix) :
    """This is a bestFirstSearch search algorithm that returns the shortest path from start point to any other points of the matrix
    """
    start = time.time()
    pq = PriorityQueue()
    pq_end = PriorityQueue()
    path = ""
    pq_end.put((f.calculate_heuristic(matrix, path), path))
    pq.put((f.calculate_heuristic(matrix, path), path))
    visited = set()
    visited_items = ""
    f.print_matrix(matrix)
    while pq_end.get() != 0 :
        cost, path = pq.get()
        if f.is_job_done(matrix, path):
            f.print_matrix(matrix)
            return ((500 - f.calculate_cost(matrix, path)), path, (time.time() - start))
        i, j = f.find_location(matrix, path)
        if (i, j, visited_items) in visited:
            continue
        visited_items += f.item_check(matrix, path)
        visited.add((i, j, visited_items))
        for move in ["L", "R", "U", "D"]:
            newpath = path + move
            if move in f.find_successors(matrix, f.find_location(matrix, path)):
                pq.put(((f.calculate_heuristic(matrix, newpath)), newpath))
        pq_end.put(pq.queue[0])
    return "No routes found!"