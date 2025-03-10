"""
The way by which we mathematically reverse x is first:
1. During each iteration get the rightmost digit
2. Add it to the reversed number and multiply what is
already there by 10 to account for the growing number
3. Remove rightmost digit from x so we can get to the
next digit in line
"""


def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """

    # negative numbers are not palindromes
    if x < 0:
        return False

    original_x = x
    reversed_x = 0
    # mathematically reverse x
    while x > 0:
        digit = x % 10
        reversed_x = (reversed_x * 10) + digit
        x = x // 10

    return original_x == reversed_x
