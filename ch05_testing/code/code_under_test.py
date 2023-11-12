def get_median(numbers):
    numbers.sort()
    if len(numbers) % 2:
        # Odd number of numbers, take middle one
        return numbers[len(numbers) // 2]

    # Even number of numbers, take average of two middle ones
    return (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
