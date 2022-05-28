class Account:

    def __init__(self,name,balance,id,pin):
        self.name= name
        self.balance = balance
        self.id = id
        self.pin =pin

    def deposit(self,amount):
        self.amount = amount
        self.balance += amount
        return  f"Hello {self.name} your balance is{self.balance}" 

    def  withdraw(self,amount):
        self.amount = amount
        self.balance -= amount
        return f"Hello {self.name} your balance is{self.balance}"   
    
        
        