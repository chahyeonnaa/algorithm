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
# 런타임에러만 졸라 돌려봤네...
# 너무 예시에 맞춰진 생각만한다...ㅠㅠㅠㅠㅠㅠ
# 왜그런지 생각 좀 하자 진짜
# dfs에서 재귀 허용 깊이 수동으로 늘려주는건 필수다.
# 내 풀이는 틀렸음. 전역변수가 필요하다.
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(R):
    global count
    visited[R]=count

    for i in graph[R]:
        if visited[i]==0:
            count+=1
            dfs(i)
            
            
N,M,R=map(int, input().split())
visited=[0]*(N+1)
graph=[[] for _ in range(N+1)]
count=1

for _ in range(M):
    A,B=map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# 아 여기서... 인덱스 에러였음...
# for i in range(M):
#     graph[i].sort()

for g in graph:
    g.sort()

dfs(R)

for i in range(1,N+1):
    print(visited[i])
# -




