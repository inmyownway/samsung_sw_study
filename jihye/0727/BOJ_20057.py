""" 20057 : 마법사 상어와 토네이도
- x에서 y로 이동할때 y의 모든 모래가 비율과 alpha가 적힌 칸으로 이동한다.
- alpha로 이동하는 모래 양은 비율이 적힌 칸으로 이동하지 않은 남은 모래 양이다.
- (1,1)까지 이동한 뒤에 소멸하고, 모래가 격자 밖으로 이동할 수도 있다.
--> 토네이도가 소멸 되었을 때 격자 밖으로 나간 모래의 양은?
"""
N = int(input()) # 격자의 크기

board = [list(map(int, input().split(' '))) for _ in range(N)]

## alpha, 0.05, 0.1, 0.1, 0.07, 0.07, 0.02, 0.02, 0.01, 0.01
DIR_DICT = {
    0: {
        "DX": [-1,-2,-1,-1, 0, 0, 0, 0, 1, 1],
        "DY": [0, 0, 1, -1, 1, -1, 2, -2, 1, -1],
    }, ## 왼쪽
    1: {
        "DX": [0, 0, 1, -1, 1, -1, 2, -2, 1, -1],
        "DY": [1, 2, 1, 1, 0, 0, 0, 0, -1, -1]
    }, ## 아래쪽
    2: {
        "DX": [1, 2, 1, 1, 0, 0, 0, 0, -1, -1],
        "DY": [0, 0, -1, 1, -1, 1, -2, 2, -1, 1],
    }, ## 오른쪽
    3: {
        "DX": [0, 0, 1, -1, 1, -1, 2, -2, 1, -1],
        "DY": [-1, -2, -1, -1, 0, 0, 0, 0, 1, 1]
    } ## 위쪽
}

RATIO_DICT = {
    0 : 0.55, 1:0.05, 2 : 0.1, 3:0.1, 4:0.07, 5:0.07,
    6:0.02, 7:0.02, 8:0.01, 9:0.01
}

def check_range(x, y):
    if (0 <= x < N) and (0 <= y < N):
        return True

    return False
def move(dir, x, y):
    temp = 0
    sand_mass = board[y][x]
    board[y][x] = 0
    if y < 0 or x < 0:
        return
    left_sand = sand_mass
    for i in range(1, 10):
        nx, ny = x + DIR_DICT[dir]["DX"][i], y + DIR_DICT[dir]["DY"][i]
        ratio = RATIO_DICT[i]
        new_sand = int(sand_mass * ratio)
        """ 주의
        - 여기서 check_range에 걸리지 않더라도 alpha 자리로 이동하는 것은 무조건 이전 ratio가 지정된 위치에 먼지가 이동을 했다는 가정하에 움직이게 될 것이다.
        """
        if check_range(nx, ny) == True:
            board[ny][nx] += new_sand
            # left_sand -= new_sand
        else: ## 영역 밖이라 버려짐
            temp += new_sand
        left_sand -= new_sand
    nx, ny = x + DIR_DICT[dir]["DX"][0], y + DIR_DICT[dir]["DY"][0]

    if check_range(nx, ny) == True:
        board[ny][nx] += left_sand
    else:
        # print(f"LEFT : {left_sand}")
        temp += left_sand

    return temp



X, Y = N // 2, N//2
dir = 0
cycle = 1
answer = 0
DX, DY = [-1, 0, 1, 0], [0, 1, 0, -1] ## 토네이도의 이동 방향

stop = False

while stop == False:
    for _ in range(cycle):

        X += DX[dir % 4]
        Y += DY[dir % 4]
        # print(X, Y)
        answer += move(dir%4, X, Y)
        if X == 0 and Y == 0: ## (0, 0)에 토네이도가 위치하면 소멸함
            stop = True
            break
        # answer += move(dir % 4, X, Y)

    dir += 1 ## 방향 정보 갱신
    cycle = cycle + 1 if dir % 2 == 0 else cycle ## 2번 방향을 바꾸는 것을 주기로 톱니바퀴 모양으로 회전하면서 이동하는 칸의 수가 1씩 증가한다.

print(answer)

