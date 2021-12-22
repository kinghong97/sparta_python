import random

##### random.randrange(1,101) 지정숫자 사이의 값을 하나 출력한다
c = random.randrange(1,101)
p = 101
for _ in range(5):
	##### 같진 않지만 다운인데 다운인 수를 입력하지 않았을때 예외처리하는 법은 모르겠다
	while (True):
		np = int(input('입력하세요: '))
		if p != np:
			p = np
			break
		else:
			print('다시 입력해주세요.')
	print(p)
	if c == p:
		print('성공!')
		print(f'정답은: {c}')
		break
	if c < p:
		print('다운')
		continue
	if c > p:
		print('업')
		continue
if c != p:
	print('실패!')
	print(f'정답은: {c}')


