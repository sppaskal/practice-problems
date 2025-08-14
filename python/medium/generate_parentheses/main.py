'''
We use recursion to generate all combinations
of well formed parentheses. We build out each
valid combination in the 'current' var, and append
it to the 'result' var when it has reach the desired
number of pairs of parentheses.
'''


def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """

    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    backtrack('', 0, 0)
    return result
