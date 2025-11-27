class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sort_list(head):
    # Base case: empty list or single node
    if not head or not head.next:
        return head

    # Step 1: Split the list into two halves using slow/fast pointers
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None  # Break the list into two halves

    # Step 2: Recursively sort both halves
    left = sort_list(head)
    right = sort_list(mid)

    # Step 3: Merge the sorted halves
    return merge(left, right)


def merge(l1, l2):
    dummy = ListNode()
    tail = dummy

    # Merge two sorted lists
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Append remaining nodes
    tail.next = l1 if l1 else l2
    return dummy.next
