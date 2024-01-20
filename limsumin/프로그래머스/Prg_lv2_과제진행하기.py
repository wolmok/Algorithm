# https://school.programmers.co.kr/learn/courses/30/lessons/176962


from collections import deque

def convert_time_to_num(time):
    hour, minute = map(int, time.split(":"))
    return hour * 60 + minute

def solution(plans):
    answer = []
        
    # 시간이 빠른 순으로 plans 정렬
    plans = sorted(list(
        map(lambda x: [x[0], convert_time_to_num(x[1]), int(x[2])], plans)), key=lambda x: x[1])
    
    print(plans)
    # 진행 중인 과제는 queue 로 관리 + 첫 과제 enqueue
    progress = deque([plans[0]])
    now = plans[0][1]
    
    for i, element in enumerate(plans[1:]):
        next_time = element[1]
        
        while progress:
            cur_name, cur_start, cur_duration = progress.pop()
            
            if cur_start > now:
                now = cur_start
            
            duration = now + cur_duration
            
            if duration <= next_time:
                now += cur_duration
                answer.append(cur_name)
            else:
                now = next_time
                progress.append([cur_name, cur_start, duration - next_time])
                break
                
        progress.append(element)
        
    while progress:
        answer.append(progress.pop()[0])
    
    return answer
