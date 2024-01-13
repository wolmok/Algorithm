# https://school.programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    answer = float('inf')
    aList = [chr(i) for i in range(ord('A'),ord('Z')+1)]
    
    if set(name) == {'A'}:
        return 0
    
    # 알파벳 계산: min(aList.index(i), 26 - aList.index(i))
    # 이동 거리 계산
    for i in range(len(name) // 2 + 1):
        l_r = name[-i:] + name[:-i] # 왼쪽먼저 갔다가 + 오른쪽
        r_l = name[i: :-1] + name[i+1:][::-1] # 기준점에서 뒤로 + 좌측
        for n in [l_r,r_l]:
    	    # 끝에 A들은 셀 필요 없으므로 자르기
            while n and n[-1] == 'A':
        	    n = n[:-1]
            cnt = [min(aList.index(c), 26 - aList.index(c)) for c in n]
            answer = min(answer, i + (len(cnt) - 1) + sum(cnt))
    return answer