L, C = map(int, input().split())
alphabets = list(input().split())
alphabets.sort()

result = ''
def recur(idx, letters):
    global result

    if idx == L:
        return
    for i in range(L):
        if alphabets[i] not in letters:
            if ('a' in letters) or ('e' in letters) or ('i' in letters) or ('o' in letters) or ('u' in letters):
                if
            recur(idx+1, letters+alphabets[i])

    if ('a' in letters) or ('e' in letters) or ('i' in letters) or ('o' in letters) or ('u' in letters):
        if


recur()
print(alphabets)