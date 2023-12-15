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
        
        

    def make_transaction(self, transaction , atm):
        atm.make_transaction(transaction = transaction , customer = self)

    def get_billing_address(self): 
        None
    
    def get_name(self):
        return self.__name
    
    
    def get_card(self):
        return self.__card
    
    def set_card(self, card_number,  card_expiry, card_pin):
        self.__card = Card(number=card_number , customer_name = self.__name, expiry=card_expiry , pin = card_pin )
    
    def get_account_number(self):
        return self.__account.__account_number
    
    def get_account(self):
        return self.__account
    
    def set_account(self ,account_number):
        self.__account = Account( account_number = account_number)

    def change_card_pin(self , new_pin):
        self.get_card().__pin = new_pin ## Pin güncellendiğinde customer listesindeki uygun customer'ın pin field'ı güncellenmelidir
        
    


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



class Account:
    def __init__(self, account_number):
        self.__account_number = account_number
        self.__total_balance = 0.0
        self.__available_balance = 0.0
        from bank import Bank
        Bank.account_list.append(self)

    def get_available_balance(self):
        return self.__available_balance
    
    def get_account_number(self):
        return self.__account_number
    
    def update_balance(self , amount):
        
        self.__available_balance = self.__available_balance + amount



class SavingAccount(Account):
    def __init__(self, withdraw_limit):
        self.__withdraw_limit = withdraw_limit


class CheckingAccount(Account):
    def __init__(self, debit_card_number):
        self.__debit_card_number = debit_card_number

