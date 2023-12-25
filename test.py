import unittest
from bank import ATM
from bank import Bank
from customer import Customer

from transaction import   CashDeposit, Withdraw, Transfer, ChangePin


class TestATM(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bank = Bank(name = "Banka1" , bank_code="1")
        cls.atm = ATM(id = 1 , location="YTÜ")
        cls.customer = Customer(name="TestUser", address="Istanbul", email="test@.com", phone="55555555", status="ACTIVE")
        cls.customer.set_card(card_number="51513"  , card_expiry="2005" , card_pin= 1234)
        cls.customer.set_account(account_number= 1111 , total_balance= 0)

        cls.customer2 = Customer(name="TestUser2", address="Istanbul", email="test2@.com", phone="55555555", status="ACTIVE")
        cls.customer2.set_card(card_number="54564"  , card_expiry="2005" , card_pin= 1234)
        cls.customer2.set_account(account_number= 2222 , total_balance= 0)


    def test_auth_user(self): ## USER AUTH TESTİ , OK VERDİ
        pin = self.customer.get_card().get_card_pin()
        result = self.atm.authenticate_user(pin , self.customer)
        self.assertTrue(result)

        result = self.atm.authenticate_user(pin = 9999 , customer = self.customer)
        self.assertFalse(result)


    def test_cash_deposit(self):

        deposit_amount = 100
        self.atm.make_transaction(transaction = CashDeposit(amount=deposit_amount, account_id=self.customer.get_account().get_account_number(), creation_date="2023-01-01") , customer=self.customer)
        update_balance = self.customer.get_account().get_total_balance()
        self.assertEqual(update_balance , deposit_amount)

    def test_withdraw(self):
        amount = 50
        future_balance = self.customer.get_account().get_total_balance() - 50
        
        self.atm.make_transaction(transaction=Withdraw(amount=amount , creation_date="2025-8-5" , account_id=self.customer.get_account().get_account_number()), customer = self.customer)
        new_balance = self.customer.get_account().get_total_balance()
        self.assertEqual(new_balance , future_balance)

    def test_change_pin(self):
        
        new_pin = 1235

        self.atm.make_transaction(transaction=ChangePin(account_id= self.customer.get_account().get_account_number(), creation_date="250-7-8", new_pin=1235),customer=self.customer)
        self.assertEqual(new_pin , self.customer.get_card().get_card_pin())

    

class TestTransfer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bank = Bank(name = "Banka1" , bank_code="1")
        cls.atm = ATM(id = 1 , location="YTÜ")
        cls.customer = Customer(name="TestUser", address="Istanbul", email="test@.com", phone="55555555", status="ACTIVE")
        cls.customer.set_card(card_number="51513"  , card_expiry="2005" , card_pin= 1234)
        cls.customer.set_account(account_number= 1111 , total_balance= 50)

        cls.customer2 = Customer(name="TestUser2", address="Istanbul", email="test2@.com", phone="55555555", status="ACTIVE")
        cls.customer2.set_card(card_number="54564"  , card_expiry="2005" , card_pin= 1234)
        cls.customer2.set_account(account_number= 2222 , total_balance= 0)
        cls.bank.customer_list.append(cls.customer2)
        cls.bank.customer_list.append(cls.customer) ##Customer , card ve account objeleri simültane oluşturulmadığı için , 
                                                    # customer oluşurken doğrudan bankanın listesine append edemiyoruz,bu da bir sorundur


    def test_transfer(self):
       
        amount = 25
        self.atm.make_transaction(transaction=Transfer(destination_account_number=2222 , amount=amount,sending_account_number=self.customer.get_account().get_account_number() , creation_date="2052-8-7") , customer=self.customer)
        self.assertEqual(25 , self.customer.get_account().get_total_balance())
        self.assertEqual(25 , self.customer2.get_account().get_total_balance())


class TestQuery(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.bank = Bank(name = "Banka1" , bank_code="1")
        cls.atm = ATM(id = 1 , location="YTÜ")
        cls.customer = Customer(name="TestUser", address="Istanbul", email="test@.com", phone="55555555", status="ACTIVE")
        cls.customer.set_card(card_number="51513"  , card_expiry="2005" , card_pin= 1234)
        cls.customer.set_account(account_number= 1111 , total_balance= 50)

        cls.customer2 = Customer(name="TestUser2", address="Istanbul", email="test2@.com", phone="55555555", status="ACTIVE")
        cls.customer2.set_card(card_number="54564"  , card_expiry="2005" , card_pin= 1234)
        cls.customer2.set_account(account_number= 2222 , total_balance= 0)

        cls.customer3 = Customer(name="TestUser3", address="Istanbul", email="test3@.com", phone="5515545025", status="ACTIVE")
        cls.customer3.set_card(card_number="3526"  , card_expiry="2005" , card_pin= 1234)
        cls.customer3.set_account(account_number= 3333 , total_balance= 0)

        cls.bank.add_customer(customer=cls.customer3)
        cls.bank.add_customer(customer=cls.customer2)
        cls.bank.add_customer(customer=cls.customer)
        

    def test_query_card_number(self):
        
        customer = self.bank.customer_list[0]
        query_customer = self.atm.find_customer_by_card_number(card_number = customer.get_card().get_card_number())
        self.assertIs(customer , query_customer)

    def test_query_account_number(self):
        customer = self.bank.customer_list[0]
        query_customer = self.atm.find_customer_by_account_number(customer.get_account().get_account_number())
        self.assertIs(customer , query_customer)

if __name__ == "__main__":
    unittest.main()