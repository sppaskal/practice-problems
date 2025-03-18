"""
In this solution we use a sliding window
technique to check for the first occurance
of needle.
"""


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """

    if needle not in haystack:
        return -1

    needle_len = len(needle)
    haystack_len = len(haystack)
    i = 0
    while i <= (haystack_len - needle_len):
        if haystack[i:i + needle_len] == needle:
            return i

        i += 1
