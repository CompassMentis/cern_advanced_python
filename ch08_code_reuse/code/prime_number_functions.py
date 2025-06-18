def is_prime(number):
    for n in range(2, number):
        if number % 2 == 0:
            return False
    return True

def list_primes(number_range):
    return [
        n
        for n in number_range
        if is_prime(n)
    ]

def main():
    for n in range(1, 10):
        print(n, is_prime(n))
    print(list_primes(range(10, 30)))

# Only run this code directly,
# not when this module is imported
if __name__ == '__main__':
    main()
