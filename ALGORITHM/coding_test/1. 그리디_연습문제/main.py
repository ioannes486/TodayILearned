n = 1260
count = 0
coin_types = [500, 100, 50, 10]
for coin in coin_types:
    count += n // coin  # n을 코인을 나눈 몫 : n에 들어갈 수 있는 동전의 최대 개수
    n %= coin # nd을 coin으로 나눈 나머지 : 동전으로 지불하고 남은 액수
print(count)
# 그리디 알고리즘에서는 문제풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할 수 있어야 한다.