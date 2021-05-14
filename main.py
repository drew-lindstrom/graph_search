from util import reconstruct_path, make_grid, draw_grid, draw, get_clicked_pos
from search_algorithms import a_star, dijkstra
from spot import Spot

import pygame
import math


WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Graph Search")


def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True

    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # If the left mouse button is pressed, gets the spot where the mouse clicked. First click creates the start point.
            # Second click creates the end point. All clicks afterwards create barriers.
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                if not start:
                    start = spot
                    start.make_start()

                elif not end and spot != start:
                    end = spot
                    end.make_end()

                elif spot != end and spot != start:
                    spot.make_barrier()

            # If the right mouse button is pressed, gets the spot where the mouse clicked. Resets the specified spot.
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                spot = grid[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            # If key on keyboard is pressed...
            if event.type == pygame.KEYDOWN:

                # If '1' or '2' is pressed and start and end are placed,
                # updates neighbors for each spot in the grid and then runs the appropriate search algorithm.
                if (
                    (event.key == pygame.K_2 or event.key == pygame.K_1)
                    and start
                    and end
                ):
                    for row in grid:
                        for spot in row:
                            spot.update_neighbors(grid)
                    # If '1' is pressed, runs the dijkstra's search algorithm.
                    if event.key == pygame.K_1:
                        dijkstra(lambda: draw(win, grid, ROWS, width), grid, start, end)
                    # If '2' is pressed, runs the a* search algorithm.
                    if event.key == pygame.K_2:
                        a_star(lambda: draw(win, grid, ROWS, width), grid, start, end)

                # If 'C' is pressed, clears the grid.
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

                # If 'Q' is pressed, quits the game.
                if event.key == pygame.K_q:
                    run = False

    pygame.quit()


main(WIN, WIDTH)