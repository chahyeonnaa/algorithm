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

def dfs():
    if len(S)==M:
        print(*S)
        # 이렇게 하면 타입에러 -> map으로 문자열으로 바꿔줘야함
        #print("".join(S))
        #print("".join(map(str,S)))
        return 
    
    for i in range(1, N+1):
        if i not in S:
            S.append(i)
            dfs()
            S.pop()
N,M=map(int, input().split())
S=[]
dfs()


