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
# 알파벳순으로 정렬해서, 제일 빠른 3개를 기준으로 쪼개서 만드려고 했는데,, 어렵네
# 대중적인 정답을 브루트포스로 푸는거였다.
S=list(input())
A=[]
B=[]

for i in range(1, len(S)-1):
    for j in range(i+1, len(S)):
        a=S[:i]
        b=S[i:j]
        c=S[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        B.append(a+b+c)
        
for a in B:
    A.append(''.join(a))
print((sorted(A)[0]))
# -


