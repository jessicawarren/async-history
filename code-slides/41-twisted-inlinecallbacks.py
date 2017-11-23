##   <h1 style="valign:center;">Twisted: @inlineCallbacks</h1>
##  <ul class="incremental">
##    <li>mark async functions</li>
##    <li>nicer to read</li>
##    <li>(linear, like threaded code)</li>
##  </ul>

from twisted.internet.defer import Deferred, inlineCallbacks
from twisted.internet.task import react

@inlineCallbacks
def main(reactor):

    d = Deferred()

    reactor.callLater(1, d.callback, None)
    print("scheduled callback")
    yield d
    print("done")


if __name__ == '__main__':
    react(main)
