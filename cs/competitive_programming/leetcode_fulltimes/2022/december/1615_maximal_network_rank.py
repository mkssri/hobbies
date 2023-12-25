import collections
from typing import List

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        graph = collections.defaultdict(set)

        # constructing graph
        for city1,city2 in roads:
            graph[city1].add(city2)
            graph[city2].add(city1)

        
        l_cities = list(graph.keys())
        
        res = 0
        for i in range(0, len(l_cities)):
            for j in range(i+1, len(l_cities)):
                has_connection = 1 if l_cities[i] in graph[l_cities[j]] else 0
                c_city1 = len(graph[l_cities[i]])
                c_city2 = len(graph[l_cities[j]])

                res = max(res, c_city1+c_city2-has_connection)

        return res