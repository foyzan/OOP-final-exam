class Personal_info:
    def __init__(self, name, email, address) -> None:
        self.name = name
        self.email = email
        self.address = address
class User(Personal_info):
    def __init__(self, name, email, address, type) -> None:
        super().__init__(name, email, address)
        self.account_type = type
        self.balance = 0
        self.account_number = None
        self.bank = None
        self.loan_time = 2
        self.loan_ammount = 0
        self.history = []
        self.transaction_history = []
    
    def add_money(self, ammount):
        self.balance +=ammount
        self.bank.recive_money(ammount, "from user", self)
        self.history.append((" Money added from owner", ammount))
    
    def cash_out(self, ammount):
        if self.bank.isbankrupt == False:
            if self.balance >= ammount:
                self.balance -= ammount
                self.bank.give_money(ammount, "To user", self)
                self.history.append(("Withdrown by owner", ammount))
            else:
                print("Withdrawal amount exceeded")
        else:
            print("Bank is Bankrupt")

    def take_loan(self, ammount):
        if self.bank.isbankrupt == False:
            if self.loan_time > 0 :
                self.balance += ammount
                self.loan_ammount += ammount
                self.loan_time -= 1
                self.bank.give_money(ammount, "For loan", self)
                self.bank.loan_ammount += ammount
                self.history.append(("loan from bank", ammount))
            else:
                print("You loan is limited")
        else:
            print("Bank is Bankrupt")
    
    def send_money(self, ammount, reciver):
        if self.bank.isbankrupt == False:
            if reciver.account_number in self.bank.users:
                self.balance -= ammount
                self.bank.users[reciver.account_number].balance += ammount
                self.bank.users[reciver.account_number].transaction_history.append((f"recive money from {self.name}", ammount)) 
                self.transaction_history.append((f"sending money to {reciver.name}", ammount))
            else:
                print("Account does not exist")
        else:
            print("Bank is Bankrupt")

    def chek_balance(self):
        print(self.balance)
    
    def show_transaction_history(self):
        print("--------- Transaction History---------\n")
        for history in self.transaction_history:
            print(history)
        
        print("--------------------------------------\n\n")
        print("----------- Other History -----------\n")
        for history in self.history:
            print(history)

    def __repr__(self) -> str:
        return f" {self.name} account number: {self.account_number} acc_type: {self.account_type} "
    

class Admin(Personal_info):
    def __init__(self, name, email, address) -> None:
        super().__init__(name, email, address)
        self.bank = None

    def chek_all_user(self):
        self.bank.show_all_user()
    
    def delet_user(self, user):
        self.bank.remove_user(user.account_number)

    def chek_balance(self):
        self.bank.show_balance()

    def chek_total_loan(self):
        self.bank.show_total_loan()

    def set_loan_option(self, y):
        self.bank.loan_feature(y)
    
    def creat_user_account(self, user):
        self.bank.add_user(user)

    