# 틀렸던 이유 : 아래 주석과 같이 입력 & 변환시
# 입력값인 02984가 숫자로 이루어진 하나의 문자열이므로 공백 기준 분할 X, 문자열 전체를 하나의 요소로 반환함
# 이 과정에서 맨 앞의 0이 사라지게 됨
# num_list = list(map(int, input().split()))
# print(num_list)

# 올바른 방법
def cal(res):
    # 0이 있는 경우
    global sum_first
    for i in range(len(sorted_list)):
        if sorted_list[i] == 0:
            sum_first = (sorted_list[i] + sorted_list[i+1])
            print(sum_first, 'sum_first')
            res += sum_first
        else:
            res *= sorted_list[i]
    # 0이 없는 경우
    else:
        for i in range(len(sorted_list)):
            if res == 0:
                res = sorted_list[i]
            else:
                res *= sorted_list[i]
    return res


input_string = input()
num_list = []
res = 0

for item in input_string:
    if item.isdigit():  # 모두 숫자로 이루어져있는 경우에만 True를 반환
        num_list.append(int(item))

sorted_list = sorted(num_list)


print(cal(res))
