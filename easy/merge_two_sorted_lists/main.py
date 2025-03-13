"""
Create a separate merged linked list
by iterating through lists 1&2 and adding
their nodes ordered by value to the new list.
At the end, add any remaining list in case
lists 1&2 are not the same length.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    merged = ListNode()  # keep as dummy head node
    cur_node = merged  # pointer to build merged list

    # iterate and build new merged list
    # by deconstructing list 1&2
    while list1 and list2:
        if list1.val <= list2.val:
            cur_node.next = list1
            list1 = list1.next
        else:
            cur_node.next = list2
            list2 = list2.next

        cur_node = cur_node.next

    # add any remainder of either list
    if list1:
        cur_node.next = list1
    if list2:
        cur_node.next = list2

    # return everything after dummy head
    return merged.next
