import sys

ap = -sys.maxsize
an = sys.maxsize

def DFS(y,x,p):
    global ap, an

    if y == n-1 and x == n-1:
        ap = max(ap,p)
        an = min(an,p)
        return

    for i in range(2):
        yy, xx = y + dy[i], x + dx[i]
        if yy == n or xx == n:
            continue
        if arr[y][x] == '*':
            DFS(yy,xx,p*arr[yy][xx])
        elif arr[y][x] == '+':
            DFS(yy,xx,p+arr[yy][xx])
        elif arr[y][x] == '-':
            DFS(yy,xx,p-arr[yy][xx])
        else:
            DFS(yy,xx,p)

n = int(input())
arr = [list(map(str,input().split())) for _ in range(n)]
dy = [0, 1]
dx = [1, 0]
for i in range(n):
    for j in range(n):
        if (i+j)%2 == 0:
            arr[i][j] = int(arr[i][j])
DFS(0,0,arr[0][0])
print(ap,an)