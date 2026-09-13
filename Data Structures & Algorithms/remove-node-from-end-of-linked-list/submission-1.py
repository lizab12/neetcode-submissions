class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: get length
        l = 0
        cur = head
        while cur:
            l += 1
            cur = cur.next
        
        pos = l - n + 1  # 1-based index of node to remove
        
        # Step 2: if removing head
        if pos == 1:
            return head.next
        
        # Step 3: move to (pos-1)-th node
        cur = head
        for _ in range(pos - 2):
            cur = cur.next
        
        # Step 4: remove node
        cur.next = cur.next.next
        
        return head
