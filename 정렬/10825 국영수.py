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
# 정렬의 기본 - 람다식 사용
N=int(input())
S=[]
for i in range(N):
    a,b,c,d = list(map(str, input().split()))
    S.append([a, int(b), int(c), int(d)])

S.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in S:
    print(i[0])
# -


