from msoc import search, engines
import asyncio


async def main():
    async for sound in search(input("Песня: ")):
        print(f"Name: {sound.title}, URL: {sound.url}")


asyncio.run(main())
