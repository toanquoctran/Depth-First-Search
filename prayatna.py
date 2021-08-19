import sys
sys.setrecursionlimit(100001)
def dfs(s):
    visited[s] = True
    for v in graph[s]:
        if not visited[v]:
            dfs(v)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        count = 0
        graph = [[] for _ in range(100001)]
        visited = [False for _ in range(100001)]
        n = int(input())
        e = int(input())
        for _ in range(e):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1
        print(count)