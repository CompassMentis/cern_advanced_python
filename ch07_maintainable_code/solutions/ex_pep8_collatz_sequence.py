"""
The Collatz sequence is defined as:

If n is even, divide it by 2 (n → n/2).
If n is odd, multiply it by 3 and add 1 (n → 3n + 1).
Repeat the process with the new value of n, and continue iterating until n becomes 1.
"""

# TODO: This Python script does not quite follow PEP8
#  Fix as many mistakes as you can whilst it still has the .txt extension
#  Things to look out for are:
#  - one space on either side of =, +, -, *, etc
#  - unless in a function call, when there should be no spaces
#  - indentation in multiple of 4 spaces
#  - the script should end with one blank line
#  - snake_case for variable names
#  - no space before a comma, one space after a comma
#  - two blank lines before and after a function definition

# TODO: Now rename this to have a .py extension
#  right click on file name in Project column (left hand)
#  Refactor -> Rename

# TODO: Check for any more PEP8 violations, shown by a grey-ish underscore
#  and fix them

# TODO: Run the code. Make sure it works. The output should be: (97, 119)


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
    longest = None
    for n in range(start, end + 1):
        length = collatz_sequence_length(n)
        if longest is None or (length, n ) > longest:
            longest = (length,n)
    return longest[1], longest[0]


print(longest_collatz_sequence(1, 100))
