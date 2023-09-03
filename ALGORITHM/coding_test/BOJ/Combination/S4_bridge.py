import sys

T = int(input())


def fact(num):
    result = 1
    for i in range(1, num+1):
        result *= i
    return result

for _ in range (T):
    N, M = map(int, sys.stdin.readline().split())
    print(fact(M) //  (fact(N)*fact(M-N)))