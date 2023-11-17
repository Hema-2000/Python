name="hemalatha"
password="12345"
user_name=input("enter the username")
user_password=input("enter the password")
amount=10000
statements=''' 
               1.credit
               2.debit
               3.mini_statement
               4.exit 
            '''
if user_name==name and user_password==password:
    while True:
        print(statements)
        choice=int(input("enter 1 to credit,enter 2 to debit, enter 3 to mini statement and enter 4 to exit"))
        if choice==1:
            credit_amount=int(input("enter amount to be credited"))
            print("balance amount in my account: ",amount+credit_amount)
        elif choice==2:
            debit_amount = int(input("enter amount to be debited"))
            print("balance amount in my account: ", amount - debit_amount)
        elif choice ==3:
            print("*****mini statement****")

        else:
            print("exit")
            break
    print("thank you! visit again!")
else:
    print("please enter valid user name and password")
