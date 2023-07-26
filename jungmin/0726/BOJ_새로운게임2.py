N, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
chess = [[[] for _ in range(N)] for _ in range(N)]

# 동 서 북 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
horse = []

for i in range(K):
    x, y, d = map(int, input().split())
    horse.append([x-1, y-1, d-1])
    chess[x-1][y-1].append(i)
# 0은 흰색, 1은 빨간색, 2는 파란색
def solve(horse_num):
    x, y, dir = horse[horse_num]

    nx = x + dx[dir]
    ny = y + dy[dir]
    # 파란색(== 범위 초과 경우 같음)
    # 방향 바꿔주고 이동
    #if 0>nx or nx>=N or 0>ny or ny>=N or board[nx][ny]==2:
    if 0 > nx or nx >= N or 0 > ny or ny >= N or board[nx][ny] == 2:
        if dir == 0 or dir == 2:
            dir+=1
        elif dir==1 or dir == 3:
            dir-=1
        horse[horse_num][2]=dir

        nx= x +dx[dir]
        ny =y+dy[dir]
        # 또 파란색 or 범위초과니까 움직이지 않음
        if 0 > nx or nx >= N or 0 > ny or ny >= N or board[nx][ny] == 2:
            return True

    horse_up=[]
    for h_idx,h_n in enumerate(chess[x][y]):
        # 이동하려는 말 위에 말이 또 있으면
        if h_n ==horse_num:
            horse_up.extend(chess[x][y][h_idx:])
            chess[x][y]=chess[x][y][:h_idx]
            break
    # 이동하려는 칸이 빨간색임
    # 거꾸로 뒤집어서 이동시켜야함
    if board[nx][ny]==1:
        horse_up.reverse()

    for h in horse_up:
        horse[h][0],horse[h][1]=nx,ny
        chess[nx][ny].append(h)

    if len(chess[nx][ny])>=4:
        return False
    return True








cnt = 0
while True:
    check = False
    if cnt > 1000:
        print(-1)
        break
    for i in range(K):
        if not solve(i):
            check = True
            break
    cnt+=1
    if check:
        print(cnt)

        break





