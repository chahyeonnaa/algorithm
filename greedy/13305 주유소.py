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
# 처음에는 부분 성공 : 제일 첫 주유소에서 최소로 넣어주고, 오름차순 정렬해서 제일 싼 곳에서 와장창 넣었음
# 이렇게 하면, 가다보면 기름이 부족할 수 있음 -> 주유소의 순서를 고려하지 않음
N=int(input())
KM=list(map(int, input().split()))
L=list(map(int, input().split()))

oil=KM[0]*L[0]
cost_mini=L[0]
for i in range(1,N-1):
    if cost_mini>L[i]:
        cost_mini=L[i]
        
    oil += (cost_mini*KM[i])
    
print(oil)
