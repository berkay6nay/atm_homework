from abc import ABC
from constants import TransactionType , CustomerStatus
from customer import Customer


class Bank:
  atm_list = []
  customer_list = []
  
  
  def __init__(self, name, bank_code):
    self.__name = name
    self.__bank_code = bank_code
    

  def get_bank_code(self):
    return self.__bank_code

  def add_atm(self, atm):
    Bank.atm_list.append(atm) ## ATM'yi bankanın atm listesine ekle

  def add_customer(self , customer):
    Bank.customer_list.append(customer) ## Customer'ı bankanın customer listesine ekle

  def add_transaction(self , transaction): ## Transaction'ı bankanın transaction listesine ekle
    Bank.transaction_list.append(transaction)

  def add_account(self , account):
    Bank.account_list.append(account)


  


  


class ATM:
  def __init__(self, id, location):
    self.__atm_id = id
    self.__location = location

    self.__cash_dispenser = CashDispenser()
    self.__keypad = Keypad()
    self.__screen = Screen()
    self.__printer = Printer()
    self.__check_deposit = CheckDeposit()
    self.__cash_deposit = CashDeposit
    self.add_atm_to_text()
    self.read_customer_from_text()

  def add_atm_to_text(self):
    try:
      with open("atm.txt" , "a") as file:
        id = self.__atm_id
        location = self.__location
        file.write(f"{id} , {location}")
    except FileNotFoundError:
      print("File not found")

  def authenticate_user(self , pin , customer):
    if pin == customer.get_card().get_card_pin():  ## Auth prototipi
      return True
    else: False
    
  def get_screen(self):
    return self.__screen
  def get_keypad(self):
    return self.__keypad
  def get_printer(self):
    return self.__printer
    

  def make_transaction(self, customer, transaction):
    customer.make_transaction(transaction)
  
  
  def find_customer_by_card_number(self, card_number): ##Girilen card number için card'ın customer'ını döndür , yoksa None döndür
    for customer in Bank.customer_list:
      if customer.get_card().get_card_number() == card_number:
        return customer
      
    return None
  
  
  def find_customer_by_account_number(self , account_id): ##Account number ile customer sorgusu
    for customer in Bank.customer_list:
      if customer.get_account().get_account_number() == account_id:
        return customer
      
    return None
  
  def read_customer_from_text(self):
        try:
            with open("customer.txt", "r") as file:
                for line in file:
                    data = line.strip().split(',')
                    name , address, email, phone, status ,card_number,  card_expiry, card_pin, account_number , total_balance = str(data[0]) ,str(data[1]) , str(data[2]) , str(data[3]), data[4], str(data[5]) , str(data[6]) , int(data[7]) , int(data[8]) , int(data[9])
                    customer = Customer(name,address,email,phone,status)
                    customer.set_account(account_number=account_number , total_balance = total_balance)
                    customer.set_card(card_number= card_number , card_expiry = card_expiry, card_pin=card_pin)
                    Bank.customer_list.append(customer)

        except FileNotFoundError:
            print("Customer file not found. Starting with an empty library.")

  
  





class CashDispenser:
  def __init__(self):
    self.__total_five_dollar_bills = 0
    self.__total_twenty_dollar_bills = 0

  def dispense_cash(self, amount):
    None

  def can_dispense_cash(self):
    pass


class Keypad:
  def get_input(self , message):
    users_input = int(input(message))
    return users_input


class Screen:
  def show_message(self, message):
    print(message)

  def get_input(self):
    pass


class Printer:
  def print_receipt(self, transaction):
    None


class CheckDeposit:
    def __init__(self):
        None


class CashDeposit:
    def __init__(self):
        None


class DepositSlot(ABC):
  def __init__(self):
    self.__total_amount = 0.0

  def get_total_amount(self):
    return self.__total_amount


class CheckDepositSlot(DepositSlot):
  def get_check_amount(self):
    None


class CashDepositSlot(DepositSlot):
  def receive_dollar_bill(self):
    None

