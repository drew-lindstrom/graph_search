from spot import Spot
import colors
import pytest


class TestSpot:
    def test_get_pos(self):
        test_spot = Spot(2, 3, 3, 2)
        row, col = test_spot.get_pos()
        assert row == 2
        assert col == 3

    def test_is_closed(self):
        test_spot = Spot(2, 3, 3, 2)
        assert test_spot.is_closed == False
        testspot.color = colors.RED
        assert test_spot.is_closed == True

    def test_is_open(self):
        test_spot = Spot(2, 3, 3, 2)
        assert test_spot.is_open == False
        testspot.color = colors.GREEN
        assert test_spot.is_open == True

    def test_is_barrier(self):
        test_spot = Spot(2, 3, 3, 2)
        assert test_spot.is_barrier == False
        testspot.color = colors.BLACK
        assert test_spot.is_barrier == True

    def test_is_start(self):
        test_spot = Spot(2, 3, 3, 2)
        assert test_spot.is_start == False
        testspot.color = colors.ORANGE
        assert test_spot.is_start == True

    def test_is_end(self):
        test_spot = Spot(2, 3, 3, 2)
        assert test_spot.is_end == False
        testspot.color = colors.TURQUOISE
        assert test_spot.is_end == True

    def test_reset(self):
        test_spot = Spot(2, 3, 3, 2)
        testspot.color = colors.RED
        assert test_spot.color != colors.WHITE
        test_spot.reset()
        assert test_spot.color == colors.WHITE

    def test_make_closed(self):
        test_spot = Spot(2, 3, 3, 2)
        assert test_spot.color != colors.RED
        testspot.make_closed()
        assert test_spot.color == colors.RED

    def test_make_open(self):
        test_spot = Spot(2, 3, 3, 2)
        assert test_spot.color != colors.GREEN
        testspot.make_open()
        assert test_spot.color == colors.GREEN

    def test_make_barrier(self):
        test_spot = Spot(2, 3, 3, 2)
        assert test_spot.color != colors.BLACK
        testspot.make_barrier()
        assert test_spot.color == colors.BLACK

    def test_make_start(self):
        test_spot = Spot(2, 3, 3, 2)
        assert test_spot.color != colors.ORANGE
        testspot.make_start()
        assert test_spot.color == colors.ORANGE

    def test_make_end(self):
        test_spot = Spot(2, 3, 3, 2)
        assert test_spot.color != colors.TURQUOISE
        testspot.make_end()
        assert test_spot.color == colors.TURQUOISE

    def test_make_path(self):
        test_spot = Spot(2, 3, 3, 2)
        assert test_spot.color != colors.PURPLE
        testspot.make_path()
        assert test_spot.color == colors.PURPLE

    # def draw(self, win):
    #     """Draws spot in the game window."""
    #     pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    # def update_neighbors(self, grid):
    #     """Updates a spot's list of neighbors by checking the spots above, below, left, and right of the calling spot.
    #     If a neighbor is a barrier, said neighbor is excluded from list of neighbors."""
    #     self.neighbors = []
    #     if (
    #         self.row < self.total_rows - 1
    #         and not grid[self.row + 1][self.col].is_barrier()
    #     ):  # Down
    #         self.neighbors.append(grid[self.row + 1][self.col])

    #     if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():  # Up
    #         self.neighbors.append(grid[self.row - 1][self.col])

    #     if (
    #         self.col < self.total_rows - 1
    #         and not grid[self.row][self.col + 1].is_barrier()
    #     ):  # Right
    #         self.neighbors.append(grid[self.row][self.col + 1])

    #     if self.row > 0 and not grid[self.row][self.col - 1].is_barrier():  # Left
    #         self.neighbors.append(grid[self.row][self.col - 1])

    # def __lt__(self, other):
    #     return False