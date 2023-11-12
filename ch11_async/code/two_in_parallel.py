import asyncio


async def plus_two(x):
    print(f'plus_two({x}) started')
    await asyncio.sleep(1)
    result = x + 2
    print(f'plus_two({x}) done')
    return result


async def main():
    coroutines = [plus_two(5), plus_two(6)]
    await asyncio.gather(*coroutines)
    print('All done')

asyncio.run(main())

# Output:
# plus_two(5) started
# plus_two(6) started
# plus_two(5) done
# plus_two(6) done
# All done
