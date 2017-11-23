##   <h1 style="valign:center;">async def, await</h1>

from twisted.internet.defer import ensureDeferred, Deferred
from twisted.internet.task import react

async def main(reactor):

    d = Deferred()

    reactor.callLater(1, d.callback, None)
    print("scheduled callback")
    await d
    print("done")


if __name__ == '__main__':
    def _main(reactor):
        return ensureDeferred(main(reactor))
    react(_main)

## show-output
