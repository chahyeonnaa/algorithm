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
# 여러 치킨집 중에서 M개만을 뽑아야한다 -> 조합
# 가능한 여러 조합 중에서 가장 최소의 치킨 거리를 찾아야함
# 각각의 조합들과 집 사이의 거리를 다 구해보면 된다
# itertools 안쓰고 dfs 쓰면?...?
from itertools import combinations
N,M=map(int, input().split())
city=[]
house=[]
chicken=[]
for i in range(N):
    city.append(list(map(int, input().split())))
    
for i in range(N):
    for j in range(N):
        if city[i][j]==1:
            house.append([i,j])
        elif city[i][j]==2:
            chicken.append([i,j])
result=1e9
# print(combinations(chicken, M))
for x in combinations(chicken, M):
    print(x)
    city_r=0
    for h in house:
        h_r=1e9
        # 집 마다 치킨 집들과의 거리 구하기
        for k in x:
            h_r=min(h_r, abs(h[0]-k[0])+abs(h[1]-k[1]))
        city_r += h_r
    result=min(result, city_r)
    
print(result)
# -


