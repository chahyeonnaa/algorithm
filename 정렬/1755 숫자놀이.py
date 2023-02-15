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
# 실패
M,N=map(int, input().split())

dict = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six',
        '7':'seven', '8':'eight', '9':'nine', '0':'zero'}

lst = []

for i in range(M, N+1):
    itoa = ' '.join(dict[j] for j in str(i))
    lst.append([i, itoa])
    
print(lst)
lst.sort(key=lambda )
for i in range(len(lst)):
    if i%10 == 0 and i!= 0:
        print(sep = '\n')
    print(lst[i][0], end=" ")
# -


