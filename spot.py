import colors
import pygame


class Spot:
    """Object to specify each spot on the game grid. Color of the spot specifys the spot's status.
    For example, black means a spot is a barrier."""

    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = colors.WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        """Returns position of spot object."""
        return self.row, self.col

    def is_closed(self):
        """Returns True if object's color is red indicating the spot has already been visited in the graph search."""
        return self.color == colors.RED

    def is_open(self):
        """Returns True if object's color is green indicating the spot queued for being visited in the graph search."""
        return self.color == colors.GREEN

    def is_barrier(self):
        """Returns True if object's color is black indicating the spot is a barrier the search algorithm must search around."""
        return self.color == colors.BLACK

    def is_start(self):
        """Returns Ture is object's color is orange indicating the spot is the starting location of the search algorithm."""
        return self.color == colors.ORANGE

    def is_end(self):
        """Returns True if object's color is turquoise indicating the spot is the desired ending location of the search algorithm."""
        return self.color == colors.TURQUOISE

    def reset(self):
        """Resets the object's color to white indicating the spot is now an empty spot without additional functionality."""
        self.color = colors.WHITE

    def make_closed(self):
        self.color = colors.RED

    def make_open(self):
        self.color = colors.GREEN

    def make_barrier(self):
        self.color = colors.BLACK

    def make_start(self):
        self.color = colors.ORANGE

    def make_end(self):
        self.color = colors.TURQUOISE

    def make_path(self):
        self.color = colors.PURPLE

    def draw(self, win):
        """Draws spot in the game window."""
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        """Updates a spot's list of neighbors by checking the spots above, below, left, and right of the calling spot.
        If a neighbor is a barrier, said neighbor is excluded from list of neighbors."""
        self.neighbors = []
        if (
            self.row < self.total_rows - 1
            and not grid[self.row + 1][self.col].is_barrier()
        ):  # Down
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # Up
            self.neighbors.append(grid[self.row - 1][self.col])

        if (
            self.col < self.total_rows - 1
            and not grid[self.row][self.col + 1].is_barrier()
        ):  # Right
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.row > 0 and not grid[self.row][self.col - 1].is_barrier():  # Left
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False