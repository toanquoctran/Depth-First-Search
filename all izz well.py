import sys
sys.setrecursionlimit(1000000)
def dfs(x, y, curChar):
    if curChar == len(term)-1:
        return True
    visited[x][y] = True
    for i in range(8):
        newx = x + dx[i]
        newy = y + dy[i]
        if 0 <= newx < r and 0 <= newy < c and not visited[newx][newy] and maze[newx][newy] == term[curChar+1]:
            visited[newx][newy] = True
            if dfs(newx, newy, curChar + 1):
                return True
            visited[newx][newy] = False
    return False

if __name__ == "__main__":
    t = int(input())
    term = "ALLIZZWELL"
    dx = [0, 0, 1, -1, -1, 1, -1, 1]
    dy = [1, -1, 0, 0, -1, -1, 1, 1]
    res = False
    for _ in range(t):
        r, c = map(int, input().split())
        visited = [[False for _ in range(c)] for i in range(r)]
        path = [[-1 for _ in range(c)] for i in range(r)]
        maze = [None] * r
        for i in range(r):
            maze[i] = input()
        for i in range(r):
            for j in range(c):
                if maze[i][j] == "A":
                    visited[i][j] = True
                    res = dfs(i, j, 0)
                    visited[i][j] = False
                    if res:
                        break
            if res:
                break
        if res:
            print("YES")
        else:
            print("NO")
        input()