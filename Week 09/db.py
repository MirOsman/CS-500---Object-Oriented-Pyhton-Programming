from Customer import Customer
import csv
class CustomerRepository:
    def __init__(self):
        self.__filename = "customers.csv"
    
    def getCustomers(self)->list[Customer]:
        customers:list[Customer] = []
        with open(self.__filename, newline ="") as file:
            reader = csv.reader(file)
            for row in reader :
                customer: Customer = Customer(
                    int(row[0]),
                    row[1], 
                    row[2],
                    float(row[3])
                )
                customers.append(customer)
        return customers 

    def saveCustomers(self, customers:list[Customer]):
        with open(self.__filename,'w', newline ="") as file:
            writer = csv.writer(file)
            for cust in customers:
                writer.writerow(cust.getCustomer())
                
def main():
    repo = CustomerRepository()
    customers = repo.getCustomers()
    for cust in customers:
        print(cust)
    
    customer = Customer(2678, "Peter", "Hammer", 20000.0)
    customers.append(customer)
    repo.saveCustomers(customers)

if __name__ == "__main__":
         main()
