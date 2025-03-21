def create_stats():
    numbers = []

    def stats(number):
        numbers.append(number)
        return dict(
            minimum=min(numbers),
            maximum=max(numbers)
        )
    return stats


my_stats = create_stats()
for number in 4, 1, 2, 5, 7, 3:
    print(number, my_stats(number))
