import queue
def dfs(s):
    visited[s] = True
    st = []
    st.append(s)
    dist[s] = 0
    while len(st) > 0:
        u = st.pop()
        for i in graph[u]:
            v = graph[u][i]
            if v > dist[u] + 1:
                dist[v] = dist[u] + 1
                st.append(v)

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
    for _ in range(q):
        x = int(input())
        dfs(x)
        res = dist[1]
        if res < minn:
            minn = res
            girl = x
        elif res == minn and x < girl:
            minn = res
            girl = x
        for i in range(1001):
            dist[i] = 0
    print(girl)