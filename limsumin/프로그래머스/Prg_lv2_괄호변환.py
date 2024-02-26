# https://school.programmers.co.kr/learn/courses/30/lessons/60058

# 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
def split(lst):
    left_idx = 0
    right_idx = 0
    cur_idx = 0
    for i in range(len(lst)):
        if lst[i] == "(":
            left_idx += 1
        elif lst[i] == ")":
            right_idx += 1
        if left_idx == right_idx:
            cur_idx = i
            break
    u, v = lst[0: cur_idx+1], lst[cur_idx+1:]
    return (u, v)

# 올바른 괄호 문자열인지 확인하는 함수
def check(lst):
    tmp = lst
    s = []
    idx = 0
    while idx < len(tmp):
        first = tmp[idx]
        if not s:
            s.append(first)
        elif s[-1] == "(" and first == ")":
            s.pop(-1)
        else:
            s.append(first)
        idx += 1
    if s:
        return 0
    return 1
# 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행하는 함수. 
# 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
def convert(lst):
    lst.pop(0)
    lst.pop(-1)
    
    if not lst:
        return []
    else:
        for i in range(len(lst)):
            if lst[i] == "(":
                lst[i] = ")"
            else:
                lst[i] = "("
        return lst
def change(w):
    if len(w) == 0:
        return []
    
    u, v = split(w)
    
    if check(u): 
        return u + change(v)
    else:
        new_u = convert(u)
        return ['('] + change(v) + [')'] + new_u
    
def solution(p):
    p = list(p)
    print(change(p))
    return (''.join(change(p)))