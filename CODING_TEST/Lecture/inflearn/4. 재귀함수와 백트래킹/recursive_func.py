def recur(number):
    # number : 재귀 for문의 깊이를 표시,
    # output : 산출된 수열
    if number == M:  # 종료조건 설정
        print(*arr)  # arr 안의 원소만 출력
        return

    # 하나의 수열을 만드는 루프
    for i in num_list:
        # 재귀함수를 사용하므로써 3개의 for문이 독립적으로 돌아간다
        # number = 1일 때, number = 2일 때, number는 3일 때의 for 문의 루프가 다르다
        # 따라서 3중 for 문의 루프가 다른 것
        # if i in arr:
        #     continue
        # if arr != []:
        #     if i <= arr[-1]:
        #         continue
        arr.append(i)  # 리스트에 수열 담기(일종의 스택)
        recur(number+1)
        arr.pop()  # 수열 없애기

N, M = map(int, input().split())  # M = 범위, N = 숫자의 개수
num_list = list(map(int, input().split()))
num_list.sort()
arr = []
recur(0)