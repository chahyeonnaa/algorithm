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
# N명이 줄서있음, 줄서는 순서에 따라 필요한 시간의 합이 달라지

N=int(input())

timee=list(map(int, input().split()))
timee.sort()

result=0
best=0

for time in timee:
    result += time
    best += result
    
print(best)
