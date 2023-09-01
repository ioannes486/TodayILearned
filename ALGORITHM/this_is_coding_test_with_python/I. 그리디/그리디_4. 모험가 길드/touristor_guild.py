import sys
sys.stdin = open('input.txt','r')
N = int(input())
men = list(map(int, input().split()))

men.sort(reverse=True)
flag = 0
result = []
for idx in range(len(men)):
    if idx != flag:
        continue
    team = []
    leader = men[idx]
    for j in range(idx, leader+1):
        team.append(men[j])
    result.append(team)
    flag += leader
    if flag >= N:
        break

print(len(result))

# 모범답안


