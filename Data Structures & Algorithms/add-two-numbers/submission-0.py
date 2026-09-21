class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        num1 = ""
        num2 = ""

        h1 = l1
        h2 = l2

        while h1:
            num1 += str(h1.val)
            h1 = h1.next

        while h2:
            num2 += str(h2.val)
            h2 = h2.next

        num1 = num1[::-1]
        num2 = num2[::-1]

        total = int(num1) + int(num2)

        dummy = ListNode()
        cur = dummy

        if total == 0:
            return ListNode(0)

        while total > 0:
            c = total % 10

            cur.next = ListNode(c)
            cur = cur.next

            total = total // 10

        return dummy.next