# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
# 아 7개가 더 나온다;;;;하 ..... 진짜 쉽지않네


# 왼쪽-아래쪽은 홀수번, 오른쪽-위는 짝수만큼 진행, 짝지어서 같이 움직인다
# 흩뿌리기는 방향별로 리스트를 만들어서 고정시킨다
# 좌표가 하나라도 음수가 되면 토네이도를 돌다가 끝난다
# 퍼지는 모래 계산,,, r이 0이면, 퍼지지않고 남은 모래가 더해진다
# r이 아니면, 현재 남아있는 양의 비율만큼 퍼진다

# 격자 밖으로 나간 모래의 양을 구해야한다
# 인덱스 검사해서 나갔으면 최종 값에 더해주고, 안나갔으면 그 자리에 모래양을 추가한다

# 핵심 : 방향별로 y를 기준으로 흩뿌려지는 모래를 받는 좌표들을 리스트로 정리
# 이동할 때 마다 모래는 흩뿌려진다 -> move 함수 호출 할 때 어떤 방향으로 이동하는지 넘겨준다
# rate 딕셔너리를 둬서 벨류 값을 꼽아준다
# 흩뿌려진 모래를 받는 좌표는 총 10개다.......

# 이거 때문에 엄청 헤맴
# a가 적힌 곳은 제일 마지막에 남은 모래를 받는 곳이다...
# 그러니까 r이 0인 좌표를 제일 마지막에 배치시켜야함....ㅎㅏ.....
# 숨은 의미까지 파악하는 실력을..기르자..센스가 필요하다!


N=int(input())
graph=[list(map(int, input().split())) for _ in range(N)]
left=[(-1,0,0.07),(1,0,0.07),(-2,0,0.02),(2,0,0.02),(-1,1,0.01),(1,1,0.01),
       (-1,-1,0.1),(1,-1,0.1),(0,-2,0.05),(0,-1,0)]
right=[(x,-y,z) for x,y,z in left]
down=[(-y,x,z) for x,y,z in left]
up=[(-x,y,z) for x,y,z in down]
answer=0
now=[N//2, N//2]
rate={"left":left, "right":right, "up":up, "down":down}
V=0

def move(cnt,dx,dy,direction):
    global answer,V
    for _ in range(cnt+1):
        now[0]=now[0]+dx
        now[1]=now[1]+dy
        
        #print(now[0],now[1])
        if now[0]<0 or now[1]<0:
            break 
            
        spreads=0
        for a, b, r in rate[direction]:
            nx,ny=now[0]+a, now[1]+b
            if r==0:
                sand=graph[now[0]][now[1]]-spreads
            else:
                sand=int(graph[now[0]][now[1]]*r)
            
            if 0<=nx<N and 0<=ny<N:
                graph[nx][ny] += sand
            else:
                answer += sand
            spreads += sand

    
    
for i in range(N):
    if i%2==0:
        move(i,0,-1,'left')
        move(i,1,0,'down')
    else:
        move(i,0,1,'right')
        move(i,-1,0,'up')
        
print(answer)    
# -

# ##### 
