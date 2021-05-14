from search_algorithms import h
import pytest


class TestSearchAlgorithms:
    def test_h(self):
        p1 = (0, 0)
        p2 = (0, 5)
        assert h(p1, p2) == 5

        p2 = (-5, 0)
        assert h(p1, p2) == 5

        p2 = (-5, -5)
        assert h(p1, p2) == 10