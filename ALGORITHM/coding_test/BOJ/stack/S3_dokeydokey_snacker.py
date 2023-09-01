N = int(input())
arr = list(map(int, input().split()))


stack = []
num = 1
for i in range(N):
    if arr[i] == num:
        num += 1
    else:
        stack.append(arr[i])
        # print(stack)
else:
    if not stack:
        print("Nice")
    else:
        for _ in range(len(stack)):
            if stack.pop() == num:
                #stack.pop()
                num += 1
            else:
                print("Sad")
                break
        else:
            print("Nice")