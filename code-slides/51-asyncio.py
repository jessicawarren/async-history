##   <h1 style="valign:center;">asyncio</h1>

import asyncio

@asyncio.coroutine
def main(loop):

    d = asyncio.Future()

    loop.call_later(1.0, d.set_result, None)
    print("scheduled callback")
    yield from d
    print("done")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
