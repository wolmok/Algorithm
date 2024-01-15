# 음료수 얼려 먹기 5-10.py

N, M = map(int, input().split())  # 입력받은 맵 크기
# 방문한 좌표 / 아이스크림 개수 전역 변수로 선언
global visited, count
count = 0
container = []  # 맵 정보 저장용 컨테이너


# 맵 정보 받아오기
for i in range(N + 1):
    for j in range(M + 1):
        container.append(list(map(int, input())))

# 북 동 남 서 방향
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def find_ice_cream(x, y):

    visited = container

    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if visited[x][y] == 0:
        visited[x][y] = 1
        # 방문한 좌표에 한해 연결된 좌표를 모두 탐색
        find_ice_cream(x-1, y)
        find_ice_cream(x+1, y)
        find_ice_cream(x, y-1)
        find_ice_cream(x, y+1)
        return True
    return False
