# Todo: Create a new module, 'tests_for_functions.py'

# Todo: Import this module

# Todo: Make a list of everything which you could/should test for each function

# Todo: Now create at least 2 tests per function

# Todo: Include at least one parameterised test

# Todo: One of the functions has a deliberate error.
#   Make sure you have a test which fails because of the error

# Todo: Now fix the error and check that the test now passes

def find_primes_in_range(start, end):
    primes = []
    for number in range(start, end + 1):
        if number > 1:
            for i in range(2, int(number**0.5) + 1):
                if number % i == 0:
                    break
            else:
                primes.append(number)
    return primes


def remove_duplicates_preserve_order(lst):
    unique_items = set()
    for item in lst:
        if item not in unique_items:
            unique_items.add(item)
    return unique_items
