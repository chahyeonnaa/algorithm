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
# 제일 작은 중량 곱하기 로프 개수 하면 될듯
# 모든 로프를 사용할 필요 없다가 핵심?

N=int(input())
rope=[]
for i in range(N):
    rope.append(int(input()))
    
rope.sort()
maxx=rope[0]*N
for i in range(1,N):
    result=rope[i]*(N-(i))
    if result>maxx:
        maxx=result

print(maxx)
