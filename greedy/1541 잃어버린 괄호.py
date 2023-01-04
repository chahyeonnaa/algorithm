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
# 여기서 하나의 과정이 더 필요하다
S=input().split('-')

result_B=0

for i in range(len(S)):
    result=0
    A=S[i].split('+')
    # 더할거 없으면 밑에 연산 안함
    if len(A)==1:
        continue
    for j in A:
        result += int(j)
    S[i]=result

result_B=int(S[0])
for i in range(1, len(S)):
    result_B -= int(S[i])
    
print(result_B)
# -

print(int('00009'))
