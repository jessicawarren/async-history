##   <h1 style="valign:center;">async def, await</h1>

import asyncio

async def main(loop):

    d = asyncio.Future()

    loop.call_later(1, d.set_result, None)
    print("scheduled callback")
    await d
    print("done")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))

## show-output
