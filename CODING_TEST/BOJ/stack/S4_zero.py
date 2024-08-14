K = int(input())
stack = []
for _ in range(K):
    amount = int(input())
    if amount == 0:
        stack.pop()
    else:
        stack.append(amount)
print(sum(stack))