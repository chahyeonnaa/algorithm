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
# 나는 X의 개수를 하나하나 세려고 했음. 그러면 코드가 너무 복잡해진다
# 문자열이니까 슬라이스 써서 묶으면 편하다
S=input()
idx=0
result=''
while idx<len(S):
    if S[idx:idx+4]=="XXXX":
        result+="AAAA"
        idx +=4
    elif S[idx: idx+2]=="XX":
        result +="BB"
        idx+=2
    elif S[idx]=="X":
        result=-1
        break
    else:
        result += S[idx]
        idx+=1
        
print(result)

# +
# replace 사용
S=input()

S=S.replace("XXXX","AAAA")
S=S.replace("XX","BB")

if "X" not in S:
    print(S)
else:
    print(-1)
# -

# 문자열을 리스트로 만들었을때와 아닐때의 차이!!!!
S=input()
A=list(input())
print(S[0:2])
print(A[0:2])


