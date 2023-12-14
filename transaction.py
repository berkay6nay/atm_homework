from abc import ABC, abstractmethod
from bank import ATM , Bank

class Transaction(ABC):
    def __init__(self, id, creation_date, status):
        self.__transaction_id = id
        self.__creation_time = creation_date
        self.__status = status
        
    @abstractmethod
    def make_transation(self , customer = None):
        None


class BalanceInquiry(Transaction):
    def __init__(self, account_id):
        self.__account_id = account_id
        Bank.transaction_list.append(self)

    def get_account_id(self):
        return self.__account_id
    
    def make_transation(self , customer = None):
        
        account_in_question = customer.get_account()

        print("Hesabinizdaki mevcut bakiye: " + str(account_in_question.get_available_balance()) + "$")

        

class Deposit(Transaction):

     def __init__(self, amount , account_id):
        self.__amount = amount
        self.__account_id = account_id
        Bank.transaction_list.append(self)

     def get_amount(self):
        return self.__amount
    
     def make_transation(self,customer = None):
         
         pass
         
         
class CheckDeposit(Deposit):
    def __init__(self, check_number, bank_code):
        self.__check_number = check_number
        self.__bank_code = bank_code
        Bank.transaction_list.append(self)

    def get_check_number(self):
        return self.__check_number


class CashDeposit(Deposit):
    def __init__(self , amount , account_id):
        self.__amount = amount
        self.__account_id = account_id
        Bank.transaction_list.append(self)
        self.__cash_deposit_limit = 100.000

    def make_transation(self, customer):
        
        account_in_question = customer.get_account()
        account_in_question.update_balance(amount = self.__amount)
        print(str(self.__amount) + "$" + " yatirdiniz \n")
        print("Mevcut bakiyeniz: " + str(account_in_question.get_available_balance()) + "$")




class Withdraw(Transaction):
    def __init__(self, amount , account_id):
        self.__amount = amount
        self.__account_id = account_id
        Bank.transaction_list.append(self)
    def get_amount(self):
        return self.__amount
    
    def make_transation(self , customer):

        account_in_question = customer.get_account()
        print("Cekmek istediginiz miktar : " + str(self.__amount) + "$ \n")
        print("Banknotlar veriliyor")
        account_in_question.update_balance(amount = -(self.__amount))
        print("Yeni bakiye : " + str(account_in_question.get_available_balance()) + "$")



class Transfer(Transaction):
    def __init__(self, destination_account_number):
        self.__destination_account_number = destination_account_number
        Bank.transaction_list.append(self)
    def get_destination_account(self):
        return self.__destination_account_number
