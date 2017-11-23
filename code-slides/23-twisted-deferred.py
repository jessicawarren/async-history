##   <h1 style="valign:center;">Deferred</h1>

from twisted.internet.defer import Deferred

#!
d = Deferred()

#!
def err(fail):
    print("error: {}".format(fail.value))
d.addErrback(err)

#!
try:
    1 / 0
except Exception:
    d.errback()

## show-output
