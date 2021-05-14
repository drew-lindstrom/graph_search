from util import reconstruct_path, make_grid, draw_grid, draw, get_clicked_pos
from queue import PriorityQueue
from heapq import *

import pygame


def dijkstra(draw, grid, start, end):
    """Function for Dijkstra's graph search."""
    # Distance dictionary - First value is distance, second value is boolean if visited.
    distance = {spot: [float("inf"), False] for row in grid for spot in row}
    # Unexplored_set - used to keep track of how many nodes still need to be examined.
    unexplored_set = {spot: 0 for row in grid for spot in row}
    came_from = {}

    distance[start][0] = 0

    while len(unexplored_set) > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        minimum = float("inf")
        current = None

        # Find the next spot with smallest distance that has not been visited yet.
        for key, value in distance.items():
            if value[0] < minimum and value[1] == False:
                minimum = value[0]
                current = key

        # Mark new current node as visited and remove from unexplored_set.
        try:
            distance[current][1] = True
        except Exception:
            break
        del unexplored_set[current]

        # Create path if the current node is the end node.
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        # Visit neighbors of current node. If neighbor hasn't been visited yet and its current distance is larger than from the current node,
        # update neighbor's distance, set it to open, and add to came_from dictionary.
        for neighbor in current.neighbors:
            if neighbor in unexplored_set:
                new_distance = distance[current][0] + 1
            if new_distance < distance[neighbor][0]:
                came_from[neighbor] = current
                distance[neighbor][0] = new_distance
                neighbor.make_open()

        draw()

        # Mark current node as closed after being examined.
        if current != start:
            current.make_closed()

    return False


def h(p1, p2):
    """Direct distance between current point and end point. H value is used in a_star graph search algorithm."""
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(draw, grid, start, end):
    """Function for a_star graph search."""
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    # g_score is the cost of the current path from the start to the current node.
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0

    # f_score = g_score + h_score (h_score is the cost from the current node to the end node).
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False