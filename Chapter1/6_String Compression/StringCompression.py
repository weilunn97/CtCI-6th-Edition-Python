# O(N)
import unittest


def string_compression(string):
    if not string:
        return ""
    char, count = string[0], 0
    chars, counts = [], []

    for s in string:
        if s == char:
            char = s
            count += 1
        else:
            chars.append(char)
            counts.append(str(count))
            char = s
            count = 1
    chars.append(char)
    counts.append(str(count))
    final = [(char, count) for char, count in zip(chars, counts)]
    final = ''.join([f for ff in final for f in ff])
    return final if len(final) < len(string) else string


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
