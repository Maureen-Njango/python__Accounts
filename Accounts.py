
class Account:
    def __init__(self, account_owner, account_number, account_balance, overdraft_limit, account_minimum_balance, pin):
        self.account_owner = account_owner
        self.account_number = account_number
        self.account_balance = account_balance
        self.overdraft_limit = overdraft_limit
        self.account_minimum_balance = account_minimum_balance
        self.pin = pin
        self.transaction = []
        self.frozen= false

    def deposit(self, amount, pin):
        if pin == self.pin:
            self.account_balance += amount
            self.transaction.append(amount)
        else:
            print("Wrong pin")

    def withdraw(self, amount, pin):
        if pin == self.pin:
            if self.account_balance - amount >= account_balance:
                self.account_balance -= amount
                self.transaction.append(amount)
            else:
                print("Insufficient funds")
        else:
            print("Wrong pin")

    def account_details(self, pin):
        if pin == self.pin:
            print(f"Account balance: {self.account_balance}")
            print(f"Account number: {self.account_number}")
        else:
            print("Wrong pin")

    def change_owner(self, new_owner):
        self.account_owner = new_owner

    def interest_calculation(self, rate):
        interest = self.account_balance * (rate / 100)
        self.account_balance += interest

    def statement(self, pin):
        if pin == self.pin:
            print(f"Your transaction history is: {self.transaction}")
        else:
            print("Wrong pin")

    def freeze_account(self, pin):
        if pin!= self.pin:
            return "Wrong PIN"
        self.freeze_account= True
            return "account frozen"
    def close_account(self, pin):
       if pin!= self.pin:
            return "Wrong PIN"

        return "Account closed"
   
    def set_minimum_balance(self, pin):
        if pin!= self.pin:
            return "Wrong PIN"
        self.account_minimum_balance = min_balance
        return f"Minimum balance set to {min_balance}"



    


    



    
     
    