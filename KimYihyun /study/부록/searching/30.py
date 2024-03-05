# 가사 검색
# https://programmers.co.kr/learn/courses/30/lessons/60060

def solution(words, queries):
    res = count_about_query(words, queries)
    answer = question(queries, res)
    return answer

# 중복 없는 저장을 위해 딕셔너리 형태를 사용
# 매칭되는 단어를 직접 세는 것은 선형 탐색으로 시간초과, 따라서 집합의 크기를 사용해야 함
def count_about_query(words, queries):
    res = {}
    for query in queries:
        prefix = True if query[0] == '?' else False
        query_length = len(query)
        res[query] = set()
        for word in words:
            if len(word) == query_length:
                if prefix:  # 쿼리가 접두사
                    if word.endswith(query.replace('?', '')):
                        res[query].add(word)
                else:  # 쿼리가 접미사
                    if word.startswith(query.replace('?', '')):
                        res[query].add(word)
    return res

def question(queries, res):
    Result = []
    for query in queries:
        cnt = 0
        filtered_strings = [s for s in res[query] if len(s) == len(query)]
        for string in filtered_strings:
            cnt += 1
        Result.append(cnt)
    return Result

