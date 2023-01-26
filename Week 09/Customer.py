class Customer:
    def __init__(self, accountNo:int, firstName: str, lastName: str, accountBalance: float) -> None:
        self.__accountNo = accountNo
        self.__firstName = firstName
        self.__lastName = lastName
        self.__accountBalance =  accountBalance

    @property
    def accountNo(self) -> int:
        return self.__accountNo
    
    @accountNo.setter
    def accountNo(self, accountNo : int):
        self.__accountNo = accountNo

    @property
    def firstName(self) -> str:
        return self.__firstName

    @property
    def lastName(self) -> str:
        return self.__lastName

    @property
    def accountBalance(self) -> float:
        return self.__accountBalance
    
    @accountBalance.setter
    def balance(self, accountBalance : float):
        self.__accountBalance = accountBalance


    def getCustomer(self) -> list[str]:
        cust = []
        cust.append(self.__accountNo)
        cust.append(self.__firstName)
        cust.append(self.__lastName)
        cust.append(self.__accountBalance)
        return cust
    
    def __repr__(self) -> str:
        return str(self)
     
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Customer):
            return self.__accountNo == __o.__accountNo
        return False


    def __str__(self) -> str:
        return "Customer : \n" + "Account No :" + str(self.__accountNo) + "\n" + "First Name :" + self.__firstName + "\n" + "Last Name :" + self.__lastName + "\n" + "Account Balance :" + str(self.__accountBalance) + "\n"
