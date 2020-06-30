def fixedsplit(text, separator=None, maxsplit=-1):
    """Split a string and return a fixed number of parts"""
    parts = text.split(separator, maxsplit)
    maxparts = maxsplit + 1
    missing = maxparts - len(parts)
    if missing > 0:
        parts = parts + (missing * [""])
    return parts


def pairs(items):
    return zip(items[:-1], items[1:])


def wrapped_pairs(items):
    return zip(items, items[1:] + items[:1])
