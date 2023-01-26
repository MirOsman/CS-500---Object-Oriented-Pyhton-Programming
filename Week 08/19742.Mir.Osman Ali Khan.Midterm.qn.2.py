import random
from typing import Counter

class Dice:	
	def __init__(self):
		self.__dice_list = [1]*4
		for i in range(4):
			self.__dice_list[i] = random.randint(2,6)
			
	def reset(self):
		for i in range(4):
			self.__dice_list[i] = random.randint(2,6)
			
	def toss(self):
		for i in range(4):
			self.__dice_list[i] = random.randint(1,6)
		return sum(self.__dice_list)
	
	def die1(self):
		return self.__die1
	
	def die2(self):
		return self.__die2
	
	def die3(self):
		return self.__die3
	
	def die4(self):
		return self.__die4

def reset(self):
		for i in range(4):
			self.__dice_list[i] = random.randint(2,6)
			
def toss(self):
		for i in range(4):
			self.__dice_list[i] = random.randint(1,6)
		return sum(self.__dice_list)
	
def main():
	d = Dice()
	Ok = 'Yes'
	
	simulations = []
	while Ok == 'Yes':
		print("Starting simulation")
		times = 0
		while d.toss() != 24:
			times += 1
		
		simulations.append(times)
		
		print("simulation ended")
		ui = input("Would you like to rerun? (Yes/No)")
	
	for pos, val in enumerate(simulations):
		print("simulation",pos,": tossed",val, "times")
    
if __name__ == "__main__":
    main()    
