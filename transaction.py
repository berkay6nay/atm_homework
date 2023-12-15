from abc import ABC, abstractmethod
from bank import ATM , Bank
from constants import TransactionType

class Transaction(ABC):
    ##next_id = Bank.get_highest_transaction_id() ## en yüksek id'yi bul ve next_id değişkenini ona göre ata.
    
    def __init__(self,  creation_date, status , id = 0):
        self.__transaction_id = id
        ##Transaction.next_id += 1
        self.__creation_date = creation_date
        self.__status = status
        

    def get_transaction_id(self):
        return self.__transaction_id
    def get_creation_time(self):
        return self.__creation_date
    def get_status(self):
        return self.__status
    

    @abstractmethod
    def make_transation(self , customer = None):
        None

    

class BalanceInquiry(Transaction):
    def __init__(self, account_id):
        ##super().__init__(creation_date = creation_date , status = status)
        self.__account_id = account_id
        

        Bank.transaction_list.append(self)

    def get_account_id(self):
        return self.__account_id
    
    """def save_transaction_to_txt(self):
        with open("transaction.txt", "a") as file:
            file.write(f"{self.get_transaction_id()},{self.get_creation_time()}, {self.get_status()}\n")"""
    
    def make_transation(self , customer = None):
        account_in_question = customer.get_account()
        print("Hesabinizdaki mevcut bakiye: " + str(account_in_question.get_available_balance()) + "$")
        ##self.save_transaction_to_txt()

    

        

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
    def __init__(self, destination_account_number , amount):
        self.__amount = amount
        self.__destination_account_number = destination_account_number
        Bank.transaction_list.append(self)
    def get_destination_account(self):
        return self.__destination_account_number
    
    def make_transation(self, customer):
        ##Önce destination account_number'a göre account inquery'si yap. ## Bu tasarımda query iki kere gerçekleşiyor,düzeltilmesi lazım.
        for customer_query in Bank.customer_list:

            if customer_query.get_account().get_account_number() == self.__destination_account_number:
                customer_receiving = customer_query
            
      
        sending_customer_account = customer.get_account()
        customer_receiving_account = customer_receiving.get_account()
        print(str(self.__amount) + "$" + " gönderiliyor")
        sending_customer_account.update_balance(-(self.__amount))
        customer_receiving_account.update_balance(self.__amount)
        print(str(self.__amount) + "$" + " gönderildi")


