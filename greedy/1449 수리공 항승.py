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
# but 다른 코드 찾아보니 내 코드는 너무 깔끔하지 못하다..
# 반복문을 차례대로 돌면서, 길이 안이면 넘어가고, 아니면 새로 붙이게
# 이렇게 하면 리스트 안 값을 다르게 안바꿔줘도 된다.

N,L=map(int, input().split())
water=list(map(int, input().split()))
water.sort()
result=0
Q=0
while Q<N:
    a=min(water)
    fix=(a-0.5)+L
    for i in range(len(water)):
        if water[i]<=fix:
            water[i]=1001
            Q+=1
    result+=1
    
print(result)

