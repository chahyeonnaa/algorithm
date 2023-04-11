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
# DFS(깊이우선탐색)
# 깊은 곳으로 계속 들어감
# 시작노드부터 도는데, 방문하지 않은 노드가 있으면 재귀호출
# DFS는 append하고, 호출하고, 다시 pop해주고 이런 루틴이 많이 쓰임
# 조건에 도달하면(주로 cnt 매개변수가 조건에 도달하면, 재귀 호출 멈춤) 리턴
# 즉 조합 개수 만큼 뽑으면 리턴함
# DFS는 어떨때 써야하는지 잘 감이 안온당 -> DFS는 무조건 조합 조합 기억하자 조합


# BFS(너비우선탐색)
# 연결된 곳 먼저 다 방문
# 큐에서 노드를 꺼내고, 인접 노드 중에서 방문하지 않은 노드를 다 큐에 넣고 방문처리
# 큐에서 꺼내기를 반복
# 큐가 빌 때까지 반복
# BFS는 보통 상하좌우대각선으로 바이러스가 퍼지거나, 영역을 확장시키거나 할 때 주로 씀
# 난 BFS가 편하긴함

# 연결요소의 개수세기(DFS, BFS 둘다 풀이 가능)



