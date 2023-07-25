# import sys
# sys.stdin = open('input.txt', 'r')

#h = int(input())
h = 5

count = 0
for i in range(h+1):  # 0시부터 h시 까지의 시간을 구해야 하기 때문에 1을 더해준다.
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
            # 시간을 hhmmss형태의 문자열로 만들어서 3이 포함되어있는지 검사
            # : 포함관계를 이야길 할 경우 문자열을 많이 사용한다.
                count +=1
print(count)


