import sys
sys.setrecursionlimit(1000000)
def dfs(s):
    visited[s] = True
    count = 1
    for v in graph[s]:
        if not visited[v]:
            count += dfs(v)
    return count

if __name__ == "__main__":
    visited = [False for _ in range(10001)]
    graph = [[] for _ in range(10001)]
    length = []
    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
    for i in range(1, n+1):
        length.append(dfs(i))
    print(max(length))