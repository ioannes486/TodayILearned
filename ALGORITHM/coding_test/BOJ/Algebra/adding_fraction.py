def gcd(a,b):
    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp
    return b

a, b = map(int, input().split())
c, d = map(int, input().split())

mo = b*d
ja = (a*d) + (b*c)

yieled = gcd(mo, ja)
print(ja // yieled, end=' ')
print(mo // yieled)

