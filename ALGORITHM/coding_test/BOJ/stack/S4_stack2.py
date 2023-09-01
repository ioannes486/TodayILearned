stack = []
N = int(input())
for _ in range(N):
    task = input().rstrip()
    if len(task) > 2:
        stack.append(int(task[2:]))  # task에서 세번째 글자 꺼내기 '1 3' -> 공백을 포함해서 스택에 넣어야 하는 수는 세번째 글자임
# 문자열 인덱스 활용하기

    elif task[0] == '2':
        if len(stack) == 0:
            print(-1)
            
        else:
            print(stack.pop())
            
    elif task[0] == '3':
        print(len(stack))
        
    elif task[0] == '4':
        if len(stack) == 0:
            print(1) 
        else:
            print(0)
    elif task[0] == '5':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
      
    
        # print(result)
