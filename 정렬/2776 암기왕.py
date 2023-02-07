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

# 숫자 있는지 없는지 확~인
# 반복문 돌리면 당연히 시간초과
# list랑 set 차이큼 - list로 받으면 시간초과
T=int(input())
for _ in range(T):
    N=int(input())
    one=set(map(int, input().split()))
    M=int(input())
    two=list(map(int, input().split()))
    for i in two:
        if i in one:
            print(1)
        else:
            print(0)
    

# +
# 리스트에 숫자 있는지 없는지 찾기 => 이진탐색(정렬되어있는 리스트)
def binary(i, one, start, end):
    if start > end:
        return 0
    m =(start+end)//2
    if i ==one[m]:
        return 1
    elif i <one[m]:
        return binary(i, one, start, m-1)
    else:
        return binary(i, one, m+1, end)
    
T=int(input())
for _ in range(T):
    N=int(input())
    one=list(map(int, input().split()))
    one.sort()
    M=int(input())
    two=list(map(int, input().split()))
    
    for i in two:
        start=0
        end=N-1
        print(binary(i, one, start, end))
            
                
    
# -


