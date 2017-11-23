##   <h1 style="valign:center;">Twisted using Deferred</h1>

from twisted.internet.defer import Deferred


def main(reactor):
    """
    :returns: a Deferred that fires when the program is completed
    """

    d = Deferred()
    # ...
    return d
