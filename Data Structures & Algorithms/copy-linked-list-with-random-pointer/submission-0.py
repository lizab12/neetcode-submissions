class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        oldToNew = {}

        cur = head

        # create copy of every node
        while cur:
            oldToNew[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        # connect next and random pointers
        while cur:
            oldToNew[cur].next = oldToNew.get(cur.next)
            oldToNew[cur].random = oldToNew.get(cur.random)

            cur = cur.next

        return oldToNew[head]