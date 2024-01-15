# 왕실의 나이트 
# 틀린 이유
# 1. ord 함수를 몰랐음
# 2. 1을 더해주지 않음

location = input()

# 현재 위치를 숫자로 변환
# ord : 문자 -> 정수
# chr : 정수 -> 문자
column = int(ord(location[0]) - ord('a') + 1)
# 1을 최종적으로 더해준 이유는 1부터 시작하기 위해서 !
row = int(location[1])

movement = [(-2, -1), (-1, -2), (1, -2), (2, -1),
            (2, 1), (1, 2), (-1, -2), (-2, 1)]
result = 0

for m in movement:
    # 일단 이동한 후에 유효성 검사
    move_row = row + m[0]
    move_col = column + m[1]

    if move_row >= 1 and move_row <= 8 and move_col >= 1 and move_col <= 8:
        result += 1

print(result)
