class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack(self, other):
        print(f"{self.name}이(가) {other.name}을(를) 공격하여 {self.damage}의 피해를 입혔습니다.")