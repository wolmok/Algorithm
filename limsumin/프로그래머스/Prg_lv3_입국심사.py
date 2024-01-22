# https://school.programmers.co.kr/learn/courses/30/lessons/43238
# 이분 탐색

def solution(n, times):
    answer = 0
    times = sorted(times)
    start = times[0]
    end = times[0] * n
    
    while start<=end:
        mid = (start+end) // 2
        
        num_cnt = 0
        for time in times:
            num_cnt += (mid // time)
        
        if num_cnt > n:
            end = mid - 1
        elif num_cnt < n:
            start = mid + 1
        else:
            answer = start
            break
    return answer