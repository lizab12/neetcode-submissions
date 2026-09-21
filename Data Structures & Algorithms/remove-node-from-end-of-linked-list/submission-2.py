# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # count nodes
        c = 0
        cur = head

        while cur:
            c += 1
            cur = cur.next

        # if removing the head
        if c == n:
            return head.next

        # move to node before the one to remove
        cur = head

        for _ in range(c - n - 1):
            cur = cur.next

        cur.next = cur.next.next

        return head
        
        