N=int(input())


# 비어있는 칸중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 정함

students=[list(map(int,input().split())) for _ in range(N*N)]

dx=[0,0,-1,1]
dy=[1,-1,0,0]


room=[[0]*N for _ in range(N)]

for idx in range (N*N):
    student=students[idx]

    tmp=[]
    for i in range(N):
        for j in range(N):
            if room[i][j]==0:
                like=0
                blank=0
                for dir in range(4):
                    nx=i+dx[dir]
                    ny=j+dy[dir]

                    if 0<=nx<N and 0<=ny<N:
                        if room[nx][ny] in student[1:]:
                            like+=1
                        if room[nx][ny]==0:
                            blank+=1
                tmp.append([like,blank,i,j])
    tmp.sort(key= lambda x:(-x[0],-x[1],x[2],x[3]))

    room[tmp[0][2]][tmp[0][3]]=student[0]


# 만족도 구하기
students.sort(key =lambda x:(x[0]))

ans = 0
#print(students)
#print(room)
for i in range(N):
    for j in range(N):
        #print("room", room[i][j],"fav",students[room[i][j]-1][1:])

        #print(room[i][j])
        cnt=0
        for idx in range(4):
            nx=i+dx[idx]
            ny=j+dy[idx]

            if 0<=nx<N and 0<=ny <N:
                if room[nx][ny] in students[room[i][j]-1][1:]:
                    cnt+=1
        #print("cnt",cnt)
        ans+=(10**cnt)//10
        #print(ans)
print(ans)
