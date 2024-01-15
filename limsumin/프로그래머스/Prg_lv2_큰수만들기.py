# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = ''
    
    # stack 이용한 풀이
    stack = []
    
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)
    
    if k > 0: # k 가 다 소진 되지 못한 경우
        stack = stack[:-k]
    answer = ''.join(stack)
    return answer