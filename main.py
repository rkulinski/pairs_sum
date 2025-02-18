from collections import defaultdict
from typing import Any
from itertools import combinations


def validate_input(item: Any) -> None:
    if not isinstance(item, int):
        raise TypeError(
            f"Expected integer in list, got {type(item).__name__} with value {item}."
        )


def find_unique_sum_pairs(arr: list[int]) -> dict[int, list[tuple[int, int]]]:
    for item in arr:
        validate_input(item)

    sum_map = defaultdict(list)
    for x, y in combinations(arr, 2):
        sum_map[x + y].append((x, y))

    return {paris_sum: pairs for paris_sum, pairs in sum_map.items() if len(pairs) > 1}


def print_results(input_data: dict[int, list[tuple[int, int]]]) -> None:
    for sum_value in sorted(input_data.keys()):
        pairs_str = " ".join(f"({x}, {y})" for (x, y) in input_data[sum_value])

        print(f"Pairs : {pairs_str} have sum : {sum_value}")


if __name__ == "__main__":
    # Sample run
    pairs = find_unique_sum_pairs([6, 4, 12, 10, 22, 54, 32, 42, 21, 11])
    print_results(pairs)
