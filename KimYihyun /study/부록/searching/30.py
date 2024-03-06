# 가사 검색
# https://programmers.co.kr/learn/courses/30/lessons/60060

from bisect import bisect_left, bisect_right

def solution(words, queries):
    answer = []
    word_dict = {}
    reversed_word_dict = {}

    for word in words:
        word_len = len(word)
        if word_len not in word_dict:
            word_dict[word_len] = []
            reversed_word_dict[word_len] = []
        word_dict[word_len].append(word)
        reversed_word_dict[word_len].append(word[::-1])

    for key in word_dict.keys():
        word_dict[key].sort()
        reversed_word_dict[key].sort()

    for query in queries:
        if query[0] != "?":
            cnt = count_by_range(word_dict.get(len(query), []), query.replace("?", "a"), query.replace("?", "z"))
        else:
            cnt = count_by_range(reversed_word_dict.get(len(query), []), query[::-1].replace("?", "a"), query[::-1].replace("?", "z"))
        answer.append(cnt)

    return answer

def count_by_range(arr, left, right):
    left_idx = bisect_left(arr, left)
    right_idx = bisect_right(arr, right)
    return right_idx - left_idx

