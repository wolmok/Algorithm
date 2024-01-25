# 7-5.py
# 시작점/끝점/중간점 이용하기

N = int(input())
store = list(map(int, input().split()))
store.sort()  # 기준이 될 리스트이므로 정렬
# print(store)

M = int(input())
customer = list(map(int, input().split()))
# print(customer)


def searchFunc(ary, target, start, end):
    global answer
    # 시작점/끝점으로 범위 설정
    while start <= end:
        # 중간점 구하기
        mid = (start + end) // 2
        # 중간점이 정답이면 바로 반환
        if ary[mid] == target:
            return mid
        # 중간점이 타겟보다 크면 끝점 변경
        elif ary[mid] > target:
            end = mid - 1
        # 중간점이 타겟보다 작으면 시작점 변경
        else:
            start = mid + 1
    # 조건에 벗어나는 경우 예외 처리
    return None


for i in customer:
    answer = searchFunc(store, i, 0, N - 1)
    if answer == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')
