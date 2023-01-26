import csv
import sys


class DB:
    def load_data(self):
        bt = []
        holiday = []
        balloon_twister_schedule = []
        with open("balloon_twisters.dat") as f:
            for line in f:
            #    self.signup(line.strip())
                bt.append(line.strip())

        with open("holidays.dat") as f:
            for line in f:
                holiday.append(line.strip())
            #    holiday = Holiday(line.strip())
            #    self.add_holiday(holiday)

        with open("schedule.csv") as f:
            reader = csv.reader(f)

            for row in reader:
                balloon_twister_schedule.append(row)
            #    (customer, balloon_twister, holiday) = row

            #    balloon_twister = next(bt for bt in self.balloon_twisters if bt.name == balloon_twister)
            #    holiday = next(h for h in self.holidays if h.name == holiday)

            #    booking = Booking(customer, balloon_twister, holiday)
            #    balloon_twister.add_holiday(holiday)
            #    holiday.add_booking(booking)
        return (bt, holiday, balloon_twister_schedule)  
    def save_data(self):
        with open("schedule.csv", "w") as f:
            writer = csv.writer(f)

            for holiday in self.holidays:
                for booking in holiday.bookings:
                   writer.writerow([booking.customer, booking.balloon_twister.name, booking.holiday.name])