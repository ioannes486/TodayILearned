
def knight():
    result = 0
    input_data = input()
    x = ord(input_data[0]) - ord('a') + 1
    y = int(input_data[1])

    steps = [  # 배열에서 말이 이동하는 경우 : 작업을 미리 리스트에 저장해놓을것
        (-2,-1),
        (-2, 1),
        (2, -1),
        (2, 1),
        (-1,-2),
        (-1, 2),
        (1, -2),
        (1, 2),


    ]

    for step in steps:
        next_x = x + step[0]
        next_y = y + step[1]
        if next_x >= 1 and next_x <=8 and next_y >= 1 and next_y <= 8:
            result+=1
    return result


print(knight())