# For simplicity, we are not defining getter and setter functions. The reader can
# assume that all class attributes are private and accessed through their respective
# public getter methods and modified only through their public methods function.


class Customer:
    def __init__(self, name, address, email, phone, status):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        self.__status = status
        
        

    def make_transaction(self, transaction):
        transaction.make_transation(customer = self)

    def get_billing_address(self): 
        None
    
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address
    def get_mail(self):
        return self.__email
    def get_phone(self):
        return self.__phone
    def get_status(self):
        return self.__status
    
    
    def get_card(self):
        return self.__card
    
    def set_card(self, card_number,  card_expiry, card_pin):
        self.__card = Card(number=card_number , customer_name = self.__name, expiry=card_expiry , pin = card_pin )
    
    def get_account_number(self):
        return self.__account.__account_number
    
    def get_account(self):
        return self.__account
    
    def set_account(self ,account_number,total_balance):
        self.__account = Account( account_number = account_number , total_balance=total_balance)

     
        
    


class Card:
    def __init__(self, number, customer_name, expiry, pin):
        self.__card_number = number
        self.__customer_name = customer_name
        self.__card_expiry = expiry
        self.__pin = pin

    def get_billing_address(self):
        None

    def get_card_number(self):
        return self.__card_number
    def get_card_pin(self):
        return self.__pin
    def get_card_expiry(self):
        return self.__card_expiry
    def change_card_pin(self , new_pin):
        self.__pin = new_pin


class Account:
    def __init__(self, account_number,total_balance):
        self.__account_number = account_number
        self.__total_balance = total_balance
        self.__available_balance = 0.0
        
        

    def get_available_balance(self):
        return self.__available_balance
    
    def get_total_balance(self):
        return self.__total_balance
    
    def get_account_number(self):
        return self.__account_number
    
    def update_balance(self , amount):
        
        self.__total_balance = self.__total_balance + amount



class SavingAccount(Account):
    def __init__(self, withdraw_limit):
        self.__withdraw_limit = withdraw_limit


class CheckingAccount(Account):
    def __init__(self, debit_card_number):
        self.__debit_card_number = debit_card_number

