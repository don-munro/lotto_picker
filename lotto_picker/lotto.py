import itertools
import sys


MIN_NUM = 1
MAX_NUM = 59
NUMS_PER_TICKET = 7
MIN_STR_LEN = NUMS_PER_TICKET
MAX_STR_LEN = NUMS_PER_TICKET*2


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
    return is_numeric(num) and (MIN_STR_LEN <= len(num) <= MAX_STR_LEN*2)


class Lotto(object):
    def __init__(self):
        self.numbers_map = {}

    def _get_slice_counts(self, numeric):
        num_dbl_digits = len(numeric) - NUMS_PER_TICKET
        combos = itertools.combinations(range(NUMS_PER_TICKET), num_dbl_digits)
        # convert each 'combo' into a list of NUM_NUMBERS values that can be
        # used directly to slice the provided string.
        slices = [[2 if i in combo else 1 for i in range(0, NUMS_PER_TICKET)]
                  for combo in combos]

        return slices

    def _slice_numeric(self, numeric, slice_counts):
        """Slice the provided numeric string into 7 lotto numbers.

        :param numeric: A numeric string that is to be sliced into 7 lottery
                        numbers [1..59] as dictated by the slice_counts list.
        :param slice_counts: A list of 7 integer values [1..2] that provides
                             an order list of how numeric should be sliced.

        :return: A list of 7 lotto numbers if the slice produced a valid set
                 of numbers otherwise returns None.

        """
        def is_valid():
            return (as_int not in lotto_numbers and
                    (MIN_NUM <= as_int <= MAX_NUM))

        lotto_numbers = []
        slice_start = 0
        for i in range(0, NUMS_PER_TICKET):
            slice_end = slice_start + slice_counts[i]
            as_int = int(numeric[slice_start: slice_end])
            if is_valid():
                lotto_numbers.append(as_int)
            else:
                return None

            slice_start = slice_end

        return lotto_numbers

    def check_numeric_strings(self, numbers):
        """Check the given numeric strings for possible lotto numbers.

        :param numbers: A list of numeric strings

        :return: The updated map that identifies a list of lotto numbers for
                 successful strings.
        """
        filter_gen = (num for num in numbers
                      if is_candidate(num) and not self.numbers_map.get(num))
        for num in filter_gen:
            slices = self._get_slice_counts(num)
            slice_gen = (self._slice_numeric(num, mask) for mask in slices)
            lotto_numbers = [nums for nums in slice_gen if nums]
            if lotto_numbers:
                self.numbers_map[num] = lotto_numbers

        return self.numbers_map

    def print_numbers(self):
        """Prints the set of lotto numbers that have been identified.

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


def main(argv):
    if not argv:
        print 'lotto [numeric_string1 numeric_string2 ...]'
        sys.exit(2)

    lotto = Lotto()
    lotto.check_numeric_strings(argv)
    lotto.print_numbers()


if __name__ == '__main__':
    main(sys.argv[1:])
