class Solution:
    def bfs(self, node, adj, visited):
        q = deque([node])
        visited.add(node)

        while q:
            node = q.popleft()

            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        cnt = 0

        adj = [[] for _ in range(n)]

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        for node in range(n):
            if node not in visited:
                self.bfs(node, adj, visited)
                cnt += 1
        
        return cnt