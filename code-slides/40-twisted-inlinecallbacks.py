##   <h1 style="valign:center;">Twisted: @inlineCallbacks</h1>
##  <ul class="incremental">
##    <li><tt>@inlineCallbacks</tt> around 2006</li>
##    <li>(ab)uses <tt>yield</tt> to wait</li>
##  </ul>

from twisted.internet.defer import Deferred, inlineCallbacks
from twisted.internet.task import react

@inlineCallbacks
def main(reactor):

    d = Deferred()

    reactor.callLater(1, d.callback, "the result")
    print("scheduled callback")
    result = yield d
    print("done: {}".format(result))


if __name__ == '__main__':
    react(main)

## show-output
