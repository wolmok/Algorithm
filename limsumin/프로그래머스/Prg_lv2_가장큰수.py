# https://school.programmers.co.kr/learn/courses/30/lessons/42746
# 참고: https://liveloper-jay.tistory.com/138#google_vignette

def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key = lambda x : x*3, reverse = True)
    
    
    answer = ''.join(numbers)
    
    return str(int(answer)) # 00 케이스로 인해 int 로 한 번 변환해준 후 다시 문자열로 변환