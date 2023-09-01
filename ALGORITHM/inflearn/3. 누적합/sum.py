import sys
sys.stdin = open('input.txt', 'r')

A, B = map(int, input().split())
num_list = list(map(int, input().split()))
prefix = []
prefix = [0 for _ in range(A+1)]

# 누적합 prefix만들기
start_num = num_list[0]
for i in range(A):
    start_num += num_list[i]
    prefix.append(start_num)

# 루프를 돌면서 리스트에 i에서 i-2번째 항을 뺀 값을 집어넣은 후 리스트 안에서 최댓값 구하기
lst = []
for i in range(B-1, A):
    num_b = prefix[i]
    if i - 2 < 0:
        num_a = 0
    else:
        num_a = prefix[i-2]
    lst.append(num_b - num_a)


print(prefix, lst , max(lst))