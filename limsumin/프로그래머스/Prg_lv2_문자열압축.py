# https://school.programmers.co.kr/learn/courses/30/lessons/60057
# 구현, 완전 탐색

def solution(s):
    answer = len(s)
    
    if len(s) == 1:
        return 1
    
    mid = len(s) // 2
    
    for i in range(1, mid + 1, 1):
        res = ''
        cnt = 1
        prev = s[0:i]
        
        for j in range(i, len(s), i):
            if prev == s[j:j+i]:
                cnt += 1
            else:
                if cnt >= 2:
                    res += (str(cnt) + prev)
                else:
                    res += prev
                prev = s[j:j+i]
                cnt = 1
        if cnt >= 2:
            res += (str(cnt) + prev)
        else:
            res += prev  
            
        answer = min(answer, len(res))
        
    
    return answer