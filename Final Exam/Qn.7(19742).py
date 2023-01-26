from state_machine import (State, Event, acts_as_state_machine,
after, before, InvalidStateTransition)
from abc import ABC, abstractmethod
import random

@acts_as_state_machine
class RentingMachine:
    # define 5 states
    apply = State(initial=True)
    check = State()
    rent = State()
    confirmed = State()
    canceled = State()

    # define transitions
    apply_info = Event(from_states=apply, to_state=check)
    check_info = Event(from_states=check,to_state=rent)
    disapprove = Event(from_states=apply,to_state=check)
    approve = Event(from_states=apply,to_state=check)
    rent_info = Event(from_states=approve,to_state=check)
        
    def __init__(self, name):
        self.name = name
             
    @before('apply')
    def apply_info(self):
        print(f'{self.name} said Thanks for the application!')
    
    @before('check')
    def check_info(self):
        print(f'{self.name}'  'entered into waiting state')
        
    @before('rent')
    def check_info(self):
        print(f'{self.name} Renting you an apartment .')
        
    @after('approve')
    def approve_info(self):
        print(f'{self.name}' ' said Congratulations, you are approved.')

    @after('disapprove')
    def disapprove_info(self):
        print(f'{self.name}' ' Sorry, you were not approved.')
        
        
class OrderSystem:
    def __init__(self):
        self.process = RentingMachine('Alex')
        
    def submit_application(self):
        try:
            self.process.apply_info()
        except  InvalidStateTransition as err:
            print(f'Error: {self.process.name} cannot get application in {self.process.current_state}  state')
        
    def check_application(self):
        try:
            self.process.check_info()
            self.verify_Order()
        except  InvalidStateTransition as err:
            print(f'Error: {self.process.name} cannot check application in gotApplication {self.process.current_state} state')
            
    def verify_Order(self):
        approved = random.randint(0,9) > 3
        try:
            if approved is True:
                self.process.approve()
            else:
                self.process.disapprove()
        except  InvalidStateTransition as err:
            print(f'Error: {self.process.name} cannot rent you apartment in apartmentRented {self.process.current_state} state')
            
    def rent_apartment(self):
        try:
                self.process.rent_info()
        except  InvalidStateTransition as err:
            print(f'Error: {self.process.name} cannot rent apartment in renting {self.process.current_state} state')
            
    
            
            
def showMenu():
        print("COMMAND MENU")
        print("apply - Submit Application")
        print("check - Check Application")
        print("rent - Rent Apartment")
        print("exit - Exit program")
        print() 
        
        
        
def main():
    mall = OrderSystem() 
    showMenu()
    
    while True:        
        command = input("Command: ")
        if command == "apply":
            mall.submit_application()
        elif command == "check":
            mall.verify_Order()
        elif command == "rent":
            mall.rent_apartment()
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")
            
    
if __name__ == "__main__":
    main()