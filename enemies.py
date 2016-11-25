# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

    def question(self):
        pass
class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный дракон'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health = 80
        self._attack = 10
        self._color = 'красный дракон'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest
class BlackDragon(Dragon):
    def __init__(self):
        self._health = 60
        self._attack = 10
        self._color = 'чёрный дракон'

    def question(self):
        x = randint(1,20)
        y = randint(1,20)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest

class Warlord(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'тролль warlord'

    def question(self):
        x = randint(1,5)
        print(x)
        self.__quest = 'Угодай число от 1 до 5'
        self.set_answer(x)
        return self.__quest
class Simplelord(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'тролль Simplelord'

    def question(self):
        x = randint(1,200)
        print(x)
        self.__quest = 'Ето просто число?(Yes/No)'
        if x == 1:
            t = 0

        i = 2
        while i * i < x:
            t = int(x % i != 0)
            if t:
                break
            i += 1
        self.set_answer(t)
        return self.__quest


#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.


enemy_types = [Simplelord]