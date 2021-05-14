from util import *
import pytest


class test_util:
    def test_get_clicked_pos(self):
        pos = [1, 15]
        width = 10
        rows = 2

        assert get_clicked_pos(pos, rows, width) == 0, 3