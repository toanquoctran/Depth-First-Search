import sys
sys.setrecursionlimit(10001)
def dfs(s):
    visited[s] = 1
    for v in graph[s]:
        if not visited[v]:
            if dfs(v):
                return True
        elif visited[v] == 1:
            return True
    visited[s] = 2

if __name__ == "__main__":
    t = int(input())
    res = False
    for _ in range(t):
        visited = [False for _ in range(10001)]
        graph = [[] for _ in range(10001)]
        n, m = map(int, input().split())
        for _ in range(m):
            a, b = map(int, input().split())
            graph[a-1].append(b-1)
        for i in range(n):
            if not visited[i]:
                res = dfs(i)
                if res:
                    break
        if res:
            print("YES")
        else:
            print("NO")