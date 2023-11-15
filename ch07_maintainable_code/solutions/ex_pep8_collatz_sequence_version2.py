"""
The Collatz sequence is defined as:

If n is even, divide it by 2 (n → n/2).
If n is odd, multiply it by 3 and add 1 (n → 3n + 1).
Repeat the process with the new value of n, and continue iterating until n becomes 1.
"""

# TODO: Make sure you've done ex_pep8_collatz_sequence.py first

# TODO: Rename this file to have a .py extension
#  right click on file name in Project column (left hand)
#  Refactor -> Rename

# TODO: Use Black to format this file into correct PEP8

# TODO: View this file in PyCharm and confirm that there are no more PEP8 violations


def collatz_sequence_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length


def longest_collatz_sequence(start, end):
    Longest = None
    for n in range(start, end + 1):
        length = collatz_sequence_length(n)
        if Longest is None or (length, n) > Longest:
            Longest = (length, n)
    return Longest[1], Longest[0]


print(longest_collatz_sequence(1, 100))
