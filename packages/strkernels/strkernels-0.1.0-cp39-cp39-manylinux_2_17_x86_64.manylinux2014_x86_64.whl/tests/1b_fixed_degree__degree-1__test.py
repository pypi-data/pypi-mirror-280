
# Author: Denilson Fagundes Barbosa, denilsonfbar@gmail.com


import unittest
import numpy as np

# kernel class import
from sys import path
path.append('..')
from strkernels import FixedDegreeStringKernel


class TestKernelMatrix(unittest.TestCase):

    def setUp(self):
        self.kernel = FixedDegreeStringKernel(degree=1)

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
            [1,    0.75,  0.5,    0],
            [0.75,    1, 0.25,    0],
            [0.5,  0.25,    1,    0],
            [0  ,     0,    0,    1]
        ])
        kernel_matrix = self.kernel(strings, strings)
        np.testing.assert_array_equal(kernel_matrix, expected_matrix)

    def test_two_sets(self):
        strings1 = np.array(["ATCG", "ATGG"])
        strings2 = np.array(["ATCG", "GGGG", "CCCC"])
        expected_matrix = np.array([
            [1,    0.25, 0.25],
            [0.75, 0.5,     0]
        ])
        kernel_matrix = self.kernel(strings1, strings2)
        np.testing.assert_array_equal(kernel_matrix, expected_matrix)

if __name__ == '__main__':
    unittest.main()
