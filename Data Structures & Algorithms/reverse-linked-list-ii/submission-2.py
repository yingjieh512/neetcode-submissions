class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        # 找到反转区间前一个节点
        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next

        # 头插法反转
        for _ in range(right - left):
            nxt = cur.next

            cur.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

        return dummy.next