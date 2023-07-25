N = int(input())
matrix = [[] for i in range(N)]
for i in range(N):
    temp = list(map(int, input().split()))
    matrix[i] = temp
    
    
value_matrix = [[] for i in range(N)]
for i in range(N):
    temp = []
    for j in range(N):
        value_matrix[i].append(matrix[i][j] + matrix[j][i])
people = [i for i in range(N)]

import copy

def gen_comb(arr, n):
    if len(arr) == n:
        return [arr]
    if n == 0:
        return [[]]
    if n == 1:
        return [[i] for i in arr]
    
    results = []
    for i in range(len(arr)):
        rest_arr = copy.deepcopy(arr)
        rest_arr = rest_arr[i+1:]
        for temp in gen_comb(rest_arr, n-1):
            results.append(temp + [arr[i]])
    return results

def get_score(arr, value_matrix):
    score = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            score += value_matrix[arr[i]][arr[j]]
    return score


# 모든 조합 배열 만들기
possible_combs = gen_comb(people, N/2)
min_diff = 9999999
for comb in possible_combs:
    opp = []
    for i in range(N):
        if i not in comb:
            opp.append(i)
    score1 = get_score(comb, value_matrix)
    score2 = get_score(opp, value_matrix)
    score = max(score1-score2, score2-score1)
    min_diff = min(min_diff, score)
print(min_diff)
