# https://school.programmers.co.kr/learn/courses/30/lessons/84512

from itertools import product

def solution(word):
    answer = 0
    words = ['A','E','I','O','U']
    lst = []
    # 모든 중복 숫자 조합 구하기
    for i in range(1, 6):
        for j in product(words, repeat = i):
            lst.append(list(j))
            
    # 알파벳 순서대로 sort        
    lst.sort()
    
    for i in lst:
        answer += 1
        cur_str = ''.join(s for s in i)
        if word == cur_str:
            break
    
    return answer