# O(NxN)
import unittest


def rotate_matrix(m):
    n = len(m)
    top, bot = 0, n - 1
    left, right = 0, n - 1

    while top < bot and left < right:
        # 1. SAVE ALL 4 ROWS ROW
        top_row = m[top][left:right + 1]
        bot_row = m[bot][left:right + 1][::-1]
        left_row = [m[i][left] for i in range(top, bot + 1)][::-1]
        right_row = [m[i][right] for i in range(top, bot + 1)]

        # LEFT TO TOP
        for i in range(n):
            m[top][left + i] = left_row[i]

        # TOP TO RIGHT
        for i in range(1, n):
            m[top + i][right] = top_row[i]

        # RIGHT TO BOT
        for i in range(1, n):
            m[bot][right - i] = right_row[i]

        # BOT TO LEFT
        for i in range(1, n):
            m[bot - i][left] = bot_row[i]

        n -= 2
        top += 1
        bot -= 1
        left += 1
        right -= 1

    return m


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([
             [1, 2, 3, 4, 5],
             [6, 7, 8, 9, 10],
             [11, 12, 13, 14, 15],
             [16, 17, 18, 19, 20],
             [21, 22, 23, 24, 25]
         ], [
             [21, 16, 11, 6, 1],
             [22, 17, 12, 7, 2],
             [23, 18, 13, 8, 3],
             [24, 19, 14, 9, 4],
             [25, 20, 15, 10, 5]
         ])
    ]

    def test_rotate_matrix(self):
        for [test_matrix, expected] in self.data:
            actual = rotate_matrix(test_matrix)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
