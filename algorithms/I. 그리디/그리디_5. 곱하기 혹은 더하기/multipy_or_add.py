num_list = [0, 2, 9, 8, 4]
# 작은 수는 더하고, 큰 수는 곱하고

num_list.sort()
result = 0

for num in num_list:
    if result == 0 or num <= 1:
        result += num
    else:
        result *= num

print(result)

