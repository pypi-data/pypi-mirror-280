
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


import unittest
import numpy as np

# kernel class import
from sys import path
path.append('..')
from strkernels import LocalityImprovedStringKernel


class TestKernelMatrix(unittest.TestCase):

    def setUp(self):
        self.kernel = LocalityImprovedStringKernel(normalizer=None, 
                                                   length=0,
                                                   inner_degree=1,
                                                   outer_degree=1)

    def test_empty_strings(self):
        strings = np.array(["", "", ""])
        expected_matrix = np.zeros((3, 3))
        kernel_matrix = self.kernel(strings, strings)
        np.testing.assert_array_equal(kernel_matrix, expected_matrix)

    def test_single_character_strings(self):
        strings = np.array(["A", "T", "A"])
        expected_matrix = np.array([
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ])
        kernel_matrix = self.kernel(strings, strings)
        np.testing.assert_array_equal(kernel_matrix, expected_matrix)

    def test_single_set(self):
        strings = np.array(["ATCG", "ATGG", "TACG", "GCTA"])
        expected_matrix = np.array([
            [16, 9, 4, 0],
            [9, 16, 1, 0],
            [4, 1, 16, 0],
            [0, 0, 0, 16]
        ])
        kernel_matrix = self.kernel(strings, strings)
        np.testing.assert_array_equal(kernel_matrix, expected_matrix)

    def test_two_sets(self):
        strings1 = np.array(["ATCG", "ATGG"])
        strings2 = np.array(["ATCG", "GGGG", "CCCC"])
        expected_matrix = np.array([
            [16, 1, 1],
            [9,  4, 0]
        ])
        kernel_matrix = self.kernel(strings1, strings2)
        np.testing.assert_array_equal(kernel_matrix, expected_matrix)

if __name__ == '__main__':
    unittest.main()
