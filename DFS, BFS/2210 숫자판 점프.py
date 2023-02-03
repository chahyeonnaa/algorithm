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
# dfs쓸지.. bfs쓸지 어떻게 알지
def dfs(x,y,number):
    if len(number)==6:
        if number not in result:
            result.append(number)
        return
    
    # 상하좌우
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        
        if nx<0 or nx>=5 or ny<0 or ny>=5:
            continue
        else:
            dfs(nx, ny, number+graph[nx][ny])
    
graph=[]


for i in range(5):
    graph.append(list(map(str, input().split())))

result=[]

for i in range(5):
    for j in range(5):
        dfs(i,j,graph[i][j])
        
print(len(result))
# -


