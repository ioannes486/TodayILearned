n = 15

cd = 0
for i in range(1, n+1):
    if n % i == 0:
        cd +=1
        print(i)
print(cd)