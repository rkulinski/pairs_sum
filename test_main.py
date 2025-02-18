import unittest
import time
import sys
import random

from main import find_unique_sum_pairs


class TestUniqueSumPairs(unittest.TestCase):
    def dict_of_sets(
        self, d: dict[int, list[tuple[int, int]]]
    ) -> dict[int, set[tuple[int, int]]]:
        """Helper function to compare output."""
        canonical_dict = {}
        for sum_value, pairs in d.items():
            canonical_dict[sum_value] = {tuple(sorted(pair)) for pair in pairs}
        return canonical_dict

    def test_sums(self):
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

        self.assertEqual(self.dict_of_sets(result), self.dict_of_sets(expected_sums))

    def test_sums_unordered(self):
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

        self.assertEqual(self.dict_of_sets(result), self.dict_of_sets(expected_sums))

    def test_empty_array(self):
        arr = []

        result = find_unique_sum_pairs(arr)

        self.assertEqual(result, {})

    def test_single_element(self):
        arr = [42]

        result = find_unique_sum_pairs(arr)

        self.assertEqual(result, {})

    def test_no_repeated_sums(self):
        arr = [1, 2, 3]

        result = find_unique_sum_pairs(arr)

        self.assertEqual(result, {})

    def test_all_zeros(self):
        arr = [0, 0, 0]

        expected_sums = {
            0: [(0, 0), (0, 0), (0, 0)],
        }

        result = find_unique_sum_pairs(arr)

        self.assertEqual(result, expected_sums)

    def test_same_number(self):
        arr = [1, 1, 1]
        expected_sums = {
            2: [(1, 1), (1, 1), (1, 1)],
        }

        result = find_unique_sum_pairs(arr)

        self.assertEqual(result, expected_sums)

    def test_mixed_numbers(self):
        arr = [2, -1, 0, 1]
        expected_sums = {
            1: [(2, -1), (1, 0)],
        }

        result = find_unique_sum_pairs(arr)

        self.assertEqual(self.dict_of_sets(result), self.dict_of_sets(expected_sums))

    def test_unexpected_character(self):
        arr = [2, -1, 0, "a"]

        with self.assertRaises(TypeError):
            find_unique_sum_pairs(arr)

    # -------------------------------------------------------------------
    # Performance / Memory Tests
    # -------------------------------------------------------------------

    # def test_large_input_performance(self):
    #     n = 10000
    #     arr = list(range(n))
    #     start_time = time.perf_counter()
    #
    #     _ = find_unique_sum_pairs(arr)
    #
    #     elapsed_time = time.perf_counter() - start_time
    #     self.assertLess(
    #         elapsed_time,
    #         3.0,
    #         f"Performance test took too long: {elapsed_time} seconds.",
    #     )
    #
    # def test_large_input_memory(self):
    #     n = 10000
    #     arr = list(range(n))
    #
    #     result = find_unique_sum_pairs(arr)
    #
    #     dict_size = sys.getsizeof(result)
    #     self.assertLess(
    #         dict_size,
    #         10_000_000,
    #         f"Memory usage too high for the result: {dict_size} bytes.",
    #     )
    #
    # def test_random_input_performance(self):
    #     random.seed(0)  # Fix seed for consistent test behavior
    #     n = 1000
    #     arr = [random.randint(-1000, 1000) for _ in range(n)]
    #
    #     start_time = time.perf_counter()
    #     _ = find_unique_sum_pairs(arr)
    #     elapsed_time = time.perf_counter() - start_time
    #
    #     self.assertLess(
    #         elapsed_time,
    #         3.0,
    #         f"Random input performance test took too long: {elapsed_time} seconds.",
    #     )


if __name__ == "__main__":
    unittest.main()
