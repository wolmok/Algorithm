# 문자열 압축
# https://school.programmers.co.kr/learn/courses/30/lessons/60057


def solution(s):
    shorten_num = [i for i in range(1, (len(s)//2+1))]
    answer = len(s)

    for length in shorten_num:
        key = s[:length]
        new_str = []
        count = 1

        for i in range(length, len(s), length):
            if key == s[i:i+length]:
                count += 1
            else:
                new_str.append([key, count])
                count = 1
                key = s[i:i+length]
        new_str.append([key, count])

        answer = min(answer, sum(
            [len(key) + (len(str(count)) if count > 1 else 0) for key, count in new_str]))
    return answer
