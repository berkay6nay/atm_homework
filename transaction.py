from abc import ABC
from bank import Bank 
from constants import TransactionType , TransactionStatus

class Transaction(ABC):
    next_id = 0
    
    def __init__(self,  creation_date, status = None):
        self.__transaction_id = Transaction.next_id
        Transaction.next_id += 1
        self.__creation_date = creation_date
        self.__status = TransactionStatus.SUCCESS
        

    def get_transaction_id(self):
        return self.__transaction_id
    def get_creation_time(self):
        return self.__creation_date
    def get_status(self):
        return self.__status
    

    
    def make_transation(self , customer = None):
        None

    
    def save_transaction_to_text(self):
        None

    def write_customer_list_to_text(self):
        with open("customer.txt" , "w") as file:
            """ name , address, email, phone, status ,card_number,  card_expiry, card_pin, account_number , total_balance = str(data[0]) ,str(data[1]) ,
              str(data[2]) , str(data[3]), data[4], str(data[5]) , str(data[6]) , int(data[7]) , int(data[8]) , int(data[9])"""
            for customer in Bank.customer_list:
                name = customer.get_name()
                address = customer.get_address()
                email = customer.get_mail()
                phone = customer.get_phone()
                status = customer.get_status()
                card_number = customer.get_card().get_card_number()
                card_expiry = customer.get_card().get_card_expiry()
                card_pin = customer.get_card().get_card_pin()
                account_number = customer.get_account().get_account_number()
                total_balance = customer.get_account().get_total_balance()

                file.write(f"{name},{address},{email},{phone},{status},{card_number},{card_expiry},{card_pin},{account_number},{total_balance} \n")

    

class BalanceInquiry(Transaction):
    def __init__(self, account_id , creation_date):
        super().__init__(creation_date = creation_date )
        self.__account_id = account_id
        self.save_transaction_to_text()

    def get_account_id(self):
        return self.__account_id
    
    
    def make_transation(self , customer = None):
        account_in_question = customer.get_account()
        print("Hesabinizdaki mevcut bakiye: " + str(account_in_question.get_total_balance()) + "$")
        

    def save_transaction_to_text(self):
        
        with open("transaction.txt" , "a") as file:
            id = super().get_transaction_id()
            date = super().get_creation_time()
            account = self.__account_id
            type = str(TransactionType.BALANCE_INQUIRY)
            file.write(f"{id} ,{type},  {date} , {account} \n")


    

        

class Deposit(Transaction):

     def __init__(self, amount , account_id ,creation_date ):
        super().__init__(creation_date=creation_date)
        self.__amount = amount
        self.__account_id = account_id

     def get_amount(self):
        return self.__amount
    
     def make_transation(self,customer = None):
         pass
     
             
         
         
class CheckDeposit(Deposit):
    def __init__(self, check_number, bank_code):
        self.__check_number = check_number
        self.__bank_code = bank_code
        

    def get_check_number(self):
        return self.__check_number


class CashDeposit(Deposit):
    def __init__(self , amount , account_id , creation_date):
        super().__init__(creation_date = creation_date , amount= amount , account_id= account_id)
        self.__amount = amount
        self.__account_id = account_id 
        self.__cash_deposit_limit = 100.000
        self.save_transaction_to_text()
    def save_transaction_to_text(self):
        with open("transaction.txt" , "a") as file:
            id = super().get_transaction_id()
            date = super().get_creation_time()
            account = self.__account_id
            amount = self.__amount
            type = str(TransactionType.DEPOSIT_CASH)
            file.write(f"{id} , {type}, {date} , {account} ,  {amount} \n")
        
    def make_transation(self, customer):
        
        account_in_question = customer.get_account()
        account_in_question.update_balance(amount = self.__amount)
        print(str(self.__amount) + "$" + " yatirdiniz \n")
        print("Mevcut bakiyeniz: " + str(account_in_question.get_total_balance()) + "$")
        super().write_customer_list_to_text()




class Withdraw(Transaction):
    def __init__(self, amount , creation_date , account_id):
        super().__init__(creation_date = creation_date)
        self.__amount = amount
        self.__account_id = account_id
        self.save_transaction_to_text()
       
    def get_amount(self):
        return self.__amount
    
    def make_transation(self , customer):

        account_in_question = customer.get_account()
        print("Cekmek istediginiz miktar : " + str(self.__amount) + "$ \n")
        print("Banknotlar veriliyor")
        account_in_question.update_balance(amount = -(self.__amount))
        print("Yeni bakiye : " + str(account_in_question.get_total_balance()) + "$")
        super().write_customer_list_to_text()

    def save_transaction_to_text(self):
        with open("transaction.txt" , "a") as file:
            id = super().get_transaction_id()
            date = self.get_creation_time()
            account = self.__account_id
            amount = self.__amount
            type = str(TransactionType.WITHDRAW)
            file.write(f"{id} ,{type} , {date} , {account} ,  {amount} \n")



class Transfer(Transaction):
    def __init__(self, destination_account_number , amount, sending_account_number , creation_date):
        super().__init__(creation_date = creation_date)
        self.__amount = amount
        self.__destination_account_number = destination_account_number
        self.__sending_account_number = sending_account_number
        self.save_transaction_to_text()

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
        super().write_customer_list_to_text()

    def save_transaction_to_text(self):
        with open("transaction.txt" , "a") as file:
            id = super().get_transaction_id()
            date = super().get_creation_time()
            amount = self.__amount
            type = str(TransactionType.TRANSFER)
            account = self.__sending_account_number
            receiver = self.__destination_account_number
            file.write(f"{id} ,{type} , {date} , {account} ,{receiver} ,  {amount}   \n")



class ChangePin(Transaction):
    def __init__(self, account_id , creation_date , new_pin):
        super().__init__(creation_date = creation_date )
        self.__account_id = account_id
        self.save_transaction_to_text()
        self.__new_pin = new_pin
        self.save_transaction_to_text()


    def make_transation(self, customer):
        card = customer.get_card()
        card.change_card_pin(new_pin = self.__new_pin)
        print("Kart şifresi değiştirildi")
        super().write_customer_list_to_text()


    def save_transaction_to_text(self):
        with open("transaction.txt" , "a") as file:
            id = super().get_transaction_id()
            date = super().get_creation_time()
            type = str(TransactionType.CHANGE_PIN)
            account = self.__account_id
            file.write(f"{id} ,{type} , {date}, {account}\n")
        


