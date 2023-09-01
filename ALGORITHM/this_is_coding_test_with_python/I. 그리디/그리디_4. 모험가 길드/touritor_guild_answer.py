import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
data = list(map(int, input().split()))
data.sort()
'''
중요하게 봐야 할 내용
1. 어떤 것을 변수로 선언할 지
ex) 최대 그룹 수, 한 그룹의 모험가 수

2. 문제를 푸는 아이디어
항상 최소한의 모함가의 수만 포함 -> 최대한 많은 그룹 결성 -> 항상 최적의 해
'''
# 어떤 것을 변수로 선언할 지
result = 0
count = 0

for i in data:
    count += 1  # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i:
        # 현재 그룹에 포함된 모험가의 수(count)가 현재의 공포도 이상(i)이라면 == 그룹 결성!
        #
        result += 1
        count = 0

print(result)