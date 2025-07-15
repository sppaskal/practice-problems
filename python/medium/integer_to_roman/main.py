def intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """

    # Define symbol mappings in descending order, including subtractive forms
    val_to_roman = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]

    result = ""
    for value, symbol in val_to_roman:
        # While the number is greater than or equal to the current value
        while num >= value:
            result += symbol  # Append the corresponding symbol
            num -= value      # Subtract the value from num
    return result
