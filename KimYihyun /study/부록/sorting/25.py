# 실패율
# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    total_players = len(stages)  # 총 플레이어 수

    for i in range(1, N+1):
        cnt = stages.count(i)  # 해당 스테이지에 도달한 플레이어 수

        if total_players != 0:
            failure = cnt / total_players
        else:
            failure = 0

        answer.append((i, failure))  # 스테이지 번호와 실패율을 함께 저장
        total_players -= cnt  # 이미 처리한 플레이어 수 제외

    answer.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in answer]
