##### 무한반복으로 다시입력하게 하기
while(True):
	p = int(input('입력하세요: '))
	if 0 < p < 101:
		break

##### range에 list를 붙히면 리스트로 출력이 가능하다

down = 101
up = 1
lr = list(range(up, down))
c = lr[int(len(lr)/2-1)]

while(True):
	if p == c:
		print(f'컴퓨터는 {c}라고 생각했다.')
		print('성공!')
		break
	if down == up:
		print(f'컴퓨터는 {up}라고 생각했다.')
		print('성공!')
		break
	print(f'컴퓨터는 {c}라고 생각했다.')
	while (True):
		pinput = input('업? 다운?: ')
		if pinput == '업' and p > c:
			break
		elif pinput == '다운' and p < c:
			break
		else:
			print('다시 입력해주세요.')

	try:
		if pinput == '업':
			up = c + 1
			lr = list(range(up, down))
			c = lr[int(len(lr) / 2 - 1)]

		if pinput == '다운':
			down = c - 1
			lr = list(range(up, down))
			c = lr[int(len(lr) / 2 - 1)]
	except:
		continue





