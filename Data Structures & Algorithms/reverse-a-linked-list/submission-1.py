class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            next_node = curr.next   # 先保存下一个节点
            curr.next = prev        # 当前节点反向指向前一个节点
            prev = curr             # prev 往前走
            curr = next_node        # curr 往前走

        return prev