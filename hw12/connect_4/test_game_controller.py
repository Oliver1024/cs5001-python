from game_controller import GameController
from disk import Disk


def test_constructor():
    """Test game_controller constructor"""
    gc = GameController(2, 2, 100)
    assert gc.w == 2
    assert gc.h == 2
    assert gc.cell_size == 100
    assert gc.grid == [[None, None], [None, None]]
    assert gc.player == "RED"
    assert gc.HALF_SIZE == 50
    assert gc.y_vel == 20
    assert gc.game_start is False
    assert gc.dropping is False
    assert gc.mouse is False
    assert gc.grid_full is False
    assert gc.winner is None
    assert gc.score_file == {}
    assert gc.target == 0
    assert gc.column == 0
    assert gc.y_ai == 0
    assert gc.row_ai == 0
    assert gc.column_ai == -1
    assert gc.RANDOM_NUM == 6
    assert gc.NUM_THREE == 3
    assert gc.NUM_TWO == 2


def test_get_available_row():
    """Test to get the actual row of the board"""
    gc = GameController(3, 3, 100)
    gc.grid = [[None, True, True], [None, None, False], [False, True, False]]
    assert gc.get_available_row(0) == 1
    assert gc.get_available_row(2) == -1


def test_next_player():
    """Test alternate the color of disk"""
    gc = GameController(2, 2, 100)
    assert gc.player == "RED"
    gc.next_player()
    assert gc.player == "YELLOW"


def test_top_n_counts():
    """ Test top counts function """
    gc = GameController(2, 2, 100)
    gc.score_file = {"a": 1, "b": 2, "c": 3}
    assert gc.top_n_counts() == [('c', 3), ('b', 2), ('a', 1)]

    gc.score_file = {"a": 1, "c": 3, "b": 2}
    assert gc.top_n_counts() == [('c', 3), ('b', 2), ('a', 1)]


def test_check_column_full():
    """Test check_column_full function"""
    gc = GameController(3, 3, 100)
    gc.grid = [[True, True, True], [None, None, None], [None, None, False]]
    assert gc.check_column_full(0) is True


def test_check_winner():
    """ test function check winner """
    gc = GameController(7, 6, 100)
    disk_1 = Disk(3, "RED", 100, 1)
    disk_2 = Disk(3, "YELLOW", 100, 1)
    gc.grid = [[None, None, disk_1, None, None, None, None],
               [None, None, disk_1, None, None, None, None],
               [None, None, disk_1, None, None, None, None],
               [None, None, disk_1, None, None, None, None],
               [None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None]]
    assert gc.check_winner() is True

    gc.grid = [[None, None, disk_2, None, None, None, None],
               [None, None, disk_2, None, None, None, None],
               [None, None, disk_2, None, None, None, None],
               [None, None, disk_2, None, None, None, None],
               [None, None, None, None, None, None, None],
               [None, None, None, None, None, None, None]]
    assert gc.check_winner() is True
