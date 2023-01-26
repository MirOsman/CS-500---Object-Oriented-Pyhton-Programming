import random
from typing import Counter

class Dice:
    def __init__(self) -> None:
        self.__dicelist = []
        for i in range(3):
            self.__dicelist.append(random.randint(1,2))


    @property
    def dice1(self) -> int:
        return self.__dicelist[0]

    @property
    def dice2(self) -> int:
        return self.__dicelist[1]

    @property
    def dice3(self) -> int:
        return self.__dicelist[2]

    def toss(self) -> int:
        sum = 0
        for i in range(len(self.__dicelist)):
            self.__dicelist[i] = random.randint(1,6)
            sum += self.__dicelist[i]
        return sum


def main():
    d = Dice()
    print('Dice 1:', d.dice1)
    print('Dice 2:', d.dice2)
    print('Dice 3:', d.dice3)

    count = 0
    while True:
        sum = d.toss()
        count += 1
        if sum == 18:
            print(d.dice1, d.dice2, d.dice3)
            print('Total number of tosses =', count)
            break

main()
