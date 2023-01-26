# This is a simple dice rolling simulator.

# The Dice class represents a set of four dice.
from random import random


class Dice:
    # The constructor initializes the dice with random values.
    # Each die has a value of 1, 2, 3, 4, 5, or 6.
    def __init__(self):
        self.die1 = 2
        self.die2 = 4
        self.die3 = 6
        self.die4 = 8


    # The get_die1() method returns the value of the first die.
    def get_die1(self):
        return self.die1

    # The get_die2() method returns the value of the second die.
    def get_die2(self):
        return self.die2

    # The get_die3() method returns the value of the third die.
    def get_die3(self):
        return self.die3

    # The get_die4() method returns the value of the fourth die.
    def get_die4(self):
        return self.die4

    # The toss() method simulates tossing the dice.
    # Each die's value will be assigned a random integer between 1 and 6.
    def toss(self):
        self.die1 = random.randint(1, 6)
        self.die2 = random.randint(1, 6)
        self.die3 = random.randint(1, 6)
        self.die4 = random.randint(1, 6)

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