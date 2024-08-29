class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        A UFDS can basically check if the graph is a cycle. Adding to a group
        can force the groups to merge, meaning a cycle is found. So when we want to add
        a edge from node to node, if it causes a cycle, we found our edge!
        """
        parent = dict()
        rank = dict()

        # populate the union find
        for i in range(1, len(edges) + 1):
            # you are your own parent since single group
            parent[i] = i
            rank[i] = 0

        # the union find 'find' function
        def find(n: int) -> int:
            """
            n: node to find in the UFDS
            returns: node
            """
            # find root of x
            if n != parent[n]:
                # path compression, recursively travel up to find the root parent
                parent[n] = find(parent[n])
            return parent[n]

        def union(n1: int, n2: int) -> bool:
            """
            n1: first node
            n2: second node to combine together
            return: return if a cycle is detected
            """
            p1, p2 = find(n1), find(n2)
            # Cant find same node, cant union yourself together
            # this means cycle found, nodes are *already in the same set
            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                # bigger tree height becomes root
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        # Process each edge
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

        # This line should never be reached if the input is valid
        return []
