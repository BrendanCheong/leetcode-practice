class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        A cycle in the graph means False.
        If we can successfully go through each and every course no problem, then its True
        We use adjacency list for O(V + E) time, other graphs won't work here we need to visit every node fast
        Do visualise this answer:
        1. DFS through every node using adjacency list
        2. Add to visited set
        3. Once we reach a node that has no neighbors (perhaps we reached the end), we unravel the recursion stack
        4. When we unravel we are travelling back where we came from, then we want to 'destroy' the edge
        when we go back. Like we go from 1 -> 2 -> 3, now we are at 3, go to 2, destroy 2 -> 3 edge: 1 -> 2 3
        5. And also pop out the visited node 3, since we already visited it and its known that we can reach that course
        6. If a course is in the visited set, return False
        7. Do this for every prequisites
        """
        # First build the Adjacency list
        graph = { i: [] for i in range(numCourses) }
        #! NOTE: Space is O(V + E)
        for courseStart, courseEnd in prerequisites:
            graph[courseStart].append(courseEnd)
        
        # Visited set
        visited = set()
        def dfs(course: int) -> bool:
            """
            Time: O(V + E), since we could visit every node and go through all edges
            """
            # Base case, we found a course in visited
            if course in visited:
                return False
            # Unravel case, the course is the end node
            if graph[course] == []:
                return True

            visited.add(course)
            # go through all neighbors
            for crs in graph[course]:
                # quick termination, this is just to optimise a bit
                # if the recursion already found its false, just return false, no need keep going through neighbors\
                if not dfs(crs):
                    return False
            # After going through all neighbors, means success! this course is cleared
            visited.remove(course)
            graph[course] = []

            # Default exit case
            return True
        
        # Go through all courses/nodes
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
