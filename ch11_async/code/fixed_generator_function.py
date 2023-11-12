import asyncio
import random


async def random_numbers(n):
    for _ in range(n):
        await asyncio.sleep(1)
        result = random.randint(1, 6)
        yield result


async def show_rolls(n, id):
    async for roll in random_numbers(n):
        print(f'{id} rolled {roll}')


async def main():
    coroutines = [show_rolls(3, 'A'), show_rolls(3, 'B')]
    await asyncio.gather(*coroutines)
    print('All done')

asyncio.run(main())

# Output:
# A rolled 3
# B rolled 4
# A rolled 6
# B rolled 1
# A rolled 4
# B rolled 1
# All done