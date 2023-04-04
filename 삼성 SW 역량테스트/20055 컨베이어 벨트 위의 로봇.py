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
# 문제를 이해하는데만 30분이 넘게 걸렸다 ㅋㅋㅋㅋㅋ
# 핵심 : 내리는 위치에 도달하면 바로 내리기 떄문에 항상 0임
# 내리는 위치 이후에는 로봇이 있을수가 없음
# "가장 먼저 벨트에 올라간 로봇부터"!!!!!! 중요. 그래서 반복문 거꾸로 돈다
# deque의 rotate 기능!
# 사소한 단어라도 놓치지 말고 꼼꼼히 의미부여를 하자......

from collections import deque
N,K=map(int, input().split())
velt=deque(list(map(int, input().split())))
robot=deque([0]*N)
res=0
while True:
    velt.rotate(1)
    robot.rotate(1)
    robot[-1]=0
    
    # 벨트위에 로봇이 있으면
    if sum(robot):
        for i in range(N-2, -1, -1):
            if robot[i]==1 and robot[i+1]==0 and velt[i+1]>=1:
                robot[i]=0
                robot[i+1]=1
                velt[i+1]-=1
        robot[-1]=0
    # 로봇 올리기
    if velt[0] >=1 and robot[0]==0:
        robot[0]=1
        velt[0] -=1
        
    res +=1
    
    if velt.count(0)>=K:
        break
print(res)
        
        
        
# -


