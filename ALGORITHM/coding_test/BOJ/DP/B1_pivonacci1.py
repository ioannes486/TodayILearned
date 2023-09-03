N = int(input())

def fib(n):
    if n == 1 or n== 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

f = [0 for _ in range(N+1)]
def fibonacci(n):
    result = 0
    f[0] = 1
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i-1] + f[i-2]
        result += 1
    return result - 1

print(fib(N), end=' ')
print(fibonacci(N))