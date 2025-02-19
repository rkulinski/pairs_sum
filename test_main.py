"""
Tests for the find_unique_sum_pairs function.
"""

import random
import time
from typing import cast

import pytest

from main import UniqueSumsOutput, find_unique_sum_pairs


def dict_of_sets(d: UniqueSumsOutput) -> dict[int, set[tuple[int, int]]]:
    """Convert dict values to sets of sorted tuples."""
    canonical_dict = {}
    for sum_value, pairs in d.items():
        canonical_dict[sum_value] = {
            cast(tuple[int, int], tuple(sorted(pair))) for pair in pairs
        }
    return canonical_dict


def test_sums():
    """Test correct sums."""
    arr = [6, 4, 12, 10, 22, 54, 32, 42, 21, 11]
    expected_sums = {
        16: [(4, 12), (6, 10)],
        32: [(10, 22), (21, 11)],
        33: [(12, 21), (22, 11)],
        43: [(22, 21), (32, 11)],
        53: [(32, 21), (42, 11)],
        54: [(12, 42), (22, 32)],
        64: [(10, 54), (22, 42)],
    }

    result = find_unique_sum_pairs(arr)

    assert dict_of_sets(result) == dict_of_sets(expected_sums)


@pytest.mark.xfail(
    reason="Expected failure due to incorrect expected sums.", strict=True,
)
def test_fail_on_incorrect_sums():
    """Test failure with incorrect expected sums."""
    arr = [6, 4, 12, 10, 22, 54, 32, 42, 21, 11]
    expected_sums = {
        16: [(4, 12), (6, 10)],
        32: [(10, 22)],  # Incorrect: should be [(10, 22), (21, 11)]
        33: [(12, 21), (22, 11)],
        43: [(22, 21), (32, 11)],
        53: [(32, 21), (42, 11)],
        54: [(12, 42), (22, 32)],
        64: [(10, 54), (22, 42)],
    }

    result = find_unique_sum_pairs(arr)

    assert dict_of_sets(result) == dict_of_sets(expected_sums)


def test_sums_unordered():
    """Test sums with unordered pairs."""
    arr = [6, 4, 12, 10, 22, 54, 32, 42, 21, 11]
    expected_sums = {
        32: [(10, 22), (21, 11)],
        33: [(12, 21), (22, 11)],
        16: [(4, 12), (10, 6)],
        54: [(22, 32), (12, 42)],
        43: [(22, 21), (32, 11)],
        53: [(32, 21), (42, 11)],
        64: [(10, 54), (22, 42)],
    }

    result = find_unique_sum_pairs(arr)

    assert dict_of_sets(result) == dict_of_sets(expected_sums)


def test_empty_array():
    """Test empty array returns empty dict."""
    arr = []
    result = find_unique_sum_pairs(arr)
    assert result == {}


def test_single_element():
    """Test single element returns empty dict."""
    arr = [42]

    result = find_unique_sum_pairs(arr)

    assert result == {}


def test_no_repeated_sums():
    """Test array with no repeated sums returns empty dict."""
    arr = [1, 2, 3]

    result = find_unique_sum_pairs(arr)

    assert result == {}


def test_all_zeros():
    """Test all zeros."""
    arr = [0, 0, 0]
    expected_sums = {0: [(0, 0), (0, 0), (0, 0)]}

    result = find_unique_sum_pairs(arr)

    assert result == expected_sums


def test_same_number():
    """Test array with identical numbers."""
    arr = [1, 1, 1]
    expected_sums = {2: [(1, 1), (1, 1), (1, 1)]}

    result = find_unique_sum_pairs(arr)

    assert result == expected_sums


def test_mixed_numbers():
    """Test mixed positive and negative numbers."""
    arr = [2, -1, 0, 1]
    expected_sums = {1: [(2, -1), (1, 0)]}

    result = find_unique_sum_pairs(arr)

    assert dict_of_sets(result) == dict_of_sets(expected_sums)


def test_unexpected_character():
    """Test array with an unexpected string character."""
    arr = [2, -1, 0, "a"]

    with pytest.raises(TypeError):
        find_unique_sum_pairs(arr)


def test_performance_scaling():
    """Test performance scaling between small and large arrays."""
    n_small = 5000
    n_large = 10000
    arr_small = [random.randint(-1000, 1000) for _ in range(n_small)]
    arr_large = [random.randint(-1000, 1000) for _ in range(n_large)]

    start_small = time.perf_counter()
    _ = find_unique_sum_pairs(arr_small)
    time_small = time.perf_counter() - start_small
    start_large = time.perf_counter()
    _ = find_unique_sum_pairs(arr_large)
    time_large = time.perf_counter() - start_large
    ratio = time_large / time_small

    assert ratio < 6, (f"Scaling ratio {ratio:.2f} "
                       f"(5k: {time_small:.2f}s, 10k: {time_large:.2f}s)")
