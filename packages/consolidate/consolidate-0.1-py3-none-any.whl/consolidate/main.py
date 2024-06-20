def generate(base, length, fill = "‌",):
    """
    Returns a list of possible consolidations.

    :param str baseString: String to put fillerString within
    :param int maxLength: Max length of result string
    :param str fillerChar : Character to consolidate with base, default is a ZWNJ
    :return: List of combinations
    :rtype: list
    """
    loc = []
    if len(base)==length:
        return [base]
    if len(base)<length:
        for i in range(len(base)+1):
            loc.append(base[:i] + fill + base[i:])
    loc2 = [base]
    for w in loc:
        loc2.extend(generate(w, length, fill))
    loc.extend(loc2)
    return set(sorted(loc))
    # maybe add a "must match max length" bool as an input if user requires exact length, no less
    # add a warning if l - len(base) is > n to prevent huge run time 


def count(base, length, fill = "‌",):
    """
    Returns the total amount of consolidations possible.a

    :param str baseString: String to put fillerString within
    :param int maxLength: Max length of result string
    :param str fillerString : String to put within baseString
    :return: List of combinations
    :rtype: list
    """
    # n = length - len(base) - len(fill)
    return "unfinished method, will finish by tomorrow!" # n*(n+1)/2