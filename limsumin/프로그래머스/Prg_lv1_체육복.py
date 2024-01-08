def solution(n, lost, reserve):
    answer = n
    student = [0] * n
    
    for l in lost:
        student[l-1] -= 1
    
    for r in reserve:
        student[r-1] += 1
        
    for i in range(n):
        val = student[i] 
        
        if val == -1: # 도둑 맞은 경우
            if i >= 1 and student[i - 1] == 1: # 앞 학생이 여분이 있을 경우
                student[i-1] = 0 # 이제 여분 없음
            elif i < n-1 and student[i + 1] == 1: # 뒤 학생이 여분이 있을 경우
                student[i+1] = 0 # 이제 여분 없음
            else:
                answer -= 1 # 빌려줄 수 없음
            
            
    return answer