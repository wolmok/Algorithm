# 동전 게임
# https://www.acmicpc.net/problem/9079

def game(coins):
    global result
    for bit_mask in range(2**8):
        copy_coins = [row[:] for row in coins]
        change_bit = str(bin(bit_mask))[2:].count('1')
        if result < change_bit:
            continue
        for row in range(3):
            if bit_mask & (1 << row):
                for col in range(3):
                    copy_coins[row][col] = (copy_coins[row][col]+1) % 2

        for col in range(3):
            if bit_mask & (1 << (col+3)):
                for row in range(3):
                    copy_coins[row][col] = (copy_coins[row][col]+1) % 2

        if bit_mask & (1 << 6):
            for row in range(3):
                copy_coins[row][row] = (copy_coins[row][row]+1) % 2

        if bit_mask & (1 << 7):
            for row in range(3):
                copy_coins[row][2-row] = (copy_coins[row][2-row]+1) % 2

        sum_temp = sum(list(map(sum, copy_coins)))
        if sum_temp == 9 or sum_temp == 0:
            result = change_bit


T = int(input())
for _ in range(T):
    coins = []
    result = float('inf')
    for _ in range(3):
        a = list(input().split())
        for i in range(3):
            if a[i] == 'T':
                a[i] = 1
            else:
                a[i] = 0
        coins.append(a)
    cnt = 0

    game(coins)
    print(-1 if result == float('inf') else result)
