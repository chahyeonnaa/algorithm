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
# 시간 초과
import sys
input=sys.stdin.readline
N=int(input())
M=int(input())

S=list(map(int, input().split()))
count=0
for i in range(N):
    if S[i]==0:
        continue
    A=M-S[i]
    for j in range(N):
        if S[j]==A:
            S[j]=0
            S[i]=0
            count+=1
            break
            
print(count)

# +
# 처음에 13퍼에서 실패, 반례 도움 받고 성공
# 아.. 좀 테케만 푸려고 하지 말자
N=int(input())
M=int(input())

S=list(map(int, input().split()))
count=0

for i in range(N):
    A=M-S[i]
    if S[i]==0 or A==S[i] or A==0:
        continue

    if A in S:
        S[i]=0
        S[S.index(A)]=0
        count+=1

print(count)

# +
# 투포인터로 풀어야하는 문제임
N=int(input())
M=int(input())

S=list(map(int, input().split()))
S.sort()

result=0
i,j=0,n-1

while i<j:
    if S[i]+S[j]==M:
        result+=1
        i+=1
        j-=1
    elif S[i]+S[j]<M:
        i+=1
    else:
        j-=1
        
print(result)

