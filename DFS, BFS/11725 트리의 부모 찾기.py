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
# 걍 제일 앞에 원소 출력하면 시간초과 날 수 밖에 없다.
# 이건 너무 1차원적인 생각 아니냐....시간초과도 고려해야지....
N=int(input())
graph=[[]*(N) for _ in range(N+1)]

for i in range(N-1):
    A,B=map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(2, N+1):
    print(graph[i][0])

# +
# 파이썬 3 - 시간초과. 왜지??????/
import sys
input=sys.stdin.readline
from collections import deque
def bfs(a, visited,graph):
    queue=deque([a])
    
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if visited[i]==0:
                visited[i]=v
                queue.append(i)
                
                
N=int(input())
visited=[0]*(N+1)
graph=[[] for _ in range(N+1)]

for i in range(N-1):
    A,B=map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)
    
bfs(1, visited,graph)
for i in range(2,N+1):
    print(visited[i])

# -


