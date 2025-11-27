'''
We use recursion to generate all combinations
of well formed parentheses. We build out each
valid combination in the 'current' var, and append
it to the 'result' var when it has reach the desired
number of pairs of parentheses.
'''


def generateParenthesis(n):
    """
    Generates all combinations of well-formed parentheses for n pairs.
    :type n: int
    :rtype: List[str]
    """

    result = []  # This will hold all valid combinations

    def backtrack(current, open_count, close_count):
        # Base case: if the current string has 2*n characters, it's complete
        if len(current) == 2 * n:
            result.append(current)
            return

        # If we can still add an opening parenthesis, do it
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)

        # If we can add a closing parenthesis without breaking the balance, do it
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    # Start the recursion with an empty string and zero open/close counts
    backtrack('', 0, 0)

    return result  # Return all valid combinations
