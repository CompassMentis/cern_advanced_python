import asyncio


async def hello_world():
    print('Hello World!')
    await asyncio.sleep(1)
    print('Done')

asyncio.run(hello_world())

# Output
# Hello World!
# Done
