N = int(input())
result = 0
if N not in [7,4]:
    if N % 5 == 0:
        result = N//5
    elif N % 5 == 4:
        result = N//5 -1 +3
    elif N % 5 == 3:
        result = N//5 + 1
    elif N % 5 == 2:
        result = N//5 -2 +4
    elif N % 5 == 1:
        result = N//5 -1 +2
else:
    result = -1
print(result)