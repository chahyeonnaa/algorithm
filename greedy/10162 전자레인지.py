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
# A: 5분 = 300초 , B: 1분 = 60초, C: 10초
# 최소 버튼 조작

T=int(input())
timer=[300,60,10]
result=[0,0,0]

for i in range(len(timer)):
    if timer[i]>T:
        continue
    else:
        result[i] += (T // timer[i])
        T=T%timer[i]

if T%10 !=0:
    print(-1)
else:
    for i in range(3):
        print(result[i], end=' ')

