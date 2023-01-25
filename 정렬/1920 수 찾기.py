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
# 계속 시간초과가 나서 찾아보니.. 이분탐색으로 풀어야함 ㅋㅋㅋㅋ
# 문제의 의도를 파악하지 못했다.........
N=int(input())
A=list(map(int, input().split()))
A.sort()

Mp=int(input())
M=list(map(int,input().split()))
result=0
for i in range(Mp):
    result=0
    for j in range(N):
        if M[i]==A[j]:
            result=1
            print(1)
            break
    if result!=1:
        print(0)

# +
N=int(input())
A=list(map(int, input().split()))
A.sort()

Mp=int(input())
M=list(map(int,input().split()))

for i in range(Mp):
    if M[i] not in A:
        print(0)
    else:
        print(1)
# +
# 이분 탐색으로 풀기
N=int(input())
A=list(map(int, input().split()))
A.sort()
m=int(input())
M=list(map(int, input().split()))

def binary(L, A, start, end):
    if start > end:
        return 0
    m =(start+end)//2
    if L ==A[m]:
        return 1
    elif L <A[m]:
        return binary(L, A, start, m-1)
    else:
        return binary(L, A, m+1, end)
    
for L in M:
    start=0
    end=len(A)-1
    print(binary(L, A, start, end))








# +
# 집합으로 풀기
# 
N=int(input())
A=set(input().split())
m=int(input())
M=list(input().split())


for i in M:
    if i in A:
        print("1")
    else:
        print("0")
# -


