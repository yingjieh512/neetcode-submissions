class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        slow = dummy
        fast = dummy

        # fast 先走 n 步
        for _ in range(n):
            fast = fast.next

        # 两个一起走，直到 fast 到最后一个 node
        while fast.next:
            slow = slow.next
            fast = fast.next

        # slow.next 就是要删除的 node
        slow.next = slow.next.next

        return dummy.next