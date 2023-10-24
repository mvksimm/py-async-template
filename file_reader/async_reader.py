import aiofiles
import asyncio
import datetime


from get_files import get_file_names


async def read_file(filename):
    print(filename)
    async with aiofiles.open(filename, mode='rb') as file:
        while True:
            # await asyncio.sleep(0.001)
            data = await file.read(1024)

            if not data:
                print(filename, "done ###############")
                break


async def main():
    begin = datetime.datetime.now()
    tasks = [asyncio.create_task(read_file(file)) for file in get_file_names()]
    for future in asyncio.as_completed(tasks):
        await future
    print(datetime.datetime.now() - begin)


asyncio.run(main())
