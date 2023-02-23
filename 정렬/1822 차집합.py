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

# 시간초과!
n,m=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
result=[]
for i in A:
    if i not in B:
        result.append(i)
result.sort()
print(len(result))
if len(result) !=0:       
    print(*result)


# +
# 원소가 있는지 없는지 확인? -> 이진탐색 (반드시 정렬되어 있는 리스트)
def binary(array, target, start, end):
    while start<=end:
        mid=(start+end)//2
        
        if array[mid] == target:
            return -1
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return 0

n,m=map(int, input().split())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
B.sort()
result=[]

for i in A:
    if binary(B,i,0,m-1)==0:
        result.append(i)
result.sort()
if len(result)==0:
    print(0)
else:
    print(len(result))        
    print(*result)
# -

# 집합으로도 풀 수 있음
n,m=map(int, input().split())
A=list(map(int, input().split()))
B=set(list(map(int, input().split())))
result=[]
for i in A:
    if i not in B:
        result.append(i)
result.sort()
print(len(result))
if len(result) !=0:       
    print(*result)
