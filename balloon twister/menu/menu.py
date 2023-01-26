import csv
import sys


class BalloonTwister:
    def __init__(self, name: str):
        self.name = name
        self.schedule = []

    def book_holiday(self, holiday):
        self.schedule.append(holiday)

    def cancel_holiday(self, holiday):
        self.schedule.remove(holiday)

    def availability(self, holiday):  
        return holiday in self.schedule

    def __str__(self):
        return self.name + ":" + str(self.schedule)

    def __repr__(self):
        return self.__str__()


class Holiday:
    def __init__(self, name : str):
        self.name = name
        self.bookings = []

    def add_booking(self, booking):
        self.bookings.append(booking)

    def cancel_booking(self, booking):
        self.bookings.remove(booking)

    def availabilty(self, balloon_twister):
        return balloon_twister not in [booking.balloon_twister for booking in self.bookings]

    def __str__(self):
        return self.name + ":" + str([booking.baloon_twister.name for booking in self.bookings])

    def __repr__(self):
        return self.__str__()

class Booking:
    def _init_(self, customer : str, balloon_twister, holiday):
        self.customer = customer
        self.balloon_twister = balloon_twister
        self.holiday = holiday

    def _str_(self):
        return self.customer + ": " + self.balloon_twister.name + " on " + self.holiday

    def _repr_(self):
        return self._str_()        


class Scheduler:  
    def __init__(self):
        self.balloon_twisters = []
        self.holidays = []
        self.waiting_list = []
            
    def add_balloon_twister(self, balloon_twister):
        self.balloon_twisters.append(balloon_twister)

    def cancel_balloon_twister(self, balloon_twister):
        self.balloon_twisters.remove(balloon_twister)

    def add_holiday(self, holiday):
        self.holidays.append(holiday)

    def cancel_holiday(self, holiday):
        self.holidays.remove(holiday)

    def add_to_waiting_list(self, customer, holiday):
        self.waiting_list.append(customer)
        self.waiting_list.append(holiday)

    def schedule(self, customer, holiday):
        for balloon_twister in self.balloon_twisters:
            if balloon_twister.availability(holiday):
                booking = Booking(customer, balloon_twister, holiday )

            self.add_to_waiting_list(customer, holiday)

            print("Included to the waiting list:\n" + customer + "on" + holiday.name)
            
    def cancel(self, customer, holiday):
        for booking in holiday.bookings:
            if booking.customer == customer:
               holiday.remove_booking(booking)
               booking.balloon_twister.remove_holiday(holiday)
               print("Cancelled booking: " + str(booking))

            if self.waiting_list:
                (new_customer, new_holiday) = self.waiting_list.pop(0)
                self.schedule(new_customer, new_holiday)
                return

        print("Could not find booking for " + customer +  "  on  "  + holiday.name)

    def status(self, name):
        for balloon_twister in self.balloon_twisters:
            if balloon_twister.name == name:
               print(balloon_twister)
               return

        for holiday in self.holidays:
            if holiday.name == name:
               print(holiday)
               return

        print("Could not find " + name)

    def signup(self, name):
       balloon_twister = BalloonTwister(name)
       self.add_balloon_twister(balloon_twister)
       print("Added " + name + " to balloon twisters")

    def dropout(self, name):
        for balloon_twister in self.balloon_twisters:
            if balloon_twister.name == name:
               self.remove_balloon_twister(balloon_twister)

               for holiday in balloon_twister.schedule:
                    for booking in holiday.bookings:
                       if booking.balloon_twister == balloon_twister:
                           holiday.remove_booking(booking)

                           if self.waiting_list:
                            (customer, new_holiday) = self.waiting_list.pop(0)
                            self.schedule(customer, new_holiday)
                            print("Rescheduled " + customer + " from waiting list")

               print("Removed " + name + " from balloon twisters")
               return

        print("Could not find " + name)

    def load_data(self):
        with open("balloon_twisters.dat") as f:
            for line in f:
               self.signup(line.strip())

        with open("holidays.dat") as f:
            for line in f:
               holiday = Holiday(line.strip())
               self.add_holiday(holiday)

        with open("schedule.csv") as f:
            reader = csv.reader(f)

            for row in reader:
               (customer, balloon_twister, holiday) = row

               balloon_twister = next(bt for bt in self.balloon_twisters if bt.name == balloon_twister)
               holiday = next(h for h in self.holidays if h.name == holiday)

               booking = Booking(customer, balloon_twister, holiday)
               balloon_twister.add_holiday(holiday)
               holiday.add_booking(booking)

    def save_data(self):
        with open("schedule.csv", "w") as f:
            writer = csv.writer(f)

            for holiday in self.holidays:
                for booking in holiday.bookings:
                   writer.writerow([booking.customer, booking.balloon_twister.name, booking.holiday.name])

    def run(self):
       self.load_data()

       while True:
        command = input("Enter command (schedule/cancel/status/signup/dropout/quit): ")

        if command == "quit":
            self.save_data()
            sys.exit(0)
        elif command == "schedule":
            customer = input("Customer name: ")
            holiday_name = input("Holiday name: ")

            try:
                holiday = next(h for h in self.holidays if h.name == holiday_name)
                self.schedule(customer, holiday)
            except StopIteration:
                print("Could not find holiday")
        elif command == "cancel":
            customer = input("Customer name: ")
            holiday_name = input("Holiday name: ")

            try:
                holiday = next(h for h in self.holidays if h.name == holiday_name)
                self.cancel(customer, holiday)
            except StopIteration:
                print("Could not find holiday")
        elif command == "status":
            name = input("Name: ")
            self.status(name)
        elif command == "signup":
            name = input("Balloon twister name: ")
            self.signup(name)
        elif command == "dropout":
            name = input("Balloon twister name: ")
            self.dropout(name)
        else:
            print("Invalid command")


def main():
    sch = Scheduler()

    try:
        sch.run()

    except KeyboardInterrupt:
        print()

        sch.save_data()

        sys.exit(0)
     

main()            

                                      




       

    
        


                             





