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

# 햄버거를 먹을 수 있는 사람의 최대 수
# 성공! 반복문 탈출 조건 더 꼼꼼하게 따지기
N,K=map(int, input().split())
S=list(map(str, input()))
count=0
for i in range(N):
    if S[i]=="P":
        for j in range(i-K, i+K+1):
            if j<0 or j>=N:
                continue
            if S[j]=="H":
                S[j]=0
                count+=1
                break
print(count)


