class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name=name
        self.account_number=account_number
        self.balance=balance
    def display(self):
        print(self.name)
        print(self.account_number)
        print(self.balance)      
Bank_details=[]
while True:
   print("1. Add Customers")
   print("2. Display the customer details")
   print("3. depost the amount:")
   print("4. withdraw the amount:")
   print("5.search the account:")
   print("6. Exit")
   choice=int(input("enter what do you want:"))
   if choice==1:
      name=input("Enter the customer name:")
      account_number=int(input("Enter the account the number:"))
      balance=int(input("enter the initial balance:"))
      new_customer=BankAccount(name,account_number,balance)
      Bank_details.append(new_customer)
   elif choice==2:    
        for bank in Bank_details:
            bank.display()
   elif choice==3:
        found=False
        account_number=int(input("Enter the your account number:"))
        deposit_amount=int(input("Enter the amount :"))
        for bank in Bank_details:
           if bank.account_number==account_number:
              bank.balance+=deposit_amount
              print("Deposit sucessfully")
              print("current balance is ",bank.balance)
              found=True
        if found==False:
               print("account number not matched in our recoreds:")
   elif choice==4:
        found=False
        account_number=int(input("please enter your account number:"))
        withdraw_amount=int(input("enter the withdraw amount:"))
        for bank in Bank_details:
            if bank.account_number==account_number:
             if bank.balance>=withdraw_amount:
                bank.balance-=withdraw_amount
                print("amount withdraw sucesfully")
                print("cuurent balanmce",bank.balance)
                found=True
             else:
                print("insificent funds")
                found=True
        if found==False:
                print("account number not matched in our recoreds")
   elif choice==5:
       found=False
       search_account=int(input("Enter the account number:"))
       for bank in Bank_details:
           if bank.account_number==search_account:
              bank.display()
              print("we found the customer details")
              found=True
       if found==False:
          print("customer details nott found:")
   elif choice==6:
      break

