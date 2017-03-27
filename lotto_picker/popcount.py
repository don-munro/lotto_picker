"""
Provides a utility functions for generating binary permutations in 'Popcount'
order as credited to Alex Bowe at http://alexbowe.com/popcount-permutations/.

"""
def get_pop_counts(count, size):

    def element_0(c):
        """Generates first permutation with a given amount
           of set bits, which is used to generate the rest."""
        return (1 << c) - 1

    def next_perm(v):
        """
        Generates next permutation with a given amount of set bits,
        given the previous lexicographical value.
        Taken from http://graphics.stanford.edu/~seander/bithacks.html
        """
        t = (v | (v - 1)) + 1
        w = t | ((((t & -t) / (v & -v)) >> 1) - 1)
        return w

    def gen_blocks(p, b):
        """
        Generates all blocks of a given popcount and blocksize
        """
        v = initial = element_0(p)
        block_mask = element_0(b)

        while (v >= initial):
            yield v
            v = next_perm(v) & block_mask

    if count == 0:
        pop_counts = [0]
    else:
        pop_counts = [x for x in gen_blocks(count, size)]
    return pop_counts


def get_bin_pop_counts(count, size):

    def to_bin(x, digits=0):
        # https://lists.gt.net/python/python/645216
        oct2bin = ['000','001','010','011','100','101','110','111']
        binstring = [oct2bin[int(n)] for n in oct(x)]
        return ''.join(binstring).lstrip('0').zfill(digits)

    pop_counts = get_pop_counts(count, size)
    bin_counts = [to_bin(bin_count, size) for bin_count in pop_counts]

    return bin_counts