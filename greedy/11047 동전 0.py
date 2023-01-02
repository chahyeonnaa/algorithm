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
# K로 만들기 위한 최소한의 동전 개수

N, K=map(int, input().split())
money=[]
result=0

for i in range(N):
    money.append(int(input()))
    
money.sort(reverse=True)

for moneyy in money:
    if K // moneyy ==0:
        continue
    target=(K // moneyy)
    result += target
    
    K= K % moneyy
    
    if K==0:
        break
        
print(result)

