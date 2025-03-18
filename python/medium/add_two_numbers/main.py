"""
Traverse both input linked lists at the same time,
adding their values (while keeping track of the remainder)
all the while building out a result linked list.
The algorithm can add linked lists of different sizes
as it keeps iterating even if one list is finished
until both l1 and l2 are None.
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1, l2):
    """
    :type l1: Optional[ListNode]
    :type l2: Optional[ListNode]
    :rtype: Optional[ListNode]
    """

    result_list = ListNode()  # result linked list
    dummy_head = result_list  # keep track of head

    carry = 0
    while l1 or l2 or carry:
        result = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        carry = 0
        if result > 9:
            carry = 1
            result = result % 10

        result_list.next = ListNode(result)
        result_list = result_list.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy_head.next
