from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = { i: list() for i in range(numCourses) }
        indegree = { i: 0 for i in range(numCourses) }
        lookup = { i: set() for i in range(numCourses) }

        # Populate the indegree
        for preq, crs in prerequisites:
            # Adjacency List, this x -> y
            graph[preq].append(crs)
            # indegree, y has +1 indegree
            indegree[crs] += 1
        
        # add indegree == 0 to queue
        q = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        # Lets do BFS to make sure all the nodes are processed starting from the first node of the toposort
        while q:
            curr = q.popleft()
            # go through neighbors
            for n in graph[curr]:
                # we want to merge the preq together so we have transitive nodes knows about those infront of them
                # My node n has this preq
                lookup[n].add(curr)
                # combine n preq with the rest of curr preq
                # 1 -> 2
                # |-> 3, so 2 has 3 as preq
                lookup[n].update(lookup[curr])
                indegree[n] -= 1
                # add to q:
                if indegree[n] == 0:
                    q.append(n)
        # what do we do with lookup now? for each of the queries
        # the queries must fulfil the lookup -> lookup[node] has these preq
        res = []
        for n1, n2 in queries:
            if n1 in lookup[n2]:
                res.append(True)
            else:
                res.append(False)
        return res
