N, M, k = map(int, input().split())

balls = []

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    balls.append([r - 1, c - 1, m, s, d])
# print(balls)
graph = [[[] for _ in range(N)] for _ in range(N)]
#print(graph)
for _ in range(k):

    # MOVE
    while balls:
        mr,mc,mm,ms,md=balls.pop(0)

        nx=(mr+ms*dx[md])%N
        ny=(mc+ms*dy[md])%N
        graph[nx][ny].append([mm,ms,md])

    # UNION

    for r in range(N):
        for c in range(N):
            # 2개 이상인 경우 -> 4개의 파이어볼로 쪼개기
            if len(graph[r][c]) > 1:
                sum_m, sum_s, cnt_odd, cnt_even, cnt = 0, 0, 0, 0, len(graph[r][c])
                while graph[r][c]:
                    _m, _s, _d = graph[r][c].pop(0)
                    sum_m += _m
                    sum_s += _s
                    if _d % 2:
                        cnt_odd += 1
                    else:
                        cnt_even += 1
                if cnt_odd == cnt or cnt_even == cnt:  # 모두 홀수이거나 모두 짝수인 경우
                    nd = [0, 2, 4, 6]
                else:
                    nd = [1, 3, 5, 7]
                if sum_m // 5:  # 질량 0이면 소멸
                    for d in nd:
                        balls.append([r, c, sum_m // 5, sum_s // cnt, d])

            # 1개인 경우
            if len(graph[r][c]) == 1:
                balls.append([r, c] + graph[r][c].pop())


print(sum([f[2] for f in balls]))

