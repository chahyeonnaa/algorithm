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
# 배추에 배추흰지렁이가 한마리라도 살고 있으면, 다른 인접 배추로 이동 가능(보호 받을 수 있음)
# 인접 기준 : 상하좌우
# 배추가 모여 있는 곳에는 지렁이가 1마리만 있으면 됨
# 배추들이 몇 군데 퍼져있는지만 알면 됨(얼려먹기랑 같은 유형)
# 일단 그래프 먼저 만들어보자
# 답은 나오는데 왜 런타임 에러가 나는지 이유를 모르겠다........ㅜ....
import sys
# 이거 붙여야 런타임 에러 통과함
# 파이썬의 기본 재귀 한도 : 1000, 재귀 깊이가 1000을 넘어갈 경우에는 모듈을 따로 추가해야함!
sys.setrecursionlimit(10000)
def dfs(x,y):
    if x<=-1 or x>=N or y<=-1 or y>=M:
        return False
    
    if graph[x][y]==1:
        
        graph[x][y]=0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    else:
        return False
    
T=int(input())

for i in range(T):
    result=0
    M,N,K=map(int, input().split())
    
    graph=[[0]*M for _ in range(N)]
    
    for j in range(K):
        A,B=map(int, input().split())
        graph[B][A]=1

    for q in range(M):
        for w in range(N):
            if dfs(w,q) ==True:
                result +=1
    print(result)
# -


