import re
import humanize


RE_SIZE = re.compile(r'^(\d+)([a-z])i?b?$')


class Util:
    def toBytes(s):
        parts = RE_SIZE.search(s.lower().replace(',', ''))
        if not parts:
            raise ValueError("Invalid Input")

        size = parts.group(1)
        suffix = parts.group(2)
        shift = suffix.translate(str.maketrans('kmgtp', '12345')) + '0'

        return int(size) << int(shift)

    def humanReadableSize(b, binary=True, gnu=False):
        return humanize.naturalsize(b, binary, gnu)
