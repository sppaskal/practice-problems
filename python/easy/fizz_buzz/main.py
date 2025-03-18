def fizzBuzz(self, n):
    """
    :type n: int
    :rtype: List[str]
    """

    result = list()

    for i in range(1, n + 1):
        cur_str = ""

        if i % 3 == 0:
            cur_str += "Fizz"
        if i % 5 == 0:
            cur_str += "Buzz"
        if not cur_str:
            cur_str = str(i)

        result.append(cur_str)

    return result
