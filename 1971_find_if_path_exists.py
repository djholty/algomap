#DFS RECURSIVE

from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = defaultdict(list)

        #convert edges into adjacency list
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen =  set()

        seen.add(source)

        def dfs(i):
            if i == destination:
                return True

            for neighbor in graph[i]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if dfs(neighbor):
                        return True

            return False #you've gone all the way through and couldn't find destination



        return dfs(source)



