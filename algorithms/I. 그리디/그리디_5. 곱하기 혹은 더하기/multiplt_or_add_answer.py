data = input()
result = int(data[0])  # 리스트의 첫번째 수로 변수를 초기화
for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result += num
print(result)
