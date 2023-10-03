import aiofiles
import asyncio
import datetime
import sys


from get_files import get_file_names


async def read_file(filename):
    print(filename)
    async with aiofiles.open(filename, mode='rb') as file:
        while True:
            await asyncio.sleep(0.001)
            data = await file.read(1024)
            if not data:
                print(filename, "done ###############")
                break


async def main():
    begin = datetime.datetime.now()
    files = get_file_names(sys.argv)
    tasks = [asyncio.create_task(read_file(file)) for file in files]
    for future in asyncio.as_completed(tasks):
        await future
    print(datetime.datetime.now() - begin)


asyncio.run(main())