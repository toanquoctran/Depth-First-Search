import sys
sys.setrecursionlimit(1000000)

def dfs(s):
    visited[s] = True
    for v in graph[s]:
        if not visited[v]:
            dist[v] = dist[s] + 1
            dfs(v)

if __name__ == "__main__":
    visited = [False for _ in range(1001)]
    dist = [-1 for _ in range(1001)]
    graph = [[] for _ in range(1001)]
    n = int(input())
    distance = []
    minn = 1001
    girl = 0
    for _ in range(n-1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    q = int(input())
    dfs(1)
    for _ in range(q):
        x = int(input())
        if dist[x] < minn:
            minn = dist[x]
            girl = x
        elif dist[x] == minn and x < girl:
            minn = dist[x]
            girl = x
    print(girl)