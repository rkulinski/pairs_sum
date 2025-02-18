from collections import defaultdict
from itertools import combinations
from typing import Any


def validate_input(item: Any) -> None:
    """Accept only integers values."""
    if not isinstance(item, int):
        raise TypeError(
            f"Expected integer in list, got {type(item).__name__} with value {item}."
        )


def find_unique_sum_pairs(arr: list[int]) -> dict[int, list[tuple[int, int]]]:
    """Identify unique sum pairs from a list of integers.

    Given a list of integers, this function finds all pairs of numbers whose sum
    appears more than once. For example, with the input:

        [4, 23, 65, 67, 24, 12, 86]

    the function will identify that the pairs (4, 86) and (23, 67) both sum to 90,
    and return these pairs associated with the sum 90.
    """
    for item in arr:
        validate_input(item)

    sum_map = defaultdict(list)
    for x, y in combinations(arr, 2):
        sum_map[x + y].append((x, y))

    return {paris_sum: pairs for paris_sum, pairs in sum_map.items() if len(pairs) > 1}


def print_results(input_data: dict[int, list[tuple[int, int]]]) -> None:
    """Print results in the desired format.

    Examples:
        Pairs : (4, 12) (6, 10) have sum : 1
        Pairs : (10, 22) (21, 11) have sum : 32
    """
    for sum_value in sorted(input_data.keys()):
        pairs_str = " ".join(f"({x}, {y})" for (x, y) in input_data[sum_value])

        print(f"Pairs : {pairs_str} have sum : {sum_value}")


if __name__ == "__main__":
    # Sample run
    pairs = find_unique_sum_pairs([6, 4, 12, 10, 22, 54, 32, 42, 21, 11])
    print_results(pairs)
