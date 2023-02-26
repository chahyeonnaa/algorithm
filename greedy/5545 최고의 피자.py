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
# 브루트포스로 풀어보자
# 70퍼에서 틀림 -> 토핑을 아예 선택하지 않을 경우 고려하지 않아서!
N=int(input())
To=[]
A,B=map(int, input().split())
C=int(input())
result=[]
for _ in range(N):
    To.append(int(input()))
    
# 이 정렬은 굳이 안해도 되지 않나..?
To.sort(reverse=True)

result.append(C // A)

for i in range(N):
    money=A
    money += ((i+1)*B)
    C += To[i]
    result.append(C//money)
    
print(max(result))

# -


