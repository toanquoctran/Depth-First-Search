def dfs(x, y):
    st = []
    visited[x][y] = True
    st.append((x, y))
    temp = []
    isOcean = False
    while len(st) > 0:
        curx, cury = st.pop()
        temp.append((curx, cury))
        if curx == 0 or cury == 0 or curx == n - 1 or cury == m - 1:
            isOcean = True
        for i in range(4):
            newx = curx + dx[i]
            newy = cury + dy[i]
            if 0 <= newx < n and 0 <= newy < m and maze[newx][newy] == "." and not visited[newx][newy]:
                visited[newx][newy] = True
                st.append((newx, newy))
    if not isOcean:
        lakes.append(temp)


if __name__ == "__main__":
    area = [0] * 2501
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    n, m, k = map(int, input().split())
    visited = [[False for _ in range(2501)] for i in range(2501)]
    maze = [None] * n
    lakes = []
    for i in range(n):
        maze[i] = list(input())
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maze[i][j] == ".":
                dfs(i, j)
    num = 0
    lakes.sort(key = lambda i: len(i))
    for i in range(len(lakes) - k):
        num += len(lakes[i])
        for newx, newy in lakes[i]:
            maze[newx][newy] = "*"
    print(num)
    for i in range(n):
        print("".join(maze[i]))