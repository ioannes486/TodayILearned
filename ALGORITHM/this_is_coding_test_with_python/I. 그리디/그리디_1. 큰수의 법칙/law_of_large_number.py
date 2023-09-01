n, m, k = map(int, '5 8 3'.split())  # 공백으로 구분된 텍스트를 리스트로 바꾼다음 int함수를 각각 적용
data = list(map(int, '2 4 5 4 6'.split()))

data.sort()
second = data[n-2]

result = 0

# while True: # while문으로 두개의 반복문 돌리기
#
#     for i in range(k): # k 번으로 횟수가 정해져있다 - for 문 사용
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break # k번 더하고 나서 확인하지 않으면 안된다.
#     result += second
#     m -= 1

first_num = m // (k+1) * k + m % (k+1)  # 가장 큰 수가 더해지는 횟수
second_num = m // (k+1)
result = first_num * first + second_num * second

print(result)