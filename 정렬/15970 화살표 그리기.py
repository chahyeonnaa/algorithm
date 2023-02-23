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
# 74퍼에서 틀림. 왜지?
# 도대ㅊ ㅔ어디가 틀린건데.
# 와 ㅅㅂ... 서브테스크 문제는 서브테스크 조건도 잘 봐야함 ㅠㅠ
# 반복문 돌릴 때 점의 개수 안맞춰줘서 한참을 헤맸다.....
N=int(input())
S=[[]*(N+1) for _ in range(N+1)]
for _ in range(N):
    A,B=map(int, input().split())
    S[B].append(A)
    
result=0
for i in range(1,N+1):
    S[i].sort()
    R=len(S[i])
    for j in range(R):
        if j== 0:
            result += (S[i][1]-S[i][0])
        elif j== R-1:
            result += (S[i][R-1]-S[i][R-2])
        else:
            Q=S[i][j]-S[i][j-1]
            W=S[i][j+1]-S[i][j]
            result += min(Q,W)
print(S)
print(result)
# -

