L, C = map(int, input().split())
alphabets = list(input().split())
alphabets.sort()

def recur(idx, letters):

    if idx == L:  # 원하는 길이에 도달할경우
        if ('a' in letters) or ('e' in letters) or ('i' in letters) or ('o' in letters) or ('u' in letters): # 모음을 하나이상 포함할경우

            # 모음만 있는 리스트 만들기
            vowels = []
            for j in letters:
                if j in 'aeiou':
                    vowels.append(j)

            if len(vowels) <= L-2: # 모음 L-2개 미만일경우 == 자음이 최소 두개 이상일경우 리턴
                print(letters)
                return
    
    for i in range(C):
        if alphabets[i] not in letters:
            if len(letters) == 0:
                recur(idx+1, letters+alphabets[i])
            elif alphabets[i] >  letters[-1]:
                recur(idx+1, letters+alphabets[i])


recur(0, '')