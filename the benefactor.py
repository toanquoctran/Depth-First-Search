import sys
sys.setrecursionlimit(100000000)

def dfs(s):
    visited[s] = True
    for v, l in graph[s]:
        if not visited[v]:
            dist[v] = dist[s] + l
            dfs(v)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        visited = [False for _ in range(50001)]
        dist = [-1 for _ in range(50001)]
        graph = [[] for _ in range(50001)]
        n = int(input())
        for _ in range(n-1):
            a, b, l = map(int, input().split())
            a -= 1
            b -= 1
            graph[a].append((b, l))
            graph[b].append((a, l))
        dist = [0]*n
        dfs(0)
        leaf1 = 0
        maxDist = 0
        for i in range(n):
            if dist[i] > maxDist:
                maxDist = dist[i]
                leaf1 = i
        maxDist = 0
        dist = [0]*n
        visited = [False for _ in range(50001)]
        dfs(leaf1)
        for i in range(n):
            if dist[i] > maxDist:
                maxDist = dist[i]
        print(maxDist)