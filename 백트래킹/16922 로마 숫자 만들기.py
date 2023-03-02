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
# 배열에 1,5,10,50 담기
# 시간초과 -> 애초에 중복 없이 뽑으면(AB나 BA나 합은 같음)
#set에서 검사하는데 시간 많이 안든다. -> 그렇다고 리스트 사용은 안됨
# 글자가 달라도 합은 같을 수 있다(숫자가 커지면)
# itertools의 combinations를 많이 사용하긴 하네..
import sys
#nput=sys.stdin.readline
def dfs(x):
    if len(result)==N:
        print(result)
        A=sum(result)
        B.add(A)
        return
    for i in range(x,4):
        result.append(S[i])
        dfs(i)
        result.pop()

N=int(input())
S=[1,5,10,50]
result=[]
B=set()
dfs(0)
print(len(B))
# -

# # 
