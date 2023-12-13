from abc import ABC
from bank import ATM , Bank

class Transaction(ABC):
    def __init__(self, id, creation_date, status):
        self.__transaction_id = id
        self.__creation_time = creation_date
        self.__status = status
        

    def make_transation(self):
        None


class BalanceInquiry(Transaction):
    def __init__(self, account_id):
        self.__account_id = account_id
        Bank.transaction_list.append(self)

    def get_account_id(self):
        return self.__account_id
    
    def return_balance(self):
        
        for account in Bank.account_list:
            if self.__account_id == account.get_account_number():
                curr_account = account

        return curr_account.get_available_balance()

class Deposit(Transaction):

     def __init__(self, amount , account_id):
        self.__amount = amount
        self.__account_id = account_id

     def get_amount(self):
        return self.__amount
    
     def make_deposit(self):
         
         pass
         
         
class CheckDeposit(Deposit):
    def __init__(self, check_number, bank_code):
        self.__check_number = check_number
        self.__bank_code = bank_code

    def get_check_number(self):
        return self.__check_number


class CashDeposit(Deposit):
    def __init__(self , amount , account_id):
        self.__amount = amount
        self.__account_id = account_id
        
        self.__cash_deposit_limit = 100.000

    def make_deposit(self):
        
        for account in Bank.account_list:
            if self.__account_id == account.get_account_number():
                curr_account = account
        curr_account.update_balance(self.__amount)



class Withdraw(Transaction):
    def __init__(self, amount , account_id):
        self.__amount = amount
        self.__account_id = account_id

    def get_amount(self):
        return self.__amount
    
    def withdraw_cash(self):

        for account in Bank.account_list:
            if self.__account_id == account.get_account_number():
                curr_account = account
        curr_account.update_balance(-(self.__amount))



class Transfer(Transaction):
    def __init__(self, destination_account_number):
        self.__destination_account_number = destination_account_number

    def get_destination_account(self):
        return self.__destination_account_number