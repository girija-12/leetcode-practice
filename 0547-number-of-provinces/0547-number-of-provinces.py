class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=set()
        count=0
        n=len(isConnected)
        def dfs(node):
            visited.add(node)
            for i in range(n):
                if isConnected[node][i] and i not in visited:
                    dfs(i)
        for city in range(n):
            if city not in visited:
                dfs(city)
                count+=1
        return count