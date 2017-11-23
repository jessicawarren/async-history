##   <h1 style="valign:center;">Deferred</h1>

from twisted.internet.defer import Deferred

#!
d = Deferred()

#!
def cb(result):
    print("result: {}".format(result))
d.addCallback(cb)

#!
d.callback("the result")

## show-output
