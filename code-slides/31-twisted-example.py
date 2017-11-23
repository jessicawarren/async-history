##   <h1 style="valign:center;">Twisted using Deferred</h1>

from twisted.internet.defer import Deferred, inlineCallbacks
from twisted.internet.task import react


def main(reactor):
    """
    :returns: a Deferred that fires when the program is completed
    """

    d = Deferred()

    def done(result):
        print("done")
    d.addCallback(done)

    reactor.callLater(1, d.callback, None)
    print("scheduled callback")
    return d


if __name__ == '__main__':
    react(main)

## show-output
