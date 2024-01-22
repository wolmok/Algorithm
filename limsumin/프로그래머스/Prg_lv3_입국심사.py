# https://school.programmers.co.kr/learn/courses/30/lessons/43238
# 이분 탐색

def solution(n, times):
    answer = float('inf')
    times = sorted(times)
    start = times[0]
    end = times[0] * n # times[-1] * n 도 가능
    
    while start<=end:
        mid = (start+end) // 2
        
        num_cnt = 0
        for time in times:
            num_cnt += (mid // time)
        
        if num_cnt >= n: # 입국관들이 처리할 수 있는 사람 수가 더 많은 경우
            answer = min(answer, mid) # answer 를 최솟값으로 업데이트
            end = mid - 1
        elif num_cnt < n:
            start = mid + 1
    return answer