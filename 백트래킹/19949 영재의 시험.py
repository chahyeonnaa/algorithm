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
def dfs(s):
    global count
    if len(result)==10:
        point=0
        for i in range(10):
            if result[i]==S[i]:
                point +=1
        if point>=5:
            count +=1
        return
    for i in range(1, 6):
        if s>=2 and result[s-1]==result[s-2]==i:
            continue
        result.append(i)
        dfs(s+1)
        result.pop()
        
S=list(map(int, input().split()))
result=[]
count=0
dfs(0)
print(count)
# -


