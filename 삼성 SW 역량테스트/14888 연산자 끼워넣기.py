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
# 백트래킹 문제 : 만들 수 있는 식의 결과가 최대, 최소인것 찾기
# -> 어쨌거나 다 만들어서 확인해봐야함 -> 백트래킹으로 풀건데...
# 연산자 4개, 순간의 선택 4개 할 수 있음 -> 각각 재귀 함수 필요
# depth 매개변수로 숫자 개수 카운트, 숫자 개수만큼 차면 return(탈출 조건)
# 각 조건문에서 다음 조건문으로 넘어갈 때는 값이 복귀됨
# 어렵다.. 어떻게 이런 생각을? 그냥 외우자. 외워......


def dfs(depth,result,plus, minus, multi, divide):
    global max_e, min_e
    if depth==N:
        max_e=max(result,max_e)
        min_e=min(result, min_e)
        return
    
    if plus:
        dfs(depth+1, result+A[depth],plus-1,minus, multi, divide)
    if minus:
        dfs(depth+1, result-A[depth],plus,minus-1, multi, divide)
    if multi:
        dfs(depth+1, result*A[depth],plus,minus, multi-1, divide)
    if divide:
        dfs(depth+1, int(result/A[depth]),plus,minus, multi, divide-1)
        
              
N=int(input())
A=list(map(int, input().split()))
plus, minus, multi, divide=map(int, input().split())
max_e=-1e9
min_e=1e9

result=A[0]
dfs(1,result,plus, minus, multi, divide)
print(max_e)
print(min_e)
