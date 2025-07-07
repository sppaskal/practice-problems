'''
We are going to use the tortoise and hare algorithm to solve
for a cycle in a singly linked list.
'''


class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode) -> bool:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Create nodes
a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)

# Link nodes to form a cycle: -4 -> 2
a.next = b
b.next = c
c.next = d
d.next = b  # cycle here

print(has_cycle(a))  # Output: True
