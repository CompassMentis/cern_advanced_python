numbers = [1, 2, 7, 15]

# Start of manual for loop
numbers_iterator = iter(numbers)
while True:
    try:
        number = next(numbers_iterator)
    except StopIteration:
        break

    # Start of for loop's code block
    print(number, 'x 5 =', number * 5)
    print('-------')

# Output:
# 1 x 5 = 5
# -------
# 2 x 5 = 10
# -------
# 7 x 5 = 35
# -------
# 15 x 5 = 75
# -------
