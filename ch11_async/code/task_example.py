import asyncio


async def plus_two(x):
    print(f'plus_two({x}) started')
    await asyncio.sleep(1)
    result = x + 2
    print(f'plus_two({x}) done')
    return result


async def main():
    tasks = [
        asyncio.Task(plus_two(5)),
        asyncio.Task(plus_two(6))
        ]
    print('Tasks created')
    await asyncio.sleep(2)
    print('Done sleeping, starting to gather')
    await asyncio.gather(*tasks)
    print('All done')

asyncio.run(main())

# Output:
# Tasks created
# plus_two(5) started
# plus_two(6) started
# plus_two(5) done
# plus_two(6) done
# Done sleeping, starting to gather
# All done
