import random

start = random.randrange(1,3)
num_list = [1, 2, 3]
b31 = 0

def pf(e):
    for a in range(e):
        global b31
        global start
        if b31 == 31:
            start = 2
            return
        b31 += 1
        print('플레이어 ',b31)
    start = 2

def cf(e):
    for a in range(e):
        global b31
        global start
        if b31 == 31:
            start = 1
            return
        b31 += 1
        print('컴퓨터',b31)
    start = 1

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
        pf(p)
    elif start == 2:
        c = random.randrange(1,4)
        cf(c)
