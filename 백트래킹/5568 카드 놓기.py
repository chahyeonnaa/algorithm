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
# list로 중복확인해서 넣었는데, set(add) 쓰면 더 간단하다.
# map써서 str만들고, 조인으로 바로 이어버리면 편함!!!!!!
# 굳이 문자열 변수 선언해서 반복문 돌릴 필요 없음
# 시간 차이 236 -> 48 엄청 많이 난다...!
n=int(input())
k=int(input())
S=[]
number=[]
result=set()
check=[0]*n
for i in range(n):
    S.append(int(input()))


def dfs():
    if len(number)==k:
        result.add(''.join(map(str,number)))
        return
        
    for i in range(n):
        if check[i]:
            continue
        number.append(S[i])
        check[i]=1
        dfs()
        number.pop()
        check[i]=0
dfs()
print(len(result))
# -


