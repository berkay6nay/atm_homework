from customer import Customer , Card, SavingAccount , CheckingAccount
from constants import CustomerStatus
from bank import Bank, ATM ,Screen
from constants import TransactionType

##DAtabase'in Kurulumu
bank = Bank(name = "YildizBank" , bank_code= "1" )
atm1 = ATM(id=1 , location="DummyAddress1")


customer1 = Customer(name="Name1" , email="dummy@gmail.com", phone="1111" , status= CustomerStatus.ACTIVE ,address="Istanbul" ,card_number="1111", card_expiry="31.07.2001" , card_pin=1234)

bank.add_atm(atm1)
bank.add_customer(customer=customer1)


###Kullanıcı Arayüzü Prototipi

while True:
    print("Çiftlik Bank Yildiz Teknik Üniversitesi ATM'sine Hoşgeldiniz \n")

    card_no = input(print("Lütfen Kartinizi Yerleştiriniz(Kart Numaranizi Giriniz) \n"))
    
    card_pin = int(input(print("Kartinizin şifresini giriniz")))

    customer_in_question = atm1.find_customer_by_card_number(card_number= card_no)

    if customer_in_question: ##Sorgulanan customer db'de var ise
        if atm1.authenticate_user(pin= card_pin , customer= customer_in_question): ## Sorgulanan customer var ise ve auth işlemi gerçekleşirse transaction kısmına geçilebilir
            screen = atm1.get_screen()
            screen.show_message("Dogrulama Basarili \n")
            screen.show_message("Lütfen Yapmak Istediginiz Islemi Seciniz \n")
            for transaction_type in TransactionType:
                screen.show_message(f"{transaction_type.value}. {transaction_type.name.replace('_', ' ')}") ##menünün konsola yazdırılması

        else: 
            print("Yanliş Şifre Girdiniz")
    
    
