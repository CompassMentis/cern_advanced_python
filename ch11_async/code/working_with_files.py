import asyncio

import aiofiles


async def main():
    async with aiofiles.open('data/test.txt') as input_file:
        text = await input_file.read()
    print(text)

asyncio.run(main())
# Output:
# A few lines of text
#
# Some random numbers
# 15
# 2309
# 4902309
