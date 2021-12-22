down = 101
up = 1
lr = list(range(up, down))
p = 101
##### 무한반복으로 다시입력하게 하기
while p not in lr:
    try:
        p = int(input('입력하세요: '))
    except:
        continue

##### range에 list를 붙히면 리스트로 출력이 가능하다
while (True):
    c = lr[int(len(lr) / 2 - 1)]
    if p == c:
        print(f'컴퓨터는 {c}라고 생각했다.')
        print('성공!')
        break
    if down == up:
        print(f'컴퓨터는 {up}라고 생각했다.')
        print('성공!')
        break
    print(f'컴퓨터는 {c}라고 생각했다.')

    pinput = input('업? 다운?: ')

    if pinput == '업' and p > c:
        up = c + 1
        lr = lr[lr.index(c) + 1:]
    elif pinput == '다운' and p < c:
        down = c - 1
        lr = lr[:lr.index(c)]
    else:
        print('다시 입력해주세요.')