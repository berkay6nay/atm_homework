from customer import Customer , Card, SavingAccount , CheckingAccount
from constants import CustomerStatus
from bank import Bank, ATM ,Screen
from constants import TransactionType
from transaction import BalanceInquiry,CashDeposit,Withdraw

##DAtabase'in Kurulumu
bank = Bank(name = "YildizBank" , bank_code= "1" )
atm1 = ATM(id=1 , location="DummyAddress1")


customer1 = Customer(name="Name1" , email="dummy@gmail.com", phone="1111" , status= CustomerStatus.ACTIVE ,address="Istanbul" ,card_number="1111", card_expiry="31.07.2001" , card_pin=1234, account_number = 31)



bank.add_atm(atm1)
bank.add_customer(customer=customer1)





###Kullanıcı Arayüzü Prototipi

while True:
    print("Çiftlik Bank Yildiz Teknik Üniversitesi ATM'sine Hoşgeldiniz \n")

    card_no = input(print("Lütfen Kartinizi Yerleştiriniz(Kart Numaranizi Giriniz) \n"))
    
    card_pin = int(input(print("Kartinizin şifresini giriniz")))

    customer_in_question = atm1.find_customer_by_card_number(card_number= card_no)

    if customer_in_question: ##Sorgulanan customer db'de var ise
        if atm1.authenticate_user(pin= card_pin , customer= customer_in_question): ##  auth işlemi gerçekleşirse transaction kısmına geçilebilir
            
            screen = atm1.get_screen()
            screen.show_message("Dogrulama Basarili \n")
            screen.show_message("Lütfen Yapmak Istediginiz Islemi Seciniz \n")
            for transaction_type in TransactionType:
                screen.show_message(f"{transaction_type.value}. {transaction_type.name.replace('_', ' ')}") ##menünün konsola yazdırılması
            
            selected_transaction = int(input("Seçmek istediğiniz işlem için menüden uygun sayiyi giriniz \n")) #Transaction'ın seçilmesi


            if(selected_transaction == 1): ## Bakiye Inquery
                
                customer_in_question.make_transaction(transaction = BalanceInquiry(account_id=customer_in_question.get_account().get_account_number()) , atm = atm1)

            if(selected_transaction == 2): ## Para Yatırma
                amount = int(input("Yatirmak istediginiz miktari giriniz \n"))
                print("Banknotlar kontrol ediliyor... \n")
                customer_in_question.make_transaction(transaction = CashDeposit(amount=amount, account_id=customer_in_question.get_account().get_account_number()) , atm = atm1)
            
            if(selected_transaction == 3):
                pass

            if(selected_transaction == 4): ## Para Çekme
                print("Çekmek istediginiz miktari seciniz \n")
                print("1 - 20$ \n 2 - 40$ \n 3 - 100$ \n 4 - Custom Amount \n 5 - Cancel") ## Withdraw tipinin seçilmesi
                withdraw_type = int(input("Lütfen menüden istediğiniz işlemi seçiniz"))
                curr_balance = customer_in_question.get_account().get_available_balance()
                flag = 0 ##If statementların kısaltılması için flag değişkeni tanımlanmıştır
                if(withdraw_type == 1 and curr_balance >= 20 ): ## Custom withdraw - 20$
                    customer_in_question.make_transaction(transaction = Withdraw(amount=20, account_id=customer_in_question.get_account().get_account_number()) , atm = atm1)
                    flag += 1 

                elif(withdraw_type == 2 and curr_balance >= 40): ## Custom withdraw - 40$
                    customer_in_question.make_transaction(transaction = Withdraw(amount=40, account_id=customer_in_question.get_account().get_account_number()) , atm = atm1)
                    flag += 1 
                   
                elif(withdraw_type == 3 and curr_balance >= 100): ## Custom withdraw - 100$
                    customer_in_question.make_transaction(transaction = Withdraw(amount=100, account_id=customer_in_question.get_account().get_account_number()) , atm = atm1)
                    flag += 1 

                elif(withdraw_type == 4): ## Kullanıcı tarafından girilen amount
                    custom_miktar = int(input("Cekmek istediginiz miktari giriniz"))
                    if(custom_miktar <= curr_balance):
                        customer_in_question.make_transaction(transaction = Withdraw(amount=custom_miktar, account_id=customer_in_question.get_account().get_account_number()) , atm = atm1)
                        flag += 1 

                elif(withdraw_type == 5):
                    print("Kart veriliyor")
                    break
                     
                if(flag == 0):
                    print("Yetersiz Bakiye")        

        else: 
            print("Yanliş Şifre Girdiniz")

    else:print("Bankamizin müsterisi oldugunuza emin misiniz?")
        
    
    
