from state_machine import (State, Event, acts_as_state_machine,
after, before, InvalidStateTransition)
from abc import ABC, abstractmethod
import random

@acts_as_state_machine
class CheckoutProcess:
    # define 5 states
    checkout = State(initial=True)
    payment = State()
    pending = State()
    confirmed = State()
    canceled = State()

    # define transitions
    payment_info = Event(from_states=checkout, to_state=payment)
    submit_order = Event(from_states=payment,to_state=pending)
    disapprove = Event(from_states=pending,to_state=checkout)
    approve = Event(from_states=pending,to_state=confirmed)
    cancel = Event(from_states=confirmed,to_state=canceled)
    back = Event(from_states=(confirmed, canceled), to_state=checkout)
        
    def __init__(self, name):
        self.name = name
             
    @before('payment_info')
    def payment_info_info(self):
        print(f'{self.name} said please enter your credit card information!')
    
    @after('submit_order')
    def submit_order_info(self):
        print(f'{self.name} received the order request and we are verifying your order.')
        print(f'{self.name} said sorry your order was not approved, please remove some items from your shopping cart.')
        
    @after('approve')
    def approve_info(self):
        print(f'{self.name}' 'said Congratulations, your order is now complete.')

    @after('disapprove')
    def disapprove_info(self):
        print(f'{self.name}' 'said sorry your order was not approved, please remove some items in your shopping cart.')
        
        
class OrderSystem:
    def __init__(self):
        self.process = CheckoutProcess('Alex')
        
    def begin_checkout(self):
        try:
            self.process.payment_info()
        except  InvalidStateTransition as err:
            print(f'Error: {self.process.name} cannot enter payment info in {self.process.current_state} state')
        
    def submit_order(self):
        try:
            self.process.submit_order()
            self.verify_Order
        except  InvalidStateTransition as err:
            print(f'Error: {self.process.name} cannot submit order in {self.process.current_state} state')
            
    def verify_Order(self):
        approved = random.randint(0,9) > 3
        try:
            if approved is True:
                self.process.approve()
            else:
                self.process.disapprove()
        except  InvalidStateTransition as err:
            print(f'Error: {self.process.name} cannot submit order in {self.process.current_state} state')
            
            
def showMenu():
        print("COMMAND MENU")
        print("begin - Begin Checkout")
        print("submit - Submit your order")
        print("cancel - Cancel my order")
        print("return - Back to Checkout")
        print("exit - Exit program")
        print() 
        
        
        
def main():
    mall = OrderSystem() 
    showMenu()
    
    while True:        
        command = input("Command: ")
        if command == "begin":
            mall.begin_checkout()
        elif command == "submit":
            mall.submit_order()
        elif command == "cancel":
            mall.cancel()
        elif command == "return":
            mall.back()
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Not a valid command. Please try again.\n")
            
    
if __name__ == "__main__":
    main()
    