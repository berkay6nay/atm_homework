from abc import ABC
from constants import TransactionType

class Bank:
  atm_list = []
  customer_list = []
  transaction_list = []
  account_list = []
  
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

  def authenticate_user(self , pin , customer):
    if pin == customer.get_card().get_card_pin():  ## Auth prototipi
      return True
    else: False
    
  def get_screen(self):
    return self.__screen
    

  def make_transaction(self, customer, transaction):
    None
  
  
  def find_customer_by_card_number(self, card_number): ##Girilen card number için card'ın customer'ını döndür , yoksa None döndür
    for customer in Bank.customer_list:
      if customer.get_card().get_card_number() == card_number:
        return customer
      
    return None
  
  
  def find_customer_by_account_number(self , account_id):
    for customer in Bank.customer_list:
      if customer.get_account().get_account_number() == account_id:
        return customer
      
    return None



class CashDispenser:
  def __init__(self):
    self.__total_five_dollar_bills = 0
    self.__total_twenty_dollar_bills = 0

  def dispense_cash(self, amount):
    None

  def can_dispense_cash(self):
    if self.__total_five_dollar_bills > 0 or self.__total_twenty_dollar_bills > 0 : ##Dispenser'da para var ise True döndür
      return True


class Keypad:
  def get_input(self):
    None


class Screen:
  def show_message(self, message):
    print(message)

  def get_input(self):
    transaction_input = int(input("Lütfen yapmak istediğiniz işlemi seçiniz")) ##Kullanıcı tarafından Transaction Type'ın girilmesi
    return TransactionType(transaction_input)
    


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

