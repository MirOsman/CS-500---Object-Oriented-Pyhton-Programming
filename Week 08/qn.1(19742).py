import random
from typing import Counter

class Dice:
    def __init__(self) -> None:
        self.__dicelist = []
        for i in range(4):
            self.__dicelist.append(random.randint(2,6))


    @property
    def die1(self) -> int:
        return self.__die1

    @property
    def die2(self) -> int:
        return self.__

    @property
    def die3(self) -> int:
        return self.__die3
    
    @property
    def die4(self) -> int:
        return self.__dielist[3]

    def toss(self) -> int:
        sum = 0
        for i in range(len(self.__dicelist)):
            self.__dicelist[i] = random.randint(1,6)
            sum += self.__dicelist[i]
        return sum

    def reset(self):
	    for i in range(4):
             self.__dice_list[i] = random.randint(2,6)
	
def main():
	dice = Dice()
	ok = 'Yes'
	
	simulations = []
	while ok == 'Yes':
		print("Starting simulation")
		times = 0
		while dice.toss() != 24:
			times += 1
		
		simulations.append(times)
		
		print("simulation ended")
		ui = input("Would you like to rerun? (Yes/No)")
	
	for pos, val in enumerate(simulations):
		print("simulation",pos,": tossed",val, "times")
		
	
main()