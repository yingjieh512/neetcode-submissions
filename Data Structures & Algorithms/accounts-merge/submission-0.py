from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(list)
        email_to_name = {}

        # 建图：同一账户的第一个邮箱与其他邮箱双向连接
        for account in accounts:
            name = account[0]
            first_email = account[1]

            for email in account[1:]:
                email_to_name[email] = name

            for email in account[2:]:
                graph[first_email].append(email)
                graph[email].append(first_email)

        visited = set()
        res = []

        # 遍历所有邮箱，单独的邮箱也能被处理到
        for email in email_to_name:
            if email in visited:
                continue

            # 用栈做 DFS，收集这一组所有连通的邮箱
            stack = [email]
            visited.add(email)
            emails = []

            while stack:
                current = stack.pop()
                emails.append(current)

                for neighbor in graph[current]:
                    if neighbor in visited:
                        continue

                    visited.add(neighbor)
                    stack.append(neighbor)

            # 同一组邮箱属于同一个人，排序后加入答案
            name = email_to_name[email]
            res.append([name] + sorted(emails))

        return res