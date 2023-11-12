import timeit

number_of_numbers = 100_000


def version5():
    return ''.join(
        str(i) for i in range(number_of_numbers)
    )


def version2():
    numbers = list(range(number_of_numbers))
    numbers_as_strings = [str(i) for i in numbers]
    result = ''.join(numbers_as_strings)
    return result


def version1():
    result = ''
    for i in range(number_of_numbers):
        result += str(i)
    return result


def version3():
    numbers = []
    i = 0
    while i < number_of_numbers:
        numbers.append(str(i))
        i += 1
    result = ''.join(numbers)
    return result

### (column break)

def version3a():
    numbers = []
    i = 0
    while i < number_of_numbers:
        numbers.insert(0, str(i))
        i += 1
    result = ''.join(numbers)
    return result


def version4():
    def add_number(result_so_far, number):
        return result_so_far + str(number)
    result = ''
    for i in range(number_of_numbers):
        result = add_number(result, i)
    return result


for function_name in ('version1', 'version2', 'version3', 'version4', 'version5'):
    print(
        function_name,
        timeit.timeit(
            stmt=f'{function_name}()',
            setup=f'from __main__ import {function_name}',
            number=10,
        )
    )
