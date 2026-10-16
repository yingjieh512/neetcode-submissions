import math

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head

        # 必须保证当前节点和下一个节点都存在
        while curr and curr.next:

            # 保存原来的下一个节点
            next_node = curr.next

            # 计算两个相邻节点的最大公约数
            gcd = math.gcd(curr.val, next_node.val)

            # 创建新节点，并让它指向原来的下一个节点
            new_node = ListNode(gcd, next_node)

            # 把新节点插入 curr 后面
            curr.next = new_node

            # 跳过刚插入的新节点
            # 继续处理原链表的下一对相邻节点
            curr = next_node

        return head