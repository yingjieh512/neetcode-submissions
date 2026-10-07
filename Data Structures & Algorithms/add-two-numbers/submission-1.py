class Solution:
    def addTwoNumbers(self, l1, l2):
        num1 = 0
        num2 = 0
        place = 1

        cur = l1
        while cur:
            num1 += cur.val * place
            place *= 10
            cur = cur.next

        place = 1
        cur = l2
        while cur:
            num2 += cur.val * place
            place *= 10
            cur = cur.next

        total = num1 + num2

        dummy = ListNode()
        cur = dummy

        if total == 0:
            return ListNode(0)

        while total:
            digit = total % 10
            cur.next = ListNode(digit)
            cur = cur.next

            total //= 10

        return dummy.next