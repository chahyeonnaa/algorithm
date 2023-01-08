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
# 2839 설탕배달
N=int(input())

# 5의 배수면, 5로 나누면 되고,
# 5의 배수가 아니면 5의 배수를 만들면됨. 3씩 빼서
# 3빼고 5의배수가 아니면, 또 3을 뺴고.. 뺀 회수 기록, 0되면 0보다 작아지면 -1

result=0
while True:
    if N<0:
        result= -1
        break
    if N%5==0:
        result+=(N//5)
        break
    else:
        N=N-3
        result+=1
        
    if N==0:
        break
        
print(result)


