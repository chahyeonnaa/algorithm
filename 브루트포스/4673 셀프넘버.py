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
# 33=33+3+3=39 -> 39의 생성자는 33
# 생성자가 없는 숫자 - 셀프넘버
# 집합 간의 차집합 연산이 가능하다는 것.. 중요..
number=set(range(1, 10001))
self_number=set()

for i in range(1,10001):
    for j in str(i):
        i +=int(j)
    self_number.add(i)
    
result=sorted(number-self_number)
for i in result:
    print(i)
        
# -


