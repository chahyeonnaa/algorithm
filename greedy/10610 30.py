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
# 3의 배수가 되는 조건만 알면 
N=list(input())

yes=0
result=0
for i in N:
    if i == '0':
        yes=1
    result += int(i)
if result%3==0 and yes==1:
    N.sort(reverse=True)
    print("".join(N))
else:
    print(-1)
