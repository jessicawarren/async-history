import json
import treq

from twisted.internet.defer import Deferred, inlineCallbacks, ensureDeferred
from twisted.internet.task import react
from twisted.web.client import readBody


async def main(reactor):
    """
    resolves when the program is completed
    """
    response = await treq.get(
        u'https://api.github.com/orgs/py-yyc/repos',
        headers={
            b"User-Agent": [b"Twisted"],
        }
    )
    raw_data = await readBody(response)
    print("Received {} bytes.".format(len(raw_data)))
    print("{}...".format(raw_data[:76]))
    # ... process data


if __name__ == '__main__':
    react(lambda r: ensureDeferred(main(r)))
