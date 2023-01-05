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
# E: 1~15 / S:1~28 / M:1~19
# while문 안 순서 중요함 *조건 탈출**
E,S,M=map(int, input().split())

E1, S1, M1=1,1,1
year=1

while True:
    if E==E1 and S==S1 and M==M1:
        break    
    E1 +=1
    S1 +=1
    M1 +=1
    
    if E1>15:
        E1=1
    if S1>28:
        S1=1
    if M1>19:
        M1=1
    year +=1
    
        
print(year)

