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
# 키 포인트
# int를 str로 바꿔서 리스트 형태를 만들고, 이걸 연산하기 위해 다시 숫자로 바꿔줌
# map을 잘 쓰면 번거로워지지 않는다..
N=int(input())

result=0

if N<=99:
    result+=N
else:
    result+=99
    for i in range(100,N+1):
        number=list(map(int, str(i)))
        if number[0]-number[1]==number[1]-number[2]:
            result+=1
             
print(result)
