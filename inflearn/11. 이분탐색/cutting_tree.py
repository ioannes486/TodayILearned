import sys
sys.stdin = open('cutting_tree.txt','r')

n, m = map(int, input().split()) # n 나무의 개수 m 필요한 목재의 양
trees = list(map(int, input()).split())  # 나무의 리스트

s = 0
e = max(trees)
while s <= e:
    mid = (s+e)//2

    wood = 0
    for tree in trees:  # 나무가 자르는 높이보다 클 경우 목재의 양을 더해 산출한다.
        if tree >= mid:
            wood += tree - mid

    if wood >= m:  # 목재의 양이 주어진 최솟값보다 클 경우 아래 포인터를 올린다.
        s = mid + 1
    else:  # 목재의 양이 주어진 최솟값보다 작을 경우 위 포인터를 내린다.
        e = mid - 1