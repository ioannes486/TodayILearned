import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

coordinates = [list(map(int, input().split())) for i in range(N)]

x_list = [x[0] for x in coordinates]
y_list = [y[1] for y in coordinates]

print(sorted(x_list))
print(y_list)
print(x_list)