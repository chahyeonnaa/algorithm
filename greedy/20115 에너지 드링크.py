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
N=int(input())
S=list(map(int, input().split()))
result=max(S)
S.sort()

for i in range(N-1):
    result += S[i]/2
if result%10==0:
    print(int(result))
else:
    print(result)
    
# # %g로 포맷팅 하기(소수점 아래 0 날리기)
# print('%g'%result)
# -


