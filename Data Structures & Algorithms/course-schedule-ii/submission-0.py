class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        # 每门课程对应它需要先完成的课程
        preMap = {i: [] for i in range(numCourses)}

        for course, pre in prerequisites:
            preMap[course].append(pre)

        # visiting：当前 DFS 路径上正在访问的课程，用于检测环
        visiting = set()

        # visited：已经完成 DFS 的课程，避免重复处理
        visited = set()

        # 保存合法的课程顺序
        res = []

        def dfs(course):

            # 当前 DFS 路径再次遇到这门课，说明存在环
            if course in visiting:
                return False

            # 这门课已经处理完，不需要重复 DFS
            if course in visited:
                return True

            # 标记当前课程正在 DFS 路径中
            visiting.add(course)

            # 先完成所有 prerequisite
            for pre in preMap[course]:
                if not dfs(pre):
                    return False

            # 所有 prerequisite 都处理完毕
            visiting.remove(course)

            # 标记课程已经处理完成
            visited.add(course)

            # 现在才能把当前课程加入结果
            res.append(course)

            return True

        # 所有课程都必须处理，包括没有依赖关系的课程
        for course in range(numCourses):
            if not dfs(course):
                return []

        return res