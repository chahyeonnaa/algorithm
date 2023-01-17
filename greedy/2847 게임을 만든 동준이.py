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
# 헙.. 가볍게 성공
N=int(input())
score=[]
result=0
for i in range(N):
    score.append(int(input()))
    
for i in range(len(score)-1, 0, -1):
     if score[i]<=score[i-1]:
        origin=score[i-1]
        score[i-1]=score[i]-1
        result += origin-score[i-1]
print(result)
