# https://school.programmers.co.kr/learn/courses/30/lessons/258712

def solution(friends, gifts):
    answer = 0
    f_len = len(friends)
    
    gift_list = [[0] * f_len for _ in range(f_len)]
    level_list = []
    score_list = [0] * f_len
    
    for gift in gifts:
        sender, receiver = map(str, gift.split(' '))
        s_idx = friends.index(sender)
        r_idx = friends.index(receiver)
        
        gift_list[s_idx][r_idx] += 1
            
    for i, friend in enumerate(friends):
        give = sum(gift_list[i])
        take = 0
        for gift in gift_list:
            take += gift[i]
        level_list.append(give - take)
    
    # print(gift_list)
    # print(level_list)
    
    for i in range(f_len):
        for j in range(i + 1, f_len):
            A = gift_list[i][j] # i -> j 
            B = gift_list[j][i] # j -> i
            
            if A > B:
                score_list[i] += 1
            elif A < B:
                score_list[j] += 1
            elif (A == 0 and B == 0) or (A == B):
                A_level = level_list[i]
                B_level = level_list[j]
                
                if A_level > B_level:
                    score_list[i] += 1
                elif A_level < B_level:
                    score_list[j] += 1
                else:
                    continue
    answer = max(score_list)
    return answer