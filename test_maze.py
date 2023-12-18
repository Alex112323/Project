from solutions import Solution
from players import Player


def test_standart_binary_solution():
    field_up = [[1, 1, 1, 1],
                [0, 0, 0, 0],
                [1, 1, 1, 0],
                [1, 1, 0, 0]]
    field_right = [[0, 0, 0, 1],
                   [1, 1, 1, 1],
                   [0, 0, 0, 1],
                   [0, 0, 1, 1]]
    solution = Solution(field_up, field_right)
    result = solution.binary_solution(1, 3)
    expected = ([(1, 3), (2, 3), (2, 2)], 3, 2)
    assert result == expected


def test_boundary_points_binary_solution():
    field_up = [[1, 1, 1],
                [0, 0, 0],
                [0, 0, 0]]
    field_right = [[0, 0, 1],
                   [1, 1, 1],
                   [1, 1, 1]]
    solution = Solution(field_up, field_right)
    result = solution.binary_solution(2, 0)
    expected = ([], 2, 0)
    assert result == expected


def test_standart_sidewinder_solution():
    field_up = [[1, 1, 1, 1],
                [0, 0, 1, 0],
                [0, 1, 0, 0],
                [0, 1, 0, 0]]
    field_right = [[0, 0, 0, 1],
                   [1, 1, 0, 1],
                   [0, 1, 1, 1],
                   [1, 0, 1, 1]]
    solution = Solution(field_up, field_right)
    result = solution.sidewinder_solution(2, 3)
    expected = ([(2, 3), (2, 2), (2, 2), (2, 1), (2, 1), (3, 1), (3, 0)], 3, 0)
    assert result == expected


def test_boundary_points_sidewinder_solution():
    field_up = [[1, 1, 1],
                [1, 0, 0],
                [0, 0, 0]]
    field_right = [[0, 0, 1],
                   [0, 1, 1],
                   [1, 1, 1]]
    solution = Solution(field_up, field_right)
    result = solution.sidewinder_solution(1, 0)
    expected = ([], 1, 0)
    assert result == expected


def test_check_coordinates_standard():
    player = Player(30, 60)
    player.rect.x, player.rect.y = 404, 404
    assert player.check_right_place(20, 20)


def test_check_coordinates_negative():
    player = Player(30, 60)
    player.rect.x, player.rect.y = 403, 404
    assert not player.check_right_place(20, 20)
