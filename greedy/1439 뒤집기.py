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
# 모든 숫자 같게 만들기
# <연속된> 하나 이상의 숫자를 잡고 모두 뒤집기
# 1을 0으로, 0을 1으로
# 연속된 부분의 개수를 각각 세야지(숫자에서 숫자로 바뀔때를 세어야하나..?)
S=list(input())
zero=0
one=0
start=S[0]

for i in range(1, len(S)):
    if start==S[i]:
        continue
    else:
        start=S[i]
        if S[i]=='1':
            one+=1
        else:
            zero+=1
print(max(one, zero))
# -


