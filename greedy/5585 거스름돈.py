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
price=int(input())

money=[500,100,50,10,5,1]

price=1000-price

result=0
for moneyy in money:
    A = price // moneyy
    price= price % moneyy
    result +=A
    
    if price ==0:
        break
    
print(result)
