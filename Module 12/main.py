from all_user import*
from Bank import*

DBC = Bank("DBC", "Danmondi 25/B")

#--------- adding User-----------
santo = User("Santo", "santo@gmail.com", "Mugda, Thana", "Saving")
DBC.add_user(santo)

safin = User("Safin", "safin@gmail.com", "kodda, BBaria", "current")
DBC.add_user(safin)


admin = Admin("kamal", "kamal.info@gmail.com", "Dhaka cantonmant")
DBC.add_admin(admin)


current_user = None
current_user_type = None

while True:
    if current_user == None:
        print("1 : Create account")
        print("2 : Login account")

        x = int(input())

        if x == 1:
            print("1 : Create as User")
            # print("2 : Creat as Admin")
            

            y = int(input())

            if y == 1:
                name = input("Enter Full Name: ")
                address = input("Enter your Address: ")
                email = input("Enter your Email: ")
                acc_type = input("Enter account type Saving / Current: ")
                
                user = User(name, email, address, acc_type)

                DBC.add_user(user)

            # elif y == 2:
            #     name = input("Enter Full Name: ")
            #     address = input("Enter your Address: ")
            #     email = input("Enter your Email: ")

            #     admin = Admin(name, email, address)
            #     DBC.add_admin(admin)

        if x == 2:
            print(" 1 : Login as User")
            print(" 2 : Login as Admin")

            y = int(input())

            if y == 1:
                name = input("Enter you name: ")
                acc_number = int(input("Enter you account number: "))

                if DBC.users[acc_number].name == name:
                    current_user = DBC.users[acc_number]
                    current_user_type = "U"
                else:
                    print("Info Didn't Match")
            
            elif y == 2:
                name = input("Enter the name: ")
                email = input("Enter the Email: ")

                if DBC.admins[0].name == name and DBC.admins[0].email == email:
                    current_user = DBC.admins[0]
                    current_user_type = "A"
                else:
                    print("Info Didn't Match")
    
    elif current_user != None and current_user_type == "U":
        print(f"__Welcome {current_user.name}__\n")

        print(" 1 : Chek balance ")
        print(" 2 : Add money ")
        print(" 3 : Send money ")
        print(" 4 : Take loan ")
        print(" 5 : Chash Out ")
        print(" 6 : See Transaction History")
        print(" 7 : Logout")

        x = int(input("\n____Opption: "))

        if x == 1:
            current_user.chek_balance()
            print()
        elif x == 2:
            amount = int(input("Enter The ammount : "))
            current_user.add_money(amount)
            print()
        elif x == 3:
            acc_number = int(input("Enter the Account number"))
            amount = int(input("Enter The ammount : "))
            current_user.send_money(amount, current_user.bank.users[acc_number])
            print()
        
        elif x == 4:
            amount = int(input("Enter The ammount : "))
            current_user.take_loan(amount)
            print()
        elif x == 5:
            amount = int(input("Enter The ammount : "))
            current_user.cash_out(amount)
            print()
        
        elif x == 6:
            current_user.show_transaction_history()
            print()
        elif x == 7:
            current_user = None
            current_user_type = None
    
    elif current_user != None and current_user_type == "A":
        print(f"---Welcome {current_user.name}---")
        print(" 1 : Create Account ")
        print(" 2 : Delet Accont ")
        print(" 3 : See All User ")
        print(" 4 : Chek Total Balance ")
        print(" 5 : Chek Total Loan ")
        print(" 6 : Set Loan Option ")
        print(" 7 : Logout")

        x = int(input("----Option: "))

        if x == 1:
            name = input("Enter Full Name: ")
            address = input("Enter your Address: ")
            email = input("Enter your Email: ")
            acc_type = input("Enter account type Saving / Current: ")
            user = User(name, email, address, acc_type)
            current_user.creat_user_account(user)
        
        elif x == 2:
            acc_number = int(input("Enter the account number: "))
            user = current_user.bank.users[acc_number]
            current_user.delet_user(user)
        
        elif x == 3:
            current_user.chek_all_user()
        elif x == 4:
            current_user.chek_balance()
        
        elif x == 5:
            current_user.chek_total_loan()
        elif x == 6:
            option = input("Enter ON / OFF : ")
            current_user.set_loan_option(option)
        
        elif x == 7:
            current_user = None
            current_user_type = None

        




                    



            
            

            



        
