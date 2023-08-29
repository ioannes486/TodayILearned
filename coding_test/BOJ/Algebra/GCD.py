

def gcd(a,b):
    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp
    return b

def lcm(a,b):
  return a*b//gcd(a,b)

T = int(input())
for _ in range(T):
  a,b = map(int, input().split())
  print(lcm(a,b))
