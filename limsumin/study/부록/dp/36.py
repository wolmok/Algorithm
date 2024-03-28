# 편집 거리
# https://velog.io/@dltmdrl1244/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-15483%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%8E%B8%EC%A7%91-%EA%B1%B0%EB%A6%ACEdit-Distance-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98 
import sys

sys.stdin = open("limsumin/study/부록/input.txt","rt")

word1 = input()
word2 = input()

len1 = len(word1)
len2 = len(word2)

dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

for i in range(1, len1 + 1) :
    dp[i][0] = i

for i in range(1, len2 + 1) :
    dp[0][i] = i

for i in range(len1 + 1):
    for j in range(len2 + 1):
        print(dp[i][j], end = ' ')
    print()
       
for i in range(1, len1 + 1) :
    for j in range(1, len2 + 1) :
        if word1[i-1] == word2[j-1] :
            dp[i][j] =  dp[i-1][j-1]
        
        else :
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            
print(dp[len1][len2])