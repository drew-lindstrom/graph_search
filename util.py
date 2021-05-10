from spot import Spot

import colors
import pygame


def reconstruct_path(came_from, current, draw):
    """Changes color of spots in came_from to purple to signify they are part of the path.
    Then calls draw() after each spot update to update the display."""
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def make_grid(rows, width):
    """Creates a 2D matrix of spot objects representing the grid in the game window."""
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid


def draw_grid(win, rows, width):
    """Draws gray lines on the window to signify the grid."""
    gap = width // rows

    for i in range(rows):
        pygame.draw.line(win, colors.GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, colors.GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    """Fills window with white, draws individual squares for each spot, draws the grid lines, and then updates the display."""
    win.fill(colors.WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    """Given the position of a right or left click on the grid, returns the row and column where the click occured."""
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col
