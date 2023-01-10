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
# 1541 잃어버린 괄호
# 괄호를 적절히 쳐서 값을 최소로 만들자
# 빼기 앞에 괄호를 치면 되는데
S=input().split('-')

result=0
for i in range(len(S)):
    result=0
    A=S[i].split('+')
    for j in A:
        result +=int(j)
    S[i]=result

answer=S[0]
for i in range(1, len(S)):
    answer -=S[i]
print(answer)
    
