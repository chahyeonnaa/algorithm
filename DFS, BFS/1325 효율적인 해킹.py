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
# 연결요소 찾기 문제인데, 판으로 주어지지 않은 경우임
# visited 배열이 필요하다
# bfs로 풀어야징 -> 접근은 잘 했는데 문제를 더 꼼꼼히 읽고 생각하자
from collections import deque
def bfs(x):
    visited=[False]*(N+1)
    count=1
    queue=deque([x])
    visited[x]=True
    
    while queue:
        x= queue.popleft()
        
        for v in graph[x]:
            if visited[v]==False:
                visited[v]=True
                queue.append(v)
                count += 1
    return count
N,M=map(int, input().split())
graph=[[]*N for _ in range(N+1)]
result=[]
for _ in range(M):
    A,B=map(int, input().split())
    # A가 B를 신뢰한다 -> B를 해킹하면, A도 해킹 가능
    # 여기서 주의!
    graph[B].append(A)
    

for i in range(1, N+1):
    result.append(bfs(i))
    
max=max(result)
for i in range(N):
    if max==result[i]:
        print(i+1, end=" ")
# -


