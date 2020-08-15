import pytest

import min_area


@pytest.mark.parametrize(
    "x, y, k, r",
    (
        ([1], [1], 1, 4),
        ([1, 2], [1, 2], 2, 9),
        ([1, 2], [1, 2], 1, 4),
        ([1, 2, 4], [1, 2, 4], 3, 25),
        ([1, 2, 3], [1, 7, 3], 2, 16),
        ([1, 2, 4], [1, 2, 4], 2, 9),
        ([3, 2, 1], [1, 7, 3], 2, 16),
        ([1, 4, 9], [1, 2, 3], 2, 25),
    ),
)
def test_min_area(x, y, k, r):
    assert min_area.min_area(x, y, k) == r
