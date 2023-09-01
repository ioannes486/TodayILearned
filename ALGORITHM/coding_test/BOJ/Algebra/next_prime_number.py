T = int(input())
#완전탐색

def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
      if x % i ==0:
        return False
    return True

for i in range(T):
    x = int(input())
    while True:
        if is_prime(x):
            print(x)
            break
        else: x += 1
            
# def prime_number(N):
#     i = 2
#     while True:
#         if N == 0 or N == 1 or N == 2:
#             return 2

#         if N % i == 0:
#             N += 1
#             i = 2
#             continue

#         else:
#             i += 1

#         if i >= N**0.5:
#             return N

# for _ in range(T):
#     print(prime_number(int(input())))
