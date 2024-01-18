# 성적이 낮은 순으로 출력하기 
import sys

sys.stdin = open("limsumin/study/sort/input.txt","rt")

N = int(input())

student_list = []

for _ in range(N):
    name, score = map(str, input().split())
    score = int(score)

    student_list.append([name, score])

student_list = sorted(student_list, key= lambda x: x[1])

for student in student_list:
    print(student[0], end=' ')