# 괄호 변환
# https://school.programmers.co.kr/learn/courses/30/lessons/60058?language=python3

from collections import deque


def split_str(p):  # 문자열 p를 u와 v로 분리
    open_p, close_p = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[:i + 1], p[i + 1:]


def check(u):  # 올바른 괄호로 구성된 문자열인지 체크
    queue = deque()
    for i in u:
        if i == '(':
            queue.append(i)
        else:
            if not queue:
                return False
            queue.pop()
    return True if not queue else False  # 빈 경우 True, 아닐 경우 False 반환


def solution(p):
    if not p:
        return p  # 빈 경우 그대로 반환

    u, v = split_str(p)  # 문자열 분리

    if check(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for str in u[1:len(u) - 1]:
            if str == '(':
                answer += ')'
            else:
                answer += '('
    return answer
