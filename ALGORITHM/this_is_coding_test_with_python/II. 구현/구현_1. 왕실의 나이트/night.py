cor = input()

alpha_list = ['a','b','c','d','e','f','g','h']
num_list = [1,2,3,4,5,6,7,8]

x = 0
y = 0
cnt = 0
for i in range(2):
    if i == 0:
        x = alpha_list.index(cor[i]) + 1
    elif i == 1:
        y = int(cor[i])

if x + 2 in num_list:
    if y + 1 in num_list:
        cnt += 1
    if y - 1 in num_list:
        cnt += 1

if x - 2 in num_list:
    if y + 1 in num_list:
        cnt += 1
    if y - 1 in num_list:
        cnt += 1

if y + 2 in num_list:
    if x + 1 in num_list:
        cnt += 1
    if x - 1 in num_list:
        cnt += 1

if y - 2 in num_list:
    if x + 1 in num_list:
        cnt += 1
    if x - 1 in num_list:
        cnt += 1

print(x,y)
print(cnt)

# for i in range(1, 9):
#     i