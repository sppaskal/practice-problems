'''
We use a step variable that oscilates between 1 and -1 to determine the
direction of movement. That variable is used to modulate the row index.
We toggle the variable based on whether we reach the top or bottom row.

NOTE: Visually, the zigzag pattern does not appear when the characters
are printed out in the final list of strings, but rather match what the
theoretical zigzag pattern order of characters would be.
'''


def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """

    # in these cases the string does not change
    # as it's perfectly horizontal or vertical
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    curRow = 0

    for char in s:
        rows[curRow] += char

        if curRow == 0:
            step = 1  # move down
        elif curRow == numRows - 1:
            step = -1  # move up

        curRow += step

    return ''.join(rows)
