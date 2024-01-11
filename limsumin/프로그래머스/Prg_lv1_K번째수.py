# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    
    for command in commands:
        i, j, k = command[0], command[1], command[2]
        sliced_list = sorted(array[i-1: j])
        result = sliced_list[k-1]
        answer.append(result)
    return answer