def find_unique_sum_pairs(arr: list[int]) -> dict[int, list[tuple[int, int]]]:
    sums = {}

    n = len(arr)
    for i in range(n):
        validate_input(arr[i])
        for j in range(i + 1, n):
            validate_input(arr[j])

    return sums


def print_results(input: dict[int, list[tuple[int, int]]]) -> None:
    pass


def validate_input(item: Any) -> None:
    if not isinstance(item, int):
        raise TypeError(
            f"Expected integer in list, got {type(item).__name__} with value {item}."
        )
