from customer import Customer , Card, SavingAccount , CheckingAccount
from constants import CustomerStatus
from bank import Bank, ATM ,Screen
from constants import TransactionType
from transaction import BalanceInquiry,CashDeposit,Withdraw

##DAtabase'in Kurulumu
bank = Bank(name = "YildizBank" , bank_code= "1" )
atm1 = ATM(id=1 , location="DummyAddress1")


customer1 = Customer(name="Name1" , email="dummy@gmail.com", phone="1111" , status= CustomerStatus.ACTIVE ,address="Istanbul" ,card_number="1111", card_expiry="31.07.2001" , card_pin=1234, account_number = 31)
customer2 = Customer(name="Name2" , email="dummy@hotmail.com", phone="0505" , status= CustomerStatus.ACTIVE ,address="Istanbul" ,card_number="2222", card_expiry="31.07.2001" , card_pin=1235, account_number = 32)
deposit = CashDeposit(amount = 100 , account_id = customer2.get_account().get_account_number())
deposit.make_deposit()


bank.add_atm(atm1)
bank.add_customer(customer=customer1)
bank.add_customer(customer=customer2)




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
            
            selected_transaction = int(input("Seçmek istediğiniz işlem için menüden uygun sayiyi giriniz")) #Transaction'ın seçilmesi
            if(selected_transaction == 1):
                balance = BalanceInquiry(customer_in_question.get_account().get_account_number()).return_balance()
                print("Mevcut bakiyeniz : " + str(balance))

            if(selected_transaction == 2):
                deposit_amount = int(input("Yatirmak istediğiniz parayi giriniz"))
                deposit = CashDeposit(amount = 100 , account_id = customer_in_question.get_account().get_account_number())
                deposit.make_deposit()
                balance = BalanceInquiry(customer_in_question.get_account().get_account_number()).return_balance()
                print(balance)
            
            if(selected_transaction == 3):
                pass

            if(selected_transaction == 4):
                print("1 - 20$ \n 2 - 40$ \n 3 - 100$ \n 4 - Custom Amount \n 5 - Cancel") ## Withdraw tipinin seçilmesi
                withdraw_type = int(input("Lütfen menüden istediğiniz işlemi seçiniz"))
                curr_balance = BalanceInquiry(customer_in_question.get_account().get_account_number()).return_balance()
                flag = 0
                if(withdraw_type == 1 and curr_balance >= 20 ):
                     ##balance'ın sorgulanması
                    withdraw = Withdraw(amount = 20 , account_id= customer_in_question.get_account().get_account_number())
                    withdraw.withdraw_cash()
                    print("20$ veriliyor")
                    print("Kalan paraniz" + str(BalanceInquiry(customer_in_question.get_account().get_account_number()).return_balance()) + "$")
                    flag += 1 

                elif(withdraw_type == 2 and curr_balance >= 40):
                    withdraw = Withdraw(amount = 40 , account_id= customer_in_question.get_account().get_account_number())
                    withdraw.withdraw_cash()
                    print("40$ veriliyor")
                    print("Kalan paraniz" + str(BalanceInquiry(customer_in_question.get_account().get_account_number()).return_balance()) + "$")
                    flag += 1 
                elif(withdraw_type == 3 and curr_balance >= 100):
                    withdraw = Withdraw(amount = 100 , account_id= customer_in_question.get_account().get_account_number())
                    withdraw.withdraw_cash()
                    print("100$ veriliyor")
                    print("Kalan paraniz" + str(BalanceInquiry(customer_in_question.get_account().get_account_number()).return_balance()) + "$")
                    flag += 1 

                elif(withdraw_type == 4):
                    custom_miktar = int(input("Cekmek istediginiz miktari giriniz"))
                    if(custom_miktar <= curr_balance):
                        withdraw = Withdraw(amount = custom_miktar , account_id= customer_in_question.get_account().get_account_number())
                        withdraw.withdraw_cash()
                        print(str(custom_miktar) +"$ " + " veriliyor")
                        print("Kalan paraniz" + str(BalanceInquiry(customer_in_question.get_account().get_account_number()).return_balance()) + "$")

                    else:print("Yetersiz Bakiye")

                

                elif(withdraw_type == 5):
                    print("Kart veriliyor")
                    break
                     
                if(flag == 0):
                    print("YetersizBakiye")        

                    

                    


                
                

        else: 
            print("Yanliş Şifre Girdiniz")

        
    
    