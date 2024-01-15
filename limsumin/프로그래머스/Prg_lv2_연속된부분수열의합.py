# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    answer = []
    
    right = 0
    cum_sum = 0
    count = float('inf')
    min_right = 0
    min_left = 0
    
    for i in range(len(sequence)):
        while cum_sum < k and right < len(sequence):
            cum_sum += sequence[right]
            right += 1 
            
        if cum_sum == k:
            if count > (right - i):
                count = right - i
                min_right = right - 1
                min_left = i
        
        cum_sum -= sequence[i]
    answer.append(min_left)
    answer.append(min_right)
    return answer