
import os
import pandas pd

def load_data():
    if os.path.exists('BalloonTwisters.dat'):
        with open('BalloonTwisters.dat','r') as f:
            balloon_twister = f.read().splitlines()
    
    if os.path.exists("Holidays.dat"):
        with open("Holidays.dat") as f:
            holidays = f.read().splitlines()
    
    if os.path.exists('Schedule.csv'):
        schedule = pd.read_csv('Schedule.csv').values.tolist()
    
    if os.path.exists('waiting.csv'):
        waiting_list = pd.read_csv('waiting.csv').values.tolist()


    return balloon_twister,holidays,schedule,waiting_list


class Schedule:
    def __init__(self,names,holiday,schedule,waiting_list) -> None:
        self.names = names
        self.holidays = holiday
        self.waiting_list = waiting_list

        self.scheduled_info = {i:None for i in names}
        self.holidays_info = {i:None for i in holiday}

        for balloon,customer, hday in schedule:
            if balloon not in self.scheduled_info or not self.scheduled_info[balloon]:
                self.scheduled_info[balloon] = [(hday, customer)]
            else:
                self.scheduled_info[balloon].append((hday, customer))
            if hday not in self.holidays_info or not self.holidays_info[hday]:
                self.holidays_info[hday] = [(customer, balloon)]
            else:
                self.holidays_info[hday].append((customer, balloon))

    def schedule(self,customer,holiday):
        
        for name in self.names:
            is_available = 0
            for booking in self.scheduled_info:
                if name in booking:
                    is_available += 1

            if not is_available:
                if holiday not in self.holidays_info or not self.holidays_info[holiday]:
                    self.holidays_info[holiday] = [(customer,name)]
                else:
                    self.holidays_info[holiday].append((customer,name))
                print(f'Customer has booked {name} on holiday {holiday}')
                return
                 
            else:
                self.waiting_list.append((holiday, customer))
                print(f'Customer {customer} has been added to waiting list on holiday {holiday}')
                return


    
    def cancel(self, customer: str, holiday: str):
        schedules = {i:None for i in self.names}
        holidays = {i:None for i in self.holidays}

        for h_day in self.holidays_info:
            if h_day == holiday:
                for schedule in self.holidays_info[holiday]:
                    if schedule[0] != customer:
                        if not schedules[schedule[1]]:
                            schedules[schedule[1]] = [(holiday, schedule[0])]
                        else:
                            schedules[schedule[1]].append((holiday, schedule[0]))

                        if not holidays[holiday]:
                            holidays[holiday] = [(schedule[0], schedule[1])]
                        else:
                            holidays[holiday].append((schedule[0], schedule[1]))  
            else:
                holidays[h_day] = self.holidays_info[h_day]

        self.holidays_info,self.schedule_info = holidays,schedules

        for i, (hday, custmer) in enumerate(self.waiting_list):
            if hday == holiday:
                self.schedule(custmer, hday)
                del self.waiting_list[i]
                return

                
    def status(self, c_or_h: str):
        if c_or_h in self.scheduled_info:
            print(f"Balloon Twister Bookings: {c_or_h}\n")
            for hday,custmer in self.scheduled_info[c_or_h]:
                print(f"Customer : {custmer} Booked for holiday: {hday}")
        elif c_or_h in self.holidays_info:
            print(f"Holiday Schedule : {c_or_h}\n")
            for custmer,balloon in self.holidays_info[c_or_h]:
                print(f"customer: {custmer} has booked Balloon Twister: {balloon}")


    def signup(self, name: str):
        if not name and name not in self.names:
            self.names.append(name)
        print(f"New Ballon Twister : {name} has signed up")

    def dropout(self, name: str):
        self.names.remove(name)
        if name in self.scheduled_info:
            booking = self.scheduled_info.pop(name)
            for holiday, customer in booking:
                print(f"Customer {customer} booking for holiday {holiday} has been added to waiting list")
                self.waiting_list.insert(0, (holiday, customer))

        hdays = {i:None for i in self.holidays}
        for holiday in self.holidays_info:
            if not self.holidays_info[holiday]:
                for balloon,custmer in self.holidays_info[holiday]:
                    if balloon != name:
                        if not hdays[holiday]:
                            hdays[holiday] = [(custmer, balloon)]
                        else:
                            hdays[holiday].append((custmer, balloon))

        self.holidays_info = hdays
        print(f"Ballon Twister {name} has been dropped out")       

    def save_data(self):
        with open("BalloonTwisters.dat",'w') as f:
            for names in self.names:
                f.write(names + '\n')
        
        with open("Holidays.dat",'w') as f:
            for names in self.holidays_info:
                f.write(names + '\n')

        new_dict = []
        for hday in self.holidays_info:
            if self.holidays_info[hday]:
                for customer,balloon in self.holidays_info[hday]:
                    new_dict.append({'Balloon Twister':balloon,'Customer':customer,'Holiday':hday})


        # pd.DataFrame.from_dict(new_dict,orient='records').to_csv("Schedule.csv",index=False)
        pd.DataFrame(new_dict).to_csv("Schedule.csv",index=False)

        pd.DataFrame(self.waiting_list,columns=["Holiday","Customer"]).to_csv('waiting.csv',index=False)


    def quit(self):
        self.save_data(self)
    



def main():
    schedule_obj = Schedule(*load_data())

    while True:
        print("\n    MENU\n")
        print("1. SCHEDULE")
        print("2. CANCEL")
        print("3. STATUS")
        print("4. QUIT")
        print("5. SIGNUP")
        print("6. DROPOUT")
        option = int(input("Enter choice: "))

        if option == 1:
            customer = input("Enter Customer Name: ")
            holiday = input("Enter Holiday: ")
            schedule_obj.schedule(customer, holiday)
        elif option == 2:
            customer = input("Enter Customer Name: ")
            holiday = input("Enter Holiday: ")
            schedule_obj.cancel(customer, holiday)
        elif option == 3:
            name = input("Enter balloon Twister name or Holiday: ")
            schedule_obj.status(name)
        elif option == 4:
            schedule_obj.save_data()
            break
        elif option == 5:
            name = input("Enter balloon Twister name: ")
            schedule_obj.signup(name)
        elif option == 6:
            name = input("Enter balloon Twister name: ")
            schedule_obj.dropout(name)


if __name__ == "__main__":
    main()