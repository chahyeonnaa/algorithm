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
# 아 모르겠다..... ㅜ
C,R=map(int, input().split())
K=int(input())
graph=[[0]*C for _ in range(R)]

# 상우하좌
dx=[0,1,0,-1]
dy=[1,0,-1,0]
x,y=0,0
direction=0
graph[0][0]=1
for i in range(2, K+1):
    if i==K:
        break
    x += dx[direction]
    y += dy[direction]

    graph[x][y]=i

    print(x,y)
    
    if x>=C or y>=R:
        direction= (direction+1)%4
print(*graph, sep='\n')
# -


