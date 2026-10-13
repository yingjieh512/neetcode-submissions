class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 创建有向图，记录每门课程需要先学哪些课程
        graph = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[a].append(b)

        # visiting 记录当前 DFS 路径中的课程
        visiting = set()

        def dfs(course):
            # 如果当前路径里已经有这门课，说明出现了环
            if course in visiting:
                return False

            # 如果没有先修课程，说明这门课可以完成
            if not graph[course]:
                return True

            # 把当前课程放入 DFS 路径
            visiting.add(course)

            # 检查所有先修课程
            for pre in graph[course]:
                if not dfs(pre):
                    return False

            # 递归结束，把当前课程从路径移除
            visiting.remove(course)

            # 已经验证过这门课程没有环
            # 清空它的先修课程，避免重复搜索
            graph[course] = []

            return True

        # 检查每一门课程
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True