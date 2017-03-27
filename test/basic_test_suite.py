import unittest
from lotto_picker import lotto


class LottoTests(unittest.TestCase):

    def setUp(self):
        self.lotto_picker = lotto.Lotto()

    def test_with_chars(self):
        # ensures non-numeric strings are ignored.
        picker = lotto.Lotto()
        numbers_map = picker.check_number_strings(['bogusString', '1234567'])
        self.assertTrue(numbers_map.get('1234567'))
        self.assertFalse(numbers_map.get('bogusString'))

    def test_multiple_lottos(self):
        # ensures that all possible lotto numbers are produced from a string
        # that is capable of producing > 1 set of numbers.
        picker = lotto.Lotto()
        numbers_map = picker.check_number_strings(['4938532814754'])
        length = len(numbers_map.get('4938532814754'))
        self.assertTrue(length == 2)

    def test_repeated_numbers(self):
        # ensures that a string does not generate a set of lotto numbers with
        # duplicate numbers.
        picker = lotto.Lotto()
        numbers_map = picker.check_number_strings(['1234123'])
        self.assertFalse(numbers_map.get('1234123'))

    def test_too_long_too_short(self):
        # ensures that strings that are too short or too long are ignored.
        picker = lotto.Lotto()
        numbers_map = picker.check_number_strings(['123456', '123456789123456'])
        self.assertFalse(numbers_map)

    def test_iterative_scan(self):
        # ensures Lotto instance can be used in an iterative way to check more
        # than one list of numbers.
        picker = lotto.Lotto()
        numbers_map = picker.check_number_strings(['1234567'])
        numbers_map = picker.check_number_strings(['4938532814754'])
        self.assertTrue(len(numbers_map) == 2)

if __name__ == '__main__':
    unittest.main()