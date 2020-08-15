from itertools import chain
from typing import Optional


def min_area(x, y, k):
    number_of_points = k

    if k == 1:
        return 4

    x_sorted_by_x, y_sorted_by_x = zip(*sorted(zip(x, y)))
    y_sorted_by_y, x_sorted_by_y = zip(*sorted(zip(y, x)))

    sublists_number = len(x) - number_of_points + 1

    def local_min(lower_index: int, by_x: bool) -> Optional[int]:
        upper_bound = lower_index + number_of_points
        upper_index = upper_bound - 1

        sorted_by = x_sorted_by_x if by_x else y_sorted_by_y
        secondary = y_sorted_by_x if by_x else x_sorted_by_y

        local_diff = sorted_by[upper_index] - sorted_by[lower_index]

        min_secondary = min(secondary[lower_index:upper_bound])
        max_secondary = max(secondary[lower_index:upper_bound])
        all_points_in_square = local_diff >= max_secondary - min_secondary

        if all_points_in_square:
            return local_diff

    min_diff = min(
        chain.from_iterable(
            filter(
                None,
                (
                    local_min(lower_index, by_x)
                    for lower_index in range(sublists_number)
                ),
            )
            for by_x in [True, False]
        )
    )

    return (min_diff + 2) ** 2
