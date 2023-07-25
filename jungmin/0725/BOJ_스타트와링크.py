
def dfs(n,alst,blst):
    global ans
    if n == N:
        if len(alst)==len(blst):
            ans = min(ans,calc(alst,blst))
        return
    dfs(n+1,alst+[n],blst)
    dfs(n+1,alst,blst+[n])






def calc(alst,blst):

    asm=bsm=0

    for i in range(M):
        for j in range(M):
            asm+=graph[alst[i]][alst[j]]
            bsm+=graph[blst[i]][blst[j]]

    return abs(asm-bsm)


N=int(input())
M=N//2

graph=[]
for _ in range(N):
    graph.append(list(map(int,input().split())))

#print(graph)
ans=1e9
dfs(0,[],[])
print(ans)







