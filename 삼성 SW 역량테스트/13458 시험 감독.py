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

# B : 총감독, C : 부감독
# 시간초과! 어쩐지 정답률 낮더라
# 반복문 돌리면 시간 초과
N=int(input())
A=list(map(int, input().split()))
B,C=map(int, input().split())
result=0
for i in range(N):
    A[i]=A[i]-B
    result +=1
    
    if A[i]<=0:
        continue
        
    while A[i]>0:
        A[i]=A[i]-C
        result+=1
print(result)
    

# B : 총감독, C : 부감독
# 나누기로 풀어야 통과
N=int(input())
A=list(map(int, input().split()))
B,C=map(int, input().split())
result=0
for i in range(N):
    A[i]=A[i]-B
    result +=1
    
    if A[i]<=0:
        continue
        
    result += A[i]//C
    if (A[i]%C) >0:
        result +=1
print(result)
