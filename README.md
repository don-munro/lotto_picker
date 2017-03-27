## Uncle Morty's Lotto Picker


With restriction that numbers be in range of 1..59,  we know that each number is made up of either one or two digits.
With this we can see that the following combinations of 1 and 2 digit numbers are possible for a string of len(n):

```
     len(n) |  1 dig. |  2 dig. |
   -------------------------------------
        7   |     7   |   0     |
        8   |     6   |   1     |
        9   |     5   |   2     |
        10  |     4   |   3     |
        11  |     3   |   4     |
        12  |     2   |   5     |
        13  |     1   |   6     |
        14  |     0   |   7     |

```

A couple of details of note from above are:
* A numeric string can only produce the 7 lotto numbers if the length of the string is between 7 and 14 characters.
* The number of 2 digit numbers that must be used in a string of len(n) is `len(n) - 7`

To identify all possible lotto numbers for a given string we note that:
* We must slice the string into a series of 1 and 2 digit numbers.
* We know the number of 1 and 2 digit numbers that are possible for a string of a given length.
* There may be many ways (combinations) that the string can be sliced.
* More than one 'slicing' may result in a valid set of lotto numbers.

# The solution

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

## Running Lotto Picker

The easiest way to run lotto picker is with the following steps:

```
git clone https://github.com/don-munro/lotto_picker.git
cd lotto_picker/lotto_picker
python lotto_picker <list of numeric strings>
```


NB:  This is a streamlined project, void of files that are not required to directly solve
     Uncle Morty's Programming Problem.
