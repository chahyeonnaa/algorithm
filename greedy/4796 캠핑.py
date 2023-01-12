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

i=1
while True:
    result=0
    L,P,V=map(int, input().split())
    if L==0 and P==0 and V==0:
        break
    
    cycle=V//P
    NA=V%P
    result += L*cycle
    if NA<=L:
        result += NA
    else:
        result +=L
    print(f"Case {i}: {result}")
    i+=1


