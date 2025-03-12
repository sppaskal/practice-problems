"""
Use a stack to keep track of the order of
closing brackets needed.
"""


def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """

    parentheses = {
        "(": ")",
        "[": "]",
        "{": "}"
    }

    closing_stack = []

    for char in s:
        if char in parentheses:  # char is an opening bracket
            # add expected corresponding closing bracket
            closing_stack.append(parentheses[char])
        else:
            # if closing bracket, compare to next in line
            # closing bracket
            if not closing_stack or char != closing_stack.pop():
                return False

    if closing_stack:  # if brackets left open
        return False

    return True
