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
# 성공!
# 테케에 나와있는 경우 외에도 생각하자..
# n이 S에 속하지 않을 경우를 생각하지 못해서 20퍼에서 틀림
# 더 클린하게 만들어보자 -> 깔끔하게 만드려면 설계할 때 최대한 간단한 규칙을 찾아야함
# 내껀 똑같은 짓을 두번한다. 비효율적
# 집합에 속한 숫자를 찾을 때에서 경우를 제한해버리기 때문..
L=int(input())
S=list(map(int, input().split()))
N=int(input())

i=0
S.sort()
A=S[0]

if S[0]>N:
    V=S[0]-1
    G=N-1
    print((N-1) * (V-N+1) + V-N)
elif N in S:
    print(0)
else:
    while N>A:
        if S[i]<N:
            A=S[i]
            i+=1
        else:
            break
    B=S[i]-1
    A+=1
    
    print((B-N) * (N-A+1) + N-A )


# +
# 처음 코드
L=int(input())
S=list(map(int, input().split()))
N=int(input())

i=0
S.sort()
A=S[0]

if S[0]>N:
    V=S[0]-1
    G=N-1
    
    result1= V-N
    result2= N-1
    result=result1*result2
    print(result1+result2+result)
else:
    while N>A:
        if S[i]<N:
            A=S[i]
            i+=1
        else:
            break
    B=S[i]

    if N in S:
        print(0)
    else:
        result1= (B-1)-N
        result2= N-(A+1)
        result= result1*result2

        print(result+result1+result2)
