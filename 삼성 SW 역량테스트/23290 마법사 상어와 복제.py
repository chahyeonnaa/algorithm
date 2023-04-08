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

# 배열에 값이 있는데 또 값을 추가하면 어떻게 되나
graph=[[[] for _ in range(4)] for _ in range(4)]
print(graph)

graph=[[0]*5]
print(graph)
graph1=[[0] for _ in range(5)]
print(graph1)

A=[1,2,3,4,5]
B=[7,8]
print(A[:])
print(A+B)

t=(1,2)
print(t)
t=(3,4)
print(t)

# +
# 핵심 : 상상하 이런식으로 상어가 움직일 떄 방문했던 칸을 또 갈 수 있음
# 핵심 : 3차원 배열을 썼다!!!!! 한칸에 물고기가 여러마리 담길 수 있음요

# 가장 처음 배열을 복제해두고, 복제한 것을 이동에 사용
# 가장 마지막에 복제 마법을 일으켜야하므로, 원본에 이동한 배열을 더해줌
# 배열끼리 더 하는것
# 복제 완료

# 반시계 45도 회전 후, 물고기 이동
# 새로운 배열 하나 더 만들어서 거기에 저장하긔

# 상어의 이동 : 백트래킹
# 3칸 이동했으면 검사, 가능한 모든 경우를 검사해서 맥스 값일 때 상어위치를 따로 튜플에 저장
# 방문했던 칸 또 갈 수 있음
# 한 칸에 물고기가 여러개 있을 수 있으므로, 3차원 배열을 사용!!
# 상어의 위치는 예전껄 기억할 필요가 없으므로 튜플 사용
# 상어가 방문했던 곳은 곧 냄새로 남는 곳!
# 상어의 이동 끝나고 냄새 배열에 냄새를 3으로 기록, 물고기는 없애주기
# 3번 돌아야 없어짐. 두번 전에 냄새가 사라지기 때문
# 한번 복제 돌 때 마다 냄새 값을 1씩 빼줌 

# 마법이 다 끝나면 남아있는 물고기 수 계산

