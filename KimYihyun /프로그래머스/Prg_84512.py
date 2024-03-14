# 완전 탐색 - 모음사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    answer = 0
    dictionary = []
    words = "AEIOU"

    def all_counts(cnt, spell):
        if cnt == 5:
            return

        for i in range(len(words)):
            dictionary.append(spell + words[i])
            all_counts(cnt + 1, spell + words[i])

    all_counts(0, "")

    return dictionary.index(word) + 1
