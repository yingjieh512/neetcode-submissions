class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. 找中点
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse 后半段
        second = slow.next
        slow.next = None

        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # prev 就是反转后的后半段
        first = head
        second = prev

        # 3. merge
        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2