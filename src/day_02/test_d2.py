from .main import count_safe_reports


def test_count_safe_reports():
    tests = [
        {
            "input": [
                [7, 6, 4, 2, 1],
                [1, 2, 7, 8, 9],
                [9, 7, 6, 2, 1],
                [1, 3, 2, 4, 5],
                [8, 6, 4, 4, 1],
                [1, 3, 6, 7, 9],
            ],
            "output": 2,
        }
    ]

    for tt in tests:
        got = count_safe_reports(tt["input"])

        assert got == tt["output"]


def test_count_safe_reports_with_tolerance():
    tests = [
        {
            "input": [
                [7, 6, 4, 2, 1],
                [1, 2, 7, 8, 9],
                [9, 7, 6, 2, 1],
                [1, 3, 2, 4, 5],
                [8, 6, 4, 4, 1],
                [1, 3, 6, 7, 9],
            ],
            "output": 4,
        },
        {
            "input": [
                [9, 5, 4, 2, 1],
            ],
            "output": 1,
        },
        {
            "input": [
                [7, 6, 4, 6, 2],
            ],
            "output": 1,
        },
    ]

    for tt in tests:
        got = count_safe_reports(tt["input"], tolerance=1)

        assert got == tt["output"]
