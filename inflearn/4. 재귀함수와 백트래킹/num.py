import sys
sys.stdin = open('number_baseball.py','r')
sys.setrecursionlimit(9999999)


def checker(idx,number):
    _number = hint[idx][0]
    _strike = hint[idx][1]
    _ball = hint[idx][2]

    strike = 0
    ball = 0

    _A = _number // 100
    _B = (_number - (_A * 100)) // 10
    _C = _number % 10


    A = number // 100
    B = (number - (A * 100)) // 10
    C = number % 10

    if A == 0 or B == 0 or C == 0:
        return False

    if A == B or A == C or B == C:
        return False

    if A == _A:
        strike+= 1
    if B == _B:
        strike+= 1
    if C == _C:
        strike+= 1

    if A == _B or A == _C:
        ball += 1
    if B == _A or B == _C:
        ball += 1
    if C == _A or C == _B:
        ball += 1

    if strike == _strike and ball == _ball:
        return True

    return False


def recur(idx, number):
    global answer

    if idx == n:
        answer += 1
        # print(number)
        recur(0, number+1)
        return

    if number == 1000:
        return

    if checker(idx,number):
        recur(idx+1, number)
    else:
        recur(0, number+1)

n = int(input())
hint = [list(map(int,input().split())) for _ in range(n)]
answer = 0
recur(0, 100)
print(answer)
