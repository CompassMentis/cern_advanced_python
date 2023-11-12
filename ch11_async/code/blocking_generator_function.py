import time
import asyncio
import random


def random_numbers(n):
    for _ in range(n):
        time.sleep(1)
        result = random.randint(1, 6)
        yield result


async def show_rolls(n, id):
    for roll in random_numbers(n):
        print(f'{id} rolled {roll}')


async def main():
    coroutines = [show_rolls(3, 'A'), show_rolls(3, 'B')]
    await asyncio.gather(*coroutines)
    print('All done')

asyncio.run(main())

# Output:
# A rolled 1
# A rolled 3
# A rolled 4
# B rolled 4
# B rolled 5
# B rolled 5
# All done
