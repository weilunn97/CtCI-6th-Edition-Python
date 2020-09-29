# O(N)
import unittest
from collections import Counter
from heapq import heappop, heapify, heappush


def pal_perm(phrase):
    phrase = phrase.lower().replace(' ', '')
    min_heap = [v & 1 for v in Counter(phrase).values()]
    return sum(min_heap) <= 1


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
