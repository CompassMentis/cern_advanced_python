# TODO: Use mypy to check this, using
#  mypy ex_type_hints_find_primes --strict

# TODO: Add type hints until mypy no longer reports any errors

def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def sum_of_digits_is_prime(number: int) ->bool:
    return is_prime(
        sum(
            int(digit)
            for digit in str(number)
        )
    )


for line in open('large_numbers.txt'):
    if not line.strip():
        continue
    number = int(line)
    if not is_prime(number):
        continue
    if not sum_of_digits_is_prime(number):
        continue
    print(number)
