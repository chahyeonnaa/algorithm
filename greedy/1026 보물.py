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
# 1026 보물
# B는 재배열하면 안되는 것이 핵심
# A 오름차순 정렬하고, 앞에서부터 하나씩 B의 최댓값과 더한다.

N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
A.sort()
result=0
for i in range(N):
    result += A[i]*max(B)
    B.remove(max(B))
    
print(result)

