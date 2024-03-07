# 치킨 배달
import sys
from itertools import combinations
sys.stdin = open("limsumin/백준/input.txt","rt")

n, m = map(int, input().split())
cities = []

for _ in range(n):
    cities.append(list(map(int, input().split())))


# 치킨 위치 구하기
chickens = []

for i in range(n):
    for j in range(n):
        if cities[i][j] == 2:
            chickens.append((i, j))

# 두 좌표의 거리를 구하는 함수
def cal_dist(x, y, a, b):
    return abs(x - a) + abs(y - b)


# 도시 전체의 치킨 거리를 구하는 함수 
def cal_c_city(chickens, city):
    val = 0
    for i in range(n):
        for j in range(n):
            if city[i][j] == 1:
                temp = int(1e9)

                for a, b in chickens:
                    temp = min(temp, cal_dist(i, j, a, b))
                
                val += temp
    
    return val

res = int(1e9)
selected_chickens = []

def find_min_dist(n, i):
    global res

    if n == m:
        res = min(res, cal_c_city(selected_chickens, cities))
        return
    
    for idx in range(i, len(chickens)):
        selected_chickens.append(chickens[idx])
        find_min_dist(n + 1, idx + 1)
        selected_chickens.pop()


for i in range(len(chickens)):
    find_min_dist(0, i)

print(res)