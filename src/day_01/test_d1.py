from .main import calc_distance_between_lists, calc_similarity_score


def test_calc_distance_between_lists():
    tests = [{"l1": [3, 4, 2, 1, 3, 3], "l2": [4, 3, 5, 3, 9, 3], "output": 11}]

    for tt in tests:
        got = calc_distance_between_lists(tt["l1"], tt["l2"])
        assert got == tt["output"]


def test_calc_similarity_score():
    tests = [{"l1": [3, 4, 2, 1, 3, 3], "l2": [4, 3, 5, 3, 9, 3], "output": 31}]

    for tt in tests:
        got = calc_similarity_score(tt["l1"], tt["l2"])
        assert got == tt["output"]
