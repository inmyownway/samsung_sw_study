""" BOJ 21608 : 상어 초등학교
<문제 설명>
- NxN의 크기의 격자 (1 ~ N^2번으로 학생들 번호가 매겨져 있음)
- (r, c) = r행 c열
- 한 칸에는 한명만 앉고, euclidian distance = 1인 두 칸이 인접한 칸이라고 한다. == 사방에 있는 칸만이 인접하다고 할 수 있음.

1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
2. 위의 조건을 만족하는 칸이 여러 개라면 인접한 칸 중에서 빈칸이 가장 많은 칸으로 자리를 정한다.
3. 위의 조건도 만족하는 칸이 여러개면 행의 번호가 작은 칸 -> 열의 번호가 작은 칸을 선택 == 제일 위에 있으면서 제일 왼쪽에 위치한 칸이어야 한다.

- 학생의 만족도는 자리배치가 모두 끝난 후에 인접한 칸에 앉은 좋아하는 학생의 수 = n이면 10 ** (n-1)이다. 단, n >= 1일때 만이다.

<문제 출력>
- 학생의 만족도의 총 합을 구하여라.
"""
import heapq
from collections import defaultdict

N = int(input())

board = [[-1 for _ in range(N)] for _ in range(N)]
like_board = defaultdict(list)
students = []
for i in range(N**2):
    arr = list(map(int, input().strip().split(' ')))
    sid = arr[0] ## 학생의 번호
    likes = arr[1:] ## sid 번호 학생이 좋아하는 학생의 번호
    students.append(sid-1)
    like_board[sid-1] = [l-1 for l in likes]
# print(like_board)
    # for l in likes:
    #     like_board[sid-1][l-1] = 1

# def _init_board():
#     global board
#     for i in range(N):
#         for j in range(N):
#             if i == 0 or i == N-1:
#                 if j == 0 or j == N-1:
#                     board[i][j] = [2, -1] ## 이웃에 빈 칸의 개수, 해당 위치에 앉은 학생의 번호
#                 else:
#                     board[i][j] = [3, -1]
#             else:
#                 if j == 0 or j == N-1:
#                     board[i][j] = [3, -1]
#                 else:
#                     board[i][j] = [4, -1]

def check_range(x, y):
    if (0 <= x < N) and (0 <= y < N):
        return True
    return False

def _check_bruteforce():
    DX, DY = [-1, 1, 0, 0], [0, 0, -1, 1]
    for sid in students:
        q = []
        for i in range(N): ## 행 (Y)
            for j in range(N): ## 열 (X)
                like_cnt = 0;empty_cnt = 0
                if board[i][j] == -1: # 여기 아무도 안앉은 경우에
                    for dx, dy in zip(DX, DY):
                        nx, ny = j + dx, i + dy
                        if check_range(nx, ny) == True:
                            if board[ny][nx] != -1:
                                temp = board[ny][nx]
                                if (temp in like_board[sid]):
                                    like_cnt += 1
                            else:
                                empty_cnt += 1
                    heapq.heappush(q, (-like_cnt, -empty_cnt, i, j))
        best_params = heapq.heappop(q)
        # print(f"Student {sid} : {best_params}")
        y, x = best_params[2:]
        board[y][x] = sid



def _add_satisfaction():
    satisfaction = 0
    DX, DY = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(N):
        for j in range(N):
            pid = board[i][j]; like_n = 0
            for dx, dy in zip(DX, DY):
                ny, nx = i + dy, j + dx

                if check_range(nx, ny) == True and board[ny][nx] in like_board[pid]:
                    like_n += 1

            if like_n == 1:satisfaction += 1
            elif like_n == 2:satisfaction += 10
            elif like_n == 3:satisfaction += 100
            elif like_n == 4:satisfaction += 1000
    return satisfaction


# _init_board()
_check_bruteforce()
# print(board)
answer = _add_satisfaction()
print(answer)
