""" BOJ 14889 : 스타트와 링크
<문제 설명>
- i번 사람과 j번 사람이 같은 팀에 속할때 팀에 S[ij]의 능력치가 더해진다.
- 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 만들고자 한다. -> 이렇게 될 수 있는 팀의 능력치의 차이의 최솟값을 구하여라.
- 무조건 스타트팀과 링크 팀의 조원의 수는 N//2로 동일해야 한다.

<풀이 방법>
1. 우선 문제를 봤을 때는 그냥 백트래킹으로 모든 경우를 해보면 될 것도 같았다. 특히 4 <= N <= 20이기 때문에 해볼만 하다고 생각한다.
2. 이분 탐색..?  이때 이분 탐색으로 찾고자 하는 수를 <가능한 눙력치의 차이>라고 해도 괜찮을 것이다.
"""
N = int(input())
S = [list(map(int, input().split(' '))) for _ in range(N)]

answer = float('INF')
def find_min_diff(arr1, arr2, idx, sum1, sum2):
    global answer, S
    # print(arr1, arr2)
    if idx == N:
        if len(arr1) == len(arr2):
            if abs(sum1 - sum2) < answer:
                answer = abs(sum1 - sum2)
        return

    # arr2.append(idx)
    if len(arr2) > 0:
        new_add = sum(S[i][idx] + S[idx][i] for i in arr2)
    else:
        new_add = 0
    arr2.append(idx)
    find_min_diff(arr1, arr2, idx+1, sum1, sum2+new_add)
    arr2.remove(idx)
    new_add = sum([S[i][idx]+S[idx][i] for i in arr1])
    arr1.append(idx)
    find_min_diff(arr1, arr2, idx+1, sum1+new_add, sum2)
    arr1.remove(idx)



find_min_diff([0],[], 1, 0, 0)
print(answer)



