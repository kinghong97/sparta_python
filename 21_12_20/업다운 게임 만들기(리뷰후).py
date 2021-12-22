import random

##### random.randrange(1,101) 지정숫자 사이의 값을 하나 출력한다
c = random.randrange(1,101)

for _ in range(5):
    p = int(input('입력하세요: '))
    print(p)
    if c < p:
        print('다운')

    elif c > p:
        print('업')

    else:
        print('성공!')
        print(f'정답은: {c}')

if c != p:
	print('실패!')
	print(f'정답은: {c}')