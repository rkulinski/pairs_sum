from collections import defaultdict
from typing import Any


def validate_input(item: Any) -> None:
    if not isinstance(item, int):
        raise TypeError(
            f"Expected integer in list, got {type(item).__name__} with value {item}."
        )


def find_unique_sum_pairs(arr: list[int]) -> dict[int, list[tuple[int, int]]]:
    sum_map = defaultdict(list)
    for item in arr:
        validate_input(item)

    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            pair_sum = arr[i] + arr[j]
            pair = (arr[i], arr[j])
            sum_map[pair_sum].append(pair)

    result = {}
    for pair_sum, pairs in sum_map.items():
        if len(pairs) > 1:
            result[pair_sum] = pairs

    return result


def print_results(input_data: dict[int, list[tuple[int, int]]]) -> None:
    for sum_value in sorted(input_data.keys()):
        pairs_str = " ".join(f"( {x}, {y})" for (x, y) in input_data[sum_value])

        print(f"Pairs : {pairs_str} have sum : {sum_value}\n")
