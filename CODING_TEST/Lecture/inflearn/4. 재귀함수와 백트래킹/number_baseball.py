import sys
sys.stdin = open('number_baseball.txt', 'r')
sys.setrecursionlimit(999999999)


def checker(idx, number):
    # 힌트 안의 변수
    # hint[0] : [123,0,1]
    _number = hint[idx][0]
    _strike = hint[idx][1]
    _ball = hint[idx][2]

    strike = 0
    ball = 0

    # 힌트에서 각 자리숫자를 꺼내기
    _A = _number // 100  # 123 / 100 몫
    _B = (_number - (_A * 100)) // 10  # 23 / 100 몫
    _C = _number % 10  # 123 / 10 나머지

    # 조사할 숫자에서 각 자리 숫자를 떠내기
    A = number // 100  # 123 / 100 몫
    B = (number - (A * 100)) // 10  # 23 / 100 몫
    C = number % 10  # 123 / 10 나머지

    # 0이 들어가면 안됨
    if A == 0 or B == 0 or C == 0:
        return False

    # 숫자가 중복되면 안됨
    if A == B or A == C or B == C:
        return False

    # 숫자가 같으면 스트라이크
    if A == _A:
        strike += 1
    if B == _B:
        strike += 1
    if C == _C:
        strike += 1

    # 숫자가 같고 자리수가 다르면 볼
    if A == _B or A == _C:
        strike += 1
    if B == _A or B == _C:
        ball += 1
    if C == _A or C == _B:
        ball += 1

    # 스트라이크와 볼의 개수가 같으면 같다고 말하기
    if strike == _strike and ball == _ball:
        return True

    return False


def recur(idx, number):
    global answer
    if idx == N:  # 모든 힌트를 통과하면 답을 만족하는 숫자개수 늘리기
        answer += 1
        recur(0, number+1)  # 모든 힌트를 통과하면 다음 숫자로 넘어가기
        return
    if number == 1000:  # 0부터 999까지의 수를 조사하고 1000이 되면 재귀 종료
        return

    if checker(idx, number):
        recur(idx+1, number)
    else:
        recur(0, number+1)  # 조사한 수가 탈락하면 다음 수로 넘어가기
        # 스트라이크와 볼카운트가 동일하다면 힌트 통과


N = int(input())
hint = [list(map(int, input().split())) for _ in range(N)]

answer = 0
recur(0, 100)
print(answer)