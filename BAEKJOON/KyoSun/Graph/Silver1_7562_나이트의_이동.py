# 16:00 ~ 16:30

DX = [1,2,2,1,-1,-2,-2,-1]
DY = [-2,-1,1,2,2,1,-1,-2]

N = int(input())

def solution():
    length = int(input())
    startX, startY = map(int, input().split())
    endX, endY = map(int, input().split())

    if startX == endX and startY == endY:
        print(0)
        return
    
    visit = [[-1] * length for _ in range(length)]
    visit[startY][startX] = 0
    q = [(startY, startX)]
    while q:
        y, x = q.pop(0)

        for dx, dy in zip(DX, DY):
            nx, ny = x + dx, y + dy
            if 0 > nx or 0 > ny or nx >= length or ny >= length:
                continue
            elif visit[ny][nx] != -1 or visit[ny][nx] <= visit[y][x] + 1:
                continue
            
            visit[ny][nx] = visit[y][x] + 1
            if nx == endX and ny == endY:
                print(visit[ny][nx])
                return
            else:
                q.append((ny, nx))
                continue

for _ in range(N):
    solution()