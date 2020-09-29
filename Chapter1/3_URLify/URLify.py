# O(N)
import unittest


def urlify(string, length):
    s = []
    for i in range(length):
        if string[i] == ' ':
            s.extend(list("%20"))
        else:
            s.append(string[i])
    return s


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22, list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
