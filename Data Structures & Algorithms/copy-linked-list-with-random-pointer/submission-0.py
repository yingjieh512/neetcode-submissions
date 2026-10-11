class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None: None}

        cur = head
        while cur:
            oldToNew[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            copy = oldToNew[cur]
            copy.next = oldToNew[cur.next]
            copy.random = oldToNew[cur.random]
            cur = cur.next

        return oldToNew[head]