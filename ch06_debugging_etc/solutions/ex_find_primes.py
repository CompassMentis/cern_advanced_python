import logging
# Todo: Configure a simple logger
#   Output should go to 'find_primes.log'
#   File mode should be wt (write-text)
#   Logging level set at DEBUG
#   Message format consist of: [level] message

# Todo: For is_prime, log at debug level:
#   is_prime or NOT_is_prime, followed by the number

# Todo: For sum_of_digits_is_prime, log at debug level:
#   sum_of_digits_is_prime or NOT_sum_of_digits_is_prime, followed by the number

# Todo: For each number that is printed, log at info level:
#   both, followed by the number

# Todo: Run the code once with logging level at DEBUG and make sure all messages are logged

# Todo: Run the code once with logging level at INFO and make sure only info messages are logged


def is_prime(number):
    if number <= 1:
        logging.debug('NOT_is_prime %s', (number, ))
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            logging.debug('NOT_is_prime %s', (number, ))
            return False
    logging.debug('is_prime %s', (number, ))
    return True


def sum_of_digits_is_prime(number):
    result = is_prime(
        sum(
            int(digit)
            for digit in str(number)
        )
    )
    if result:
        logging.debug('sum_of_digits_is_prime %s', (number,))
    else:
        logging.debug('NOT_sum_of_digits_is_prime %s', (number,))
    return result


logging.basicConfig(filename='find_primes.log', level=logging.INFO, format='[%(levelname)s %(message)s', filemode='wt')


for line in open('large_numbers.txt'):
    if not line.strip():
        continue
    number = int(line)
    if not is_prime(number):
        continue
    if not sum_of_digits_is_prime(number):
        continue
    print(number)
    logging.info('both %s', (number,))
