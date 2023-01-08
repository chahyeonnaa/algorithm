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
# 11399 ATM

# 돈을 인출하는데 필요한 시간의 합 최소로 만들기
# 누적되니까 오름차순 정렬하면 됨

# 3 1 4 3 2-> 3+4+8+11+13=39
# 1 2 3 3 4-> 1+3+6+9+13=32

N=int(input())
money=list(map(int, input().split()))

money.sort()
result=0
new=0
for i in money:
    result +=i
    new += result
    
print(new)
