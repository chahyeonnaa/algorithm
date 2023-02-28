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
# 많이 등장하면 앞에 있어야함, 등장 횟수가 같으면 먼저 나온게 앞에 있어야
# 딕셔너리 사용해서 횟수를 담고,, 횟수만큼 키를 출력하면 되려나
# items() 이용하는거 몰랐음. 자료구조 문제 풀어야할듯
N,C=map(int, input().split())
S=list(map(int, input().split()))
dict={}

for i in S:
    if i not in dict:
        dict[i]=1
    else:
        dict[i] +=1
        
#dict=sorted(dict.items(), key=lambda x: x[1], reverse=True)
print(type(dict))
# 리스트안에 튜플로 정리됨
print(dict.items())
for key, value in dict:
    for i in range(value):
        print(key, end=" ")
# -


