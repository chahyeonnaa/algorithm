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
# 나는 규칙 찾아서 풀었는데, 찾은 공식을 더 간소화해서 풀면 개간단하다..하..
# 핵심 : 1부터 n까지의 합 공식 사용하면 1더할때마다 반복문 안돌려도 된다.

S=int(input())

step=2
i=3
count=1

while True:
    A=step
    step +=i
    i+=1
    count+=1
    
    if A<S<=step or S<=2:
        break
        
if S<=2:
    print(1)
else:
    print(count)
        
    
