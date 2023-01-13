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
# A를 B로 바꾸기
# B를 A로 만들자~!
# 아 자꾸 놓치는 케이스가 있다..
# 문제 풀 때, 예제 케이스만 푸는게 아니라,, 가능한 모든 경우의 수를 생각해야함
# 무작정 풀려고만 하지말고 천천히 어떤 케이스가 있는지 생각하자
A,B=map(int, input().split())
count=1

while A<B:
    if B%2==0:
        B=B//2
    elif B%10 ==1:
        B=B//10
    else:
        break
    count+=1

if A==B:
    print(count)
else:
    print(-1)
    

        


