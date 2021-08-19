import sys
sys.setrecursionlimit(1000000)
def dfs(x, y, curChar):
    maxLength = 0
    if curChar == len(term) - 1:
        return 1
    visited[x][y] = True
    for i in range(8):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0 <= newx < h and 0 <= newy < w and not visited[newx][newy] and maze[newx][newy] == term[curChar+1]:
            visited[newx][newy] = True
            maxLength = max(maxLength, dfs(newx, newy, curChar + 1))
            visited[newx][newy] = False
    return maxLength+1

if __name__ == "__main__":
    term = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dx = [0, 0, 1, -1, -1, 1, -1, 1]
    dy = [1, -1, 0, 0, -1, -1, 1, 1]
    case = 0
    while True:
        h, w = map(int, input().split())
        res = 0
        if h == 0 and w == 0:
            break
        visited = [[False for _ in range(w)] for i in range(h)]
        maze = [None] * h
        for i in range(h):
            maze[i] = input()
        for i in range(h):
            for j in range(w):
                if maze[i][j] == "A":
                    visited[i][j] = True
                    res = max(res, dfs(i, j, 0))
        case += 1
        print("Case {}: {}".format(case, res))