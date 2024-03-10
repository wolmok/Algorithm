# 플로이드
# https://www.acmicpc.net/problem/11404
# 주의 : 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다는 조건 참고
# 참고 코드 : https://heo-it-til.tistory.com/entry/%EB%B0%B1%EC%A4%80-%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-11404-Python

N = int(input())  # 도시
M = int(input())  # 버스
INF = int(1e9)
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

# 이동하는데 드는 최소 비용을 저장
for _ in range(M):
    a, b, c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c

for k in range(1, N+1):
    for p in range(1, N+1):
        for q in range(1, N+1):
            graph[p][q] = min(graph[p][q], graph[p][k] + graph[k][q])

for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == INF:  # i -> j로 가지 못하는 경우
            print(0, end=' ')  # 대신 0을 출력
        else:
            print(graph[i][j], end=' ')
    print()
