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
# 성공!
# 예제 뿐만 아니라 가능한 모든 경우의 수를 차근차근 생각해보자 그러면 풀린다..
N,M=map(int, input().split())
package=[]
one=[]
result=0
for i in range(M):
    A,B=map(int, input().split())
    package.append(A)
    one.append(B)

mini_P=min(package)
mini_O=min(one)

if mini_P>(mini_O*6):
    result += (mini_O * N)
else:
    result +=(N//6)*mini_P

    O=(N%6)*min(one)
    if O<mini_P:
        result +=O
    else:
        result +=mini_P
    
print(result)
    
