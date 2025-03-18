"""
The key here is to iterate through the string in reverse
so that you we can check the previous numeral in order to
know if you should subtract or add the current numeral.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        val_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_val = 0

        for num in reversed(s):
            cur_val = val_map[num]
            if prev_val > cur_val:
                total -= cur_val
            else:
                total += cur_val

            prev_val = cur_val

        return total
