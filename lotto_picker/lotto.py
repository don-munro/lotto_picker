import itertools
import sys

import popcount


def is_numeric(num_str):
    """ Returns an indication of whether the provided string is a number.

    :param num_str:
    :return:
    """
    try:
        int(num_str)
    except Exception:
        return False
    return True

def is_candidate(num):
    """ Determines if the provided string can be used to generate lotto numbers

    A string is deemed capable of being used to generate lotto numbers if the
    string is numeric and has a length such that it can be slice into the
    required number of lotto numbers.

    :param num: A numeric string
    :return: True if the string meets the format requirements.
             False otherwise.
    """
    return is_numeric(num) and (7 <= len(num) <= 14)


class Lotto(object):
    def __init__(self):
        self.numbers_map = {}

    def _get_numbers_for_numeric(self, numeric):

        if not is_candidate(numeric):
            return None

        slices = self._get_slice_counts(numeric)
        lotto_numbers = [self._slice_numeric_string(numeric, mask)
                         for mask in slices]
        lotto_numbers = filter(lambda v: v is not None, lotto_numbers)
        if lotto_numbers:
            self.numbers_map[numeric] = lotto_numbers

    def _get_slice_counts(self, numeric):

        num_dbl_digits = len(numeric) - 7
        masks = popcount.get_pop_counts(num_dbl_digits, 7)
        digit_masks = [[(pop >> i & 1) + 1 for i in range(6, -1, -1)]
                       for pop in masks]
        return digit_masks

    def _slice_numeric_string(self, numeric, digit_counts):
        """ slice the provided numeric string into 7 lotto numbers

        :param numeric: A numeric string that is to be slice into 7 lottery
                        numbers [1..59] as dictated by the provided mask.
        :param digit_counts: A list of 7 integer values [1..2] that identify
                             number of digits each lotto number is to be.

        :return: A list of 7 lotto numbers

        """
        def is_valid():
            return (not as_int in lotto_numbers and
                   (1 <= as_int <= 59))

        lotto_numbers = []
        sliceStart = 0
        for i in range(0, 7):
            sliceEnd = sliceStart + digit_counts[i]
            as_int = int(numeric[sliceStart: sliceEnd])
            if is_valid():
                lotto_numbers.append(as_int)
            else:
                return None

            sliceStart = sliceEnd

        return lotto_numbers

    def print_numbers(self):
        """ Prints the set of lotto numbers that have been identified.

        All sets of lotto numbers for successful strings will be printed with
        the following  example format:

            4938532814754 -> 49 38 53 28 14 7 54, 49 38 53 28 1 47 54
            4938532894754 -> 49 38 53 28 9 47 54

        Note that a comma separated list is used if the numeric string is found
        to support more than one set of lotto numbers.

        """
        for key, lottos in self.numbers_map.items():
            numbers = ', '.join(str(x).strip('[]').replace(',', '')
                                for x in lottos)
            print ("%s -> %s" % (key, numbers))

    def get_lotto(self, numbers):

        gen = (num for num in numbers if is_candidate(num))
        for num in gen:
            slices = self._get_slice_counts(num)
            lotto_numbers = [self._slice_numeric_string(num, mask)
                             for mask in slices]
            lotto_numbers = filter(lambda v: v is not None, lotto_numbers)
            if lotto_numbers:
                self.numbers_map[num] = lotto_numbers



def main(argv):
    if not argv:
        print 'lotto [numeric_string1 numeric_string2 ...]'
        sys.exit(2)

    lotto = Lotto()
    lotto.get_lotto(argv)
    lotto.print_numbers()


if __name__ == '__main__':
    main(sys.argv[1:])