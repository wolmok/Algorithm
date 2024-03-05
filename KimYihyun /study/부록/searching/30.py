# 가사 검색
# https://programmers.co.kr/learn/courses/30/lessons/60060

res = []
cnt = 0
Result = []


def solution(words, queries):
    res = count_about_query(words, queries)
    answer = question(words, queries, res)
    return answer

# 일단 queries를 순회하면서 시작
# 접두/접미사 구분 + 중복 단어 제거 필요


def count_about_query(words, queries):
    res = []
    for query in queries:
        prefix = True if query[0] == '?' else False
        query_length = len(query)
        for word in words:
            if len(word) == query_length:
                if prefix:  # 쿼리가 접두사
                    if word.endswith(query.replace('?', '')):
                        res.append(word)
                else:  # 쿼리가 접미사
                    if word.startswith(query.replace('?', '')):
                        res.append(word)
    return list(set(res))  # 중복 제거 후 반환

# 길이가 같은 아이템들을 바탕으로 와일드카드와 비교 / 실제 counting이 일어나는 함수


def question(words, queries, res):
    filtered_strings = [''.join(char for char in s if char != '?')
                        for s in queries]  # 쿼리에서 물음표 제거하고 새롭게 저장하는 리스트 생성
    for string in filtered_strings:
        for word in res:
            for i in len(string):
                if string[i] != word[i]:
                    break
            cnt += 1
    Result.append(cnt)
    return Result  # 실제 답이 될 Result 배열
