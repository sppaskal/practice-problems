"""
Start with first string as potential common prefix
and keep checking against following strings, removing
a character from prefix and rechecking against each
string until a common prefix is found before moving
to next string.
"""


def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    if not strs:
        return ""

    prefix = strs[0]

    for string in strs[1:]:
        while string[:len(prefix)] != prefix and prefix:
            prefix = prefix[:-1]

        if not prefix:
            break

    return prefix
