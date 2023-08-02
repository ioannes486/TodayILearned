# 다이나믹프로그래밍
import sys
sys.stdin = open('input.txt', 'r')

A, B = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0 for _ in range(A+1)]
# prefix의 첫번째 항을 0으로 만들어서 2.의 i-B가 음수가 되지 않게 만들어서
# 루프가 도는데 문제가 없게 하고 내 답안처럼 쓸데없는 조건문 안넣기


# 1. 누적합 prefix만들기
for i in range(A):
# arr    : [   3, -2, -4, -9, 0, 3, 7, 13, 8, -3]
# prefix : [0, 3, 1, -3, -12, -12, -9, -2, 11, 19, 16]
   prefix[i+1] = prefix[i] + arr[i]  # 대각선으로 더해서 다음항

# 2. 루프를 돌면서 리스트에 i에서 i-2번째 항을 뺀 값을 집어넣은 후 리스트 안에서 최댓값 구하기
lst = []
for i in range(B, A+1):
    num_b = prefix[i]
    num_a = prefix[i-B]
    lst.append(num_b - num_a)


print(max(lst))