class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {i: 0 for i in range(numCourses)}

        graph = defaultdict(list)

        for a, b in prerequisites:
            indegree[a] += 1
            graph[b].append(a)
        res = [i for i in range(numCourses) if indegree[i] == 0]

        j = 0
        while j < len(res):
            curr = res[j]
            for course in graph[curr]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    res.append(course)
            j += 1
        return [] if len(res) != numCourses else res
