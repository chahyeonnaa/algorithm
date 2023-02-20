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
N=int(input())
S=list(map(int, input().split()))
result=[]
S.sort()

start=0
end=len(S)-1
for i in range(N):
    result.append(S[end]+S[start])
    end -=1
    start +=1
print(min(result))
# -


