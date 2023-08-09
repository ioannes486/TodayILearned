import sys
sys.stdin = open('thanos.txt','r')

N = int(input())
arr1 = sorted(list(map(int, input().split())))  # 수열

M = int(input())
arr2 = list(map(int, input().split()))  # 찾아야 할 숫자.

lst = []
for number in arr2:  # 찾아야 할 숫자에 대해 한개씩 루프를 돈다.
    s = 0
    e = N-1
    flag = 0
    while s <= e:  # 교차되지 않았다면. 이 조건의 역, 즉 아래포인터가 위 포인터보다 크거나 같은 경우가 교차된 경우이다.
        mid = (s+e)//2

        if arr1[mid] == number:  # 숫자를 맞히면 종료해라
            flag = 1
            break

        elif arr1[mid] < number:
        # 숫자를 못 맞히고 그 숫자가 가운데 숫자보다 작을 경우 아래 포인터를 가운데 숫자에서 한칸 더 위로 옮겨라
        # 이때 한칸 더 위로 옮기는 이유는 어차피 가운데 숫자는 정답이 아니기 때문
            s = mid + 1

        elif arr1[mid] > number:
        # 숫자를 못 맞히고 그 숫자가 가운데 숫자보다 클 경우 위 포인터를 가운데 숫자에서 한칸 더 아래로 옮겨라
        # 이때 한칸 더 아래로 옮기는 이유는 어차피 가운데 숫자는 정답이 아니기 때문
            e = mid - 1

    lst.append(flag)
print(*lst)