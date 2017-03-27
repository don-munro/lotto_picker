## Uncle Morty's Lotto Picker

## Running Lotto Picker

The easiest way to run lotto picker is with the following steps:

```
cd $YOUR_WORK_DIR
git clone https://github.com/don-munro/lotto_picker.git
cd lotto_picker/lotto_picker
python lotto <list of numeric strings>
```

## Running Test Cases
A small number of unit tests have been included in recognition that good test habits lead to good code.
To run the test cases:

```
cd $YOUR_WORK_DIR\lotto_picker
python setup.py test
```

## Notes

With restriction that numbers be in range of 1..59,  we know that each number is made up of either one or two digits.
With this we can see that the following combinations of 1 and 2 digit numbers are possible for a string of len(n):

```
     len(n) |  1 dig. |  2 dig. | # combos
   ---------------------------------------
        7   |     7   |   0     |   1
        8   |     6   |   1     |   7
        9   |     5   |   2     |   21
        10  |     4   |   3     |   35
        11  |     3   |   4     |   35
        12  |     2   |   5     |   21
        13  |     1   |   6     |   7
        14  |     0   |   7     |   1

```

A couple of details of note from above are:
* A numeric string can only produce the 7 lotto numbers if the length of the string is between 7 and 14 characters.
* The number of 2 digit numbers that must be used in a string of len(n) is `len(n) - 7`

To identify all possible lotto numbers for a given string we note that:
* We must slice the string into a series of 1 and 2 digit numbers.
* We know the number of 1 and 2 digit numbers that are possible for a string of a given length.
* There may be many ways (combinations) that the string can be sliced.
* More than one 'slicing' may result in a valid set of lotto numbers.

## The solution

The solution at hand here :
* Maintains a string-to-numbers map that identifies a set of valid lotto numbers that can be gleaned from a
  given string.  Only strings that produce valid lotto numbers are found in this map.
* For a given string, check the string-to-numbers map and ignore the current string if we have seen it before. If
  we have not seen it:
    * Finds all combination of 1 and 2 digit numbers for the string.
    * For each combination slice the string into candidate numbers validating each as the slice is being performed.
    * Update string-to-numbers to include all (valid) lotto numbers that were identified for the string.
* Cycle though all provided strings

When executed directly lotto_picker will also print the results.

## Algorithm Analysis

From an efficiencey point of view this solution is fairly straight forward in how results are generated.
Using psuedocode to demonstrate we have:

  ```
     for each provided string:
        get ways(combos) to string can be sliced
        for each way
           slice and check if we have a valid set of numbers
  ```

A few points to highlight:
* Finding the ways to split a string is simple call to create the generator.
* The number of combinations of 2 and 1 digit numbers that can make up a set of 7 lotto numbers can be calculated as a
  'n choose r' problem such that nCr = n!/r!(n - r)! where n is fixed at 7 (the number of numbers) and r is the number
  of two digit numbers in the set of 7 numbers. Our worse case scenario occurs when r=3 and r=4 where nCr=35 which
  provides constant time.
* We slice each string 7 times (less if we find an invalid number) and each slice is done in O(k) where k is the
  size of the slice and  1 <= k <= 2

Printing the final results requires we iterate over the full result set (map) and print the list of lott numbers.
This does come with some overhead in order to format the output as required.


### Efficiency changes and notes:
* As an improvement, I actually started off using an approach for 'Generating Binary Permutations in Popcount order'
  which was something I stumbled across recently. It seemed like a good approach and worked as expected but I clued
  in a bit that Python's itertools might just provide a better option with combinations. A quick test showed it was
  more than 5x more efficient so I bailed on the use of Popcounts. I'll admit that cute idea was not so cute after all.
  (reference: http://alexbowe.com/popcount-permutations/)
* A change I considered to improve the efficiency with which lotto numbers can be printed was to build up the map of
  successful numbers using strings as the values instead of the list of integers I currently use.  In the end I'll note
  that my Uncle Morty has plans to perform analytics on all discovered lotto numbers and chose to accept the overhead of
  stripping chars and printing the list of ints.
* One could also consider the fact that the masks that are used to slice the strings are essentially fixed. A new mask
  is generated for every string that is parsed but we could instead generate the masks once and persist/save them for
  easy access.

NB:  This is a streamlined project, void of files that are not required to directly solve
     Uncle Morty's Programming Problem.
