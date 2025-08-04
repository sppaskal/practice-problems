'''
Use a recursive approach to traverse
all the nested lists within the main
list. Use .extend() to add all elems
of each item (when it's an iterable)
to the flat list, or simply append when
the item is not an iterable.
'''


def flatten_nested_list(nested_list):
    flat = []

    for item in nested_list:
        if isinstance(item, list):
            flat.extend(flatten_nested_list(item))
        else:
            flat.append(item)

    return flat


print(flatten_nested_list([1, [2, [3, 4], 5], 6]))
