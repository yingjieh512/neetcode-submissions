class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = groupPrev

            for i in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next

            prev = groupNext
            cur = groupPrev.next

            while cur != groupNext:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp