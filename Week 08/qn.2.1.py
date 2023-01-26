# This is a simple dice rolling simulator.

# The Dice class represents a set of four dice.
from random import random


class Dice:
    # The constructor initializes the dice with random values.
    # Each die has a value of 1, 2, 3, 4, 5, or 6.
    def __init__(self) -> None:
        self.__dicelist = []
        for i in range(4):
            self.__dicelist.append(random.randint(2,4))

    @property
    def die1(self) -> int:
        return self.__dicelist[0]

    @property
    def die2(self) -> int:
        return self.__dicelist[1]

    @property
    def die3(self) -> int:
        return self.__dicelist[2]
    
    @property
    def die4(self) -> int:
        return self.__dicelist[3]

    # The toss() method simulates tossing the dice.
    # Each dice's value will be assigned a random integer between 1 and 6.
    def toss(self) -> int:
        sum = 0
        for i in range(len(self.__dicelist)):
            self.__dicelist[i] = random.randint(1,6)
            sum += self.__dicelist[i]
        return sum

    # The reset() method resets the dice to their initial values.
    def reset(self):
        self.die1 = 2
        self.die2 = 4
        self.die3 = 6
        self.die4 = 8

# The main() function is the starting point of the program.
def main():
    # Create an instance of the Dice class.
    dice = Dice()

    # Keep track of the number of tosses.
    num_tosses = 0

    # Toss the dice until their sum is 24.
    while True:
        dice.toss()
        num_tosses += 1
        if dice.get_die1() + dice.get_die2() + dice.get_die3() + dice.get_die4() == 24:
            break

    # Print the results.
    print("It took {} tosses to get a total of 24.".format(num_tosses))

    # Reset the dice for the next simulation.
    dice.reset()

# Call the main() function to start the program.
if __name__ == "__main__":
    main()