import random

enemy = []


class Object:
    def __init__(self, 이름, HP, 공격력):
        self.이름 = 이름
        self.HP = HP
        self.공격력 = 공격력

    alive = True

    def 공격(self, target):
        print(f'{self.이름}는 {target.이름}을 공격했다!')
        target.damage(self.공격력)

    def status_check(self, 공격력):
        if self.alive:
            print(f'{self.이름}는 {공격력}의 피해를 입었다!')
            print(f'{self.이름}의 HP는 {self.HP}가 되었다!')
        else:
            print(f'{self.이름}는 {공격력}의 피해를 입었다!')
            print(f'{self.이름}의 HP는 0이 되었다!')
            print(f'{self.이름}는 쓰러졌다!')

    def damage(self, 공격력):
        self.HP = self.HP - 공격력
        if self.HP <= 0:
            self.alive = False

        self.status_check(공격력)


class Player(Object):
    def 마법(self, target, num):
        if num == 1:
            print(f'{self.이름}은 {target.이름}에게 백만볼트를 썼다!')
            target.damage(50)
        elif num == 2:
            self.공격력 += self.공격력
            print(f'{self.이름}의 공격력이 크게 올라갔다!')


class Monster(Object):
    def 적군(self):
        enemy.append(self)

    def 대기(self):
        print(f'{self.이름}가 대기했습니다')

    def 치료(self):
        self.HP += 10
        print(f'{self.이름}가 자신의 체력을 10만큼 회복했다')
        print(f'{self.이름}의 HP는 {self.HP}가 되었다!')

    def status_check(self, 공격력):
        if self.alive:
            print(f'{self.이름}는 {공격력}의 피해를 입었다!')
            print(f'{self.이름}의 HP는 {self.HP}가 되었다!')
        else:
            print(f'{self.이름}는 {공격력}의 피해를 입었다!')
            print(f'{self.이름}의 HP는 0이 되었다!')
            print(f'{self.이름}는 쓰러졌다!')
            enemy.remove(self)


전사 = Player('전사', 100, 10)
미니고블린 = Monster('미니고블린', 10, 10)
고블린 = Monster('고블린', 30, 30)
슈퍼고블린 = Monster('슈퍼고블린', 50, 50)

미니고블린.적군()
고블린.적군()
슈퍼고블린.적군()


def all_status_check(이름):
    if 이름.alive:
        print(f'{이름.이름} HP:{이름.HP}')


def status():
    print('------------')
    all_status_check(전사)
    for e in enemy:
        all_status_check(e)
    print('------------')


def pt():

    print('1. 공격')
    print('2. 마법')
    print('------------')
    atk = int(input('행동할 번호를 입력해주세요: '))
    while atk not in [1, 2]:
        atk = int(input('행동할 번호를 입력해주세요: '))
    print('------------')
    for i, data in enumerate(enemy):
        print(f'{i + 1}. {data.이름}')
    print('------------')
    target = int(input('행동할 번호를 입력해주세요: '))
    while target not in range(len(enemy) + 1):
        target = int(input('행동할 번호를 입력해주세요: '))
    print('------------')
    if atk == '1':
        전사.공격(enemy[target - 1])
    else:
        전사.마법(enemy[target - 1], 1)


def mt(mon):
    m = random.randrange(1, 4)
    if m == 1:
        mon.공격(전사)
    elif m == 2:
        mon.대기()
    else:
        mon.치료()


while (True):
    status()
    pt()
    if len(enemy) == 0:
        print('몬스터를 다 쓰러뜨렸다!')
        print('플레이어 승리!')
        break
    status()
    for a in enemy:
        mt(a)
    if not 전사.alive:
        print('플레이어가 쓰러졌다!')
        print('플레이어 패배!')
        break
