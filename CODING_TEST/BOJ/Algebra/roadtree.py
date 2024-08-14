N = int(input())
trees = [int(input()) for _ in range(N)]


def gcd(a,b):
    while a % b != 0:
        tmp = a % b
        a = b
        b = tmp
    return b

margins = []
for idx in range(N-1):
    margins.append(trees[idx+1] - trees[idx])
    
g = margins[0]
for idx in range(N-2):
    g = gcd(margins[idx+1], g)

result = 0
for each in margins:
    result += each // g - 1
print(result)
# if trees[-1] % result == 0:
#   print(((trees[-1]//result)) - N)
# else:
#   print(((trees[-1]//result)+1) - N)