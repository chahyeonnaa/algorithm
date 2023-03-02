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

# 공식찾기가 핵심이었던 .. 문제,,
T=int(input())
for i in range(T):
    N=int(input())
    dict={}
    for i in range(N):
        A,B=map(str, input().split())
        if B not in dict:
            dict[B]=1
        else:
            dict[B]+=1
    result=1
    G=list(dict.values())
    for key in G:
        result *=(key+1)
    print(result-1)


