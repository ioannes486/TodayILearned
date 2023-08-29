N = int(input())
arr = list(map(int, input().split()))
add_num, sub_num, mul_num, div_num = map(int, input().split())
min_num = 1000000000
max_num = -1000000000


def calculate(idx, number, add_num, sub_num, mul_num, div_num):
	# 1. 재귀할 때마다 독립된 경우의 수를 만들기 위해서 각 사칙연산의 횟수를 
	# 변수로 두지 않고 인자로 두었다.
    
    # 2. 재귀하면서 조건을 만족하면 다음 인덱스의 수를  연산해주어야 하기 때문에 idx인자를 주었다.
    global max_num, min_num
    
    # 계산횟수를 전부 소비하면 함수를 끝내기
    if add_num == sub_num == mul_num == div_num == 0:
        max_num = max(number, max_num)
        min_num = min(number, min_num)
        return
	
    # 계산횟수가 남아있으면 계산을 해라
    if add_num > 0:
        calculate(idx + 1, number + arr[idx+1], add_num-1, sub_num, mul_num, div_num)


    if sub_num > 0:
        calculate(idx + 1, number - arr[idx+1], add_num, sub_num-1, mul_num, div_num)

    if mul_num > 0:
        calculate(idx + 1, number * arr[idx+1], add_num, sub_num, mul_num-1, div_num)

	# 나눗셈의 경우 음수 나누기 양수를 계산할 때 나누어지는 수를 양수로 바꾼 후 그 몫을 다시 음수로 바꿔줘야 하므로 경우를 두가지로 나눠서 계산했다.
    if div_num > 0:
        if number >= 0:
            calculate(idx + 1, number // arr[idx+1], add_num, sub_num, mul_num, div_num-1)
        else:
            calculate(idx + 1, -1*((-1 * number) // arr[idx + 1]), add_num, sub_num, mul_num, div_num - 1)
calculate(0, arr[0], add_num, sub_num, mul_num, div_num)


print(max_num)
print(min_num)