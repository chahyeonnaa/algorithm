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
# 붙지 않는 경우는 없음
# 같은 팀에 속할 때 까지 돌리고 돌리고
# 정리하자면,, K랑 I가 같을 때까지 반복문 돌린다.
# 클린 코드의 핵심 : 현재 번호에서 나눈 값을 빼주면 홀짝 안나눠도 된다.

N,K,I=map(int, input().split())
round=1
while N>2:
    if N%2!=0:
        N=(N//2)+1
    else:
        N=N//2
    if I%2!=0:
        I=(I//2)+1
    else:
        I=I//2
        
    if K%2!=0:
        K=(K//2)+1
    else:
        K=K//2

    if K==I:
        break
    round+=1
        
print(round)

# +
# 조금 더 깔끔하게 바꾸면
N,K,I=map(int, input().split())
round=1
while N>2:
    if N%2!=0:
        N=(N//2)+1
    else:
        N=N//2
    I-=(I//2)
    K-=(K//2)

    if K==I:
        break
    round+=1
        
print(round)

# -


