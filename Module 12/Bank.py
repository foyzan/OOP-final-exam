from other import History

class Bank:

    acc_number = 900000000

    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.balance = 10000000000
        self.history = []
        self.users = {}
        self.admins = []
        self.isbankrupt = False
        self.loan_ammount = 0

    def recive_money(self, ammount, remark, user):
        self.balance += ammount
        history = History(ammount, remark, user)
        self.history.append(history)

    def add_user(self, user):
        # print("cheak golab acc num",Bank.acc_number)
        Bank.acc_number += 10
        user.account_number = Bank.acc_number
    
        user.bank = self
        self.users[user.account_number] = user
        print(user.account_number)

    def add_admin(self, admin):
        admin.bank = self
        self.admins.append(admin)


    def give_money(self, ammount, remark, user):
        if self.isbankrupt == False and self.balance >= ammount:
            self.balance -= ammount
            history = History(ammount, remark, user)
            self.history.append(history)
        else:
            print("Bank is bankrupt")

    def remove_user(self, user_id):
        del self.users[user_id]    

    def show_all_user(self):
        for key, value in self.users.items():
            print(value)
    
    def show_balance(self):
        print(self.balance)
    
    def show_total_loan(self):
        print(self.loan_ammount)
    
    def loan_feature(self, x):
        if x == "ON":
            self.isbankrupt = False
        elif x == "OFF":
            self.isbankrupt = True


