from collections import defaultdict

def solution(N, stages):
    answer = []
    fail_dict = defaultdict(int)
    
    stages_cnt = defaultdict(int)
    total = len(stages)
    
    for stage in stages:
        stages_cnt[stage] += 1
    
    for i in range(1, N+1):
        if total == 0:
            fail_dict[i] = 0
            continue
        if total != 0:
            fail_dict[i] = stages_cnt[i] / total
            total -= stages_cnt[i]
        else:
            fail_dict[i] = 0
            break
    
    fail_dict = sorted(fail_dict.items(), key = lambda x: -x[1])
    
    for element in fail_dict:
        answer.append(element[0])
        
    return answer