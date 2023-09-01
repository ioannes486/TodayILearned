
T = int(input())
for i in range(T):
  stack = []
  vps = input()
  for par in vps:  # 문자열 왼쪽에서 괄호를 확인해서
    if par =='(': # ( 이면 스택에 추가
      stack.append(par) 
    elif par ==')':  # ) 이면 스택에서 뺴기 -> 항상 스택을 빈 상태로 유지해서 그 상태가 끝까지 지속되면 YES이다.
      if stack:  
        stack.pop()
      else:  # )일 때 스택이 비어있으면 == 제일 왼쪽 괄호가 ) {예) )()()} 이면 바로 NO
        print('NO')
        break
  else:  # for 문이 다 지났을 때 수행하기
    if not stack:
      print('YES')
    else:
      print('NO')