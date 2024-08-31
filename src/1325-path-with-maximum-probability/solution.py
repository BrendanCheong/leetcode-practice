import heapq
from collections import defaultdict
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Create an adjacency list for the graph
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))
        
        # Max-heap priority queue, we use negative probabilities because heapq is a min-heap by default
        max_heap = [(-1.0, start_node)]
        
        # Probability to reach each node starting from the start_node
        probabilities = [0.0] * n
        probabilities[start_node] = 1.0
        
        while max_heap:
            # Get the node with the highest probability (invert sign back)
            current_prob, node = heapq.heappop(max_heap)
            current_prob = -current_prob
            
            # If we've reached the end_node, return the probability
            if node == end_node:
                return current_prob
            
            # Explore neighbors
            for neighbor, edge_prob in graph[node]:
                new_prob = current_prob * edge_prob
                # If we find a higher probability path to neighbor, update and push to the heap
                if new_prob > probabilities[neighbor]:
                    probabilities[neighbor] = new_prob
                    heapq.heappush(max_heap, (-new_prob, neighbor))
        
        # If we never reach the end_node, return 0
        return 0.0
