class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        cur = head

        # 1. Insert copied nodes after originals
        while cur:
            copy = Node(cur.val)
            copy.next = cur.next
            cur.next = copy
            cur = copy.next

        # 2. Set random pointers for copied nodes
        cur = head

        while cur:
            copy = cur.next

            if cur.random:
                copy.random = cur.random.next

            cur = copy.next

        # 3. Separate original and copied lists
        cur = head
        copyHead = head.next

        while cur:
            copy = cur.next

            cur.next = copy.next

            if copy.next:
                copy.next = copy.next.next

            cur = cur.next

        return copyHead