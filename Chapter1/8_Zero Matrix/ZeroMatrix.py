# O(MxN)
import unittest


def zero_matrix(m):
    nrows, ncols = len(m), len(m[0])
    zero_in_row0 = 0 in m[0]
    zero_in_col0 = 0 in [m[i][0] for i in range(nrows)]

    for i in range(nrows):
        for j in range(ncols):
            if m[i][j] == 0 and i != 0 and j != 0:
                m[i][0] = 0
                m[0][j] = 0

    for i in range(1, nrows):
        if m[i][0] == 0:
            set_row_zero(m, i)

    for j in range(1, ncols):
        if m[0][j] == 0:
            set_col_zero(m, j)

    if zero_in_row0: set_row_zero(m, 0)
    if zero_in_col0: set_col_zero(m, 0)
    return m


def set_row_zero(m, row):
    m[row] = [0] * len(m[0])


def set_col_zero(m, col):
    for i in range(len(m)):
        m[i][col] = 0


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
             [1, 2, 3, 4, 0],
             [6, 0, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 0, 18, 19, 20],
             [21, 22, 23, 24, 25]
         ], [
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [11, 0, 13, 14, 0],
             [0, 0, 0, 0, 0],
             [21, 0, 23, 24, 0]
         ])
    ]

    def test_zero_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = zero_matrix(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
