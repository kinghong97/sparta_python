import random

start = random.randrange(1,3)
num_list = [1, 2, 3]
b31 = 0
b31_win_list = list(range(2, 31, 4))

def f(e, b31, start):
    if start == 1:
        for a in range(e):
            if b31 == 31:
                return b31, 2
            b31 += 1
            print('플레이어 ', b31)
        return b31, 2
    else:
        for a in range(e):
            if b31 == 31:
                return b31, 1
            elif b31 in b31_win_list:
                return b31, 1
            b31 += 1
            print('컴퓨터 ', b31)
        return b31, 1

while (True):
    if b31 == 31:
        if start == 1:
            print('플레이어 승리!')
        else:
            print('컴퓨터 승리!')
        break
    elif start == 1:
        p = 0
        while p not in num_list:
            try:
                p = int(input('숫자를 입력하세요: '))
            except:
                print('다시 입력해주세요')
                continue
        b31, start = f(p, b31, start)
    elif start == 2:
        if b31 in b31_win_list:
            b31 += 1
            print('컴퓨터', b31)
            c = 2
            b31, start = f(c, b31, start)
        else:
            c = 3
            b31, start = f(c, b31, start)