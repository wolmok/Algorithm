# 문자열 재정렬
S = input()  # 주어지는 문자열

sorted_list = sorted(S)  # 숫자부터 알파벳까지 정렬
print(sorted_list)
numbers = []

for item in sorted_list:
    if item.isdigit():  # 숫자로만 이루어진 경우
        numbers.append(item)  # 새 리스트에 숫자만 저장

# 문자만 존재하는 문자열 생성
result_string = ''.join(
    item for item in sorted_list if not item.isdigit())

print(result_string + ''.join(numbers))  # 둘을 더해서 출력
