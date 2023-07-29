""" BOJ 20056 : 마법사 상어와 파이어볼
- 크기가 NxN인 격자에 M개의 파이어볼 발사.
(r, c) : 파이어볼의 위치
m : 파이어볼의 질량
d : 파이어볼의 방향
s : 파이어볼의 속력
- 1번행은 N번과,  1번 열은 N번 열과 연결되어 있음

<문제 조건>
1. 각자의 방향으로 s만큼 이동하고, 이때 같은 칸에 여러개의 파이어볼이 있을 수 있다.
2. 한 칸에 2개 이상의 파이어볼이 있다면
    - 같은 칸에 있는 파이어볼은 하나로 합침
    - 4개의 파이어볼로 나눈다.
    -> 새 질량 = 전체 질량의 합 / 5
    -> 새 속력 = 전체 속력의 합 / 전체 개수
    -> 방향이 모두 홀수이거나 짝수이면 방향은 0, 2, 4, 6이 되고 아니면 1, 3, 5, 7이 된다.
3. 질량이 0인 파이어볼은 소멸되어 없어진다.

=> K번 이동한 후에 남은 파이어볼의 질량의 합은?
"""

DX, DY = [0, 1, 1, 1, 0, -1, -1, -1], [-1, -1, 0, 1, 1, 1, 0, -1]
N, M, K = map(int, input().split(' '))

from collections import defaultdict

board = defaultdict(list)

# def check_range(c):
#     if c < 0:
#         c = N - (abs(c) % N)
#     elif c >= N:
#         c = c % N
#
#     return c

# def move_coord(x, y, d, speed):
#     for s in range(speed):
#         x += DX[d];y += DY[d]
#         if x == N:x = 0
#         if x == -1:x = N-1
#         if y == N:y=0
#         if y == -1:y = N-1
#     return x, y

for _ in range(M):
    r, c, m, s, d = list(map(int, input().split(' '))) ## row, col
    board_key = f"{r-1}_{c-1}"
    board[board_key].append((m, d, s))

def move_ball():
    global board, DX, DY
    moved_ball = defaultdict(list)
    for key, value in board.items():
        y, x = key.split('_')
        y, x = int(y), int(x)
        for v in value:
            mass, d, speed = v
            # ny, nx = check_range(y + DY[d]*speed), check_range(x + DX[d]*speed)
            # nx, ny = move_coord(x, y, d, speed)
            ny, nx = (y + DY[d]*speed) % N, (x +DX[d]*speed) % N
            moved_ball[f"{ny}_{nx}"].append((mass, d, speed))

    board = moved_ball

def check_dir(dirs):
    add_odd, add_even = 0, 0
    for d in dirs:
        if d % 2 == 0:
            add_even += 1
        else:
            add_odd += 1
    if add_even == len(dirs) or add_odd == len(dirs):
        return [0, 2, 4, 6]
    return [1, 3, 5, 7]
    # div = [d % 2 for d in dirs]
    # if sum(div) == 0 or sum(div) == len(dirs): # 방향이 모두 홄수이거나 짝수이면
    #     return [0, 2, 4, 6]
    # return [1, 3, 5, 7]
def check_multi():
    global board
    new_board = defaultdict(list)
    for key, value in board.items():
        if len(value) > 1:
            new_mass = sum([v[0] for v in value]) // 5
            if new_mass != 0:
                new_speed = sum([v[2] for v in value]) // len(value)
                new_dir = check_dir([v[1] for v in value])
                # new_board[key] = []
                for d in new_dir:
                    new_board[key].append((new_mass, d, new_speed))
        elif len(value) == 1:
            new_board[key] = value
    board = new_board

def add_left():
    answer = 0
    for key, value in board.items():
        answer += sum([v[0] for v in value])
    return answer

# print(board)
for k in range(K):
    move_ball()
    check_multi()
    # print(board)

answer = add_left()
print(answer)

