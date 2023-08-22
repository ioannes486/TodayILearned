T = int(input())
test_cases = [int(input()) for _ in range(T)]
# result = 0


def recur(number):
    global result
    if number == 0:
        result += 1
        return
    elif number < 0:
        return

    recur(number-1)
    recur(number-2)
    recur(number-3)


for case in test_cases:
    result = 0
    recur(case)
    print(result)
