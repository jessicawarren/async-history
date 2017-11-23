##   <h1 style="valign:center;">Coding Exercise</h1>

import treq

from twisted.internet.defer import Deferred, ensureDeferred
from twisted.internet.task import react
from twisted.web.client import readBody


async def main(reactor):
    # download from a URI
    uri = u"https://meejah.ca"
    response = await treq.get(
        uri,
        headers={
            b"User-Agent": [b"Twisted"],
        }
    )
    # download the reply
    raw_data = await readBody(response)
    print("Received {} bytes".format(len(raw_data)))


if __name__ == '__main__':
    def _main(reactor):
        return ensureDeferred(main(reactor))
    react(_main)
