from abc import ABC, abstractmethod
from typing import List, Mapping

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Bird:
    def fly(self):
        print("A bird is flying in the sky")

class Car:
    def run(self):
        print("The car is running on the road")

class Ship:
    def drive(self):
        print("The captain is driving a ship on the ocean")


class FlyCommand(Command):
    def __init__(self, bird) -> None:
        self.bird = bird

    def execute(self):
        self.bird.fly()


class RunCommand(Command):
    def __init__(self, car) -> None:
        self.car = car

    def execute(self):
        self.car.run()

class DriveCommand(Command):
    def __init__(self, ship) -> None:
        self.ship = ship

    def execute(self):
        self.ship.drive()

class Invoker:
    def __init__(self) -> None:
        self.commands:List[Command] = []

    def addCommand(self, command:Command):
        self.commands.append(command)

    def executeAll(self):
        [c.execute() for c in self.commands]
    

def main():
    bird = Bird()
    car = Car()
    ship = Ship()

    invoker = Invoker()
    invoker.addCommand(FlyCommand(bird))
    invoker.addCommand(RunCommand(car))
    invoker.addCommand(DriveCommand(ship))

    invoker.executeAll()


if __name__ == "__main__":
    main()