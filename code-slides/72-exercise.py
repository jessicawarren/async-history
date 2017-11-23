##   <h1 style="valign:center;">Coding Exercise</h1>
import json

import asyncio
import aiohttp


async def main(loop):
    # download from a URL
    url = u"https://meejah.ca"

    async with aiohttp.ClientSession(loop=loop) as session:
        req_context = session.get(
            url,
            headers={
                u"User-Agent": u"asyncio",
            }
        )
        async with req_context as response:
            raw_data = await response.text()

    print("Received {} bytes".format(len(raw_data)))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
