from customer import Customer , Card, SavingAccount , CheckingAccount
from constants import CustomerStatus
from bank import Bank, ATM ,Screen
from constants import TransactionType, TransactionStatus
from transaction import BalanceInquiry,CashDeposit,Withdraw,Transfer

from datetime import datetime

##DAtabase'in Kurulumu
"""bank = Bank(name = "YildizBank" , bank_code= "1" )
bank.read_customer_from_text()
bank.read_atm_from_text()
atm1 = Bank.atm_list[0]"""

bank = Bank(name = "YildizBank" , bank_code = "1")
atm1 = ATM(id = 1 , location = "Istanbul")






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
                
                customer_in_question.make_transaction(transaction = BalanceInquiry( account_id=customer_in_question.get_account().get_account_number() , creation_date= datetime.today().date()), atm = atm1)

            if(selected_transaction == 2): ## Para Yatırma
                amount = int(input("Yatirmak istediginiz miktari giriniz \n"))
                print("Banknotlar kontrol ediliyor... \n")
                customer_in_question.make_transaction(transaction = CashDeposit(amount=amount, account_id=customer_in_question.get_account().get_account_number(), creation_date= datetime.today().date()) , atm = atm1)
            
            if(selected_transaction == 3):
                pass

            

            if(selected_transaction == 4): ## Para Çekme
                while True: ## Yetersiz bakiye durumunda kullanıcının para çekme menüsüne dönmesi için while döngüsü tanımlandı.
                    print("Çekmek istediginiz miktari seciniz \n")
                    print("1 - 20$ \n 2 - 40$ \n 3 - 100$ \n 4 - Custom Amount \n 5 - Cancel") ## Withdraw tipinin seçilmesi
                    withdraw_type = int(input("Lütfen menüden istediğiniz işlemi seçiniz"))
                    curr_balance = customer_in_question.get_account().get_available_balance()
                    flag = 0 ##If statementların kısaltılması için flag değişkeni tanımlanmıştır
                    if(withdraw_type == 1 and curr_balance >= 20 ): ## Custom withdraw - 20$
                        customer_in_question.make_transaction(transaction = Withdraw(amount=20, account_id=customer_in_question.get_account().get_account_number() ,creation_date= datetime.today().date()) , atm = atm1)
                        flag += 1 
                        break

                    elif(withdraw_type == 2 and curr_balance >= 40): ## Custom withdraw - 40$
                        customer_in_question.make_transaction(transaction = Withdraw(amount=40, account_id=customer_in_question.get_account().get_account_number() ,creation_date= datetime.today().date()) , atm = atm1)
                        flag += 1 
                        break
                    elif(withdraw_type == 3 and curr_balance >= 100): ## Custom withdraw - 100$
                        customer_in_question.make_transaction(transaction = Withdraw(amount=100, account_id=customer_in_question.get_account().get_account_number() ,creation_date= datetime.today().date()) , atm = atm1)
                        flag += 1 
                        break

                    elif(withdraw_type == 4): ## Kullanıcı tarafından girilen amount
                        custom_miktar = int(input("Cekmek istediginiz miktari giriniz"))
                        if(custom_miktar <= curr_balance):
                            customer_in_question.make_transaction(transaction = Withdraw(amount=custom_miktar, account_id=customer_in_question.get_account().get_account_number() ,creation_date= datetime.today().date()) , atm = atm1)
                            flag += 1 
                            break

                    elif(withdraw_type == 5):
                        print("Kart veriliyor")
                        break
                            
                    if(flag == 0):
                        print("Yetersiz Bakiye \n")
                        print("Yeni bir miktar seçin \n")
                        continue   

            if(selected_transaction == 5): ##Para Transferi
                while True: ## Yetersiz bakiye için tanımlanan while döngüsü.
                    
                    amount_to_be_sent = int(input("Lütfen göndermek istediğiniz miktari girin"))

                    if(amount_to_be_sent > customer_in_question.get_account().get_available_balance()):
                        choice = int(input("Yetersiz bakiye.\n 1-Karti ver \n 2- Başka bir miktar gir"))
                        if(choice == 1): break
                        if(choice == 2): continue
                    
                    else:

                        while True: ## yanlış account number için while döngüsü tanımlanması.

                            destination_account_number = int(input("Lütfen hedef hesap numarisini girin")) ## Doğru amount girildikten sonra destination account sorgulanabilir.
                            if atm1.find_customer_by_account_number(destination_account_number):
                                customer_in_question.make_transaction(transaction = Transfer(sending_account_number=customer_in_question.get_account().get_account_number() , 
                                                                                             destination_account_number=destination_account_number, amount=amount_to_be_sent,creation_date= datetime.today().date()), 
                                                                                             atm = atm1)
                                break
                            else:
                                choice = int(input("Girdiginiz hesap bulunamadi. \n 1- Karti Ver \n 2 - Yeni hesap numarasi gir")) 
                                if choice == 1: break
                                if choice == 2: continue
                    break
                  
                   

        else: 
            print("Yanliş Şifre Girdiniz")
            print("1 - Tekrar Dene \n 2- Karti Ver")
            choice = int(input("Lütfen yapmak istediğiniz işlemi seçin"))
            if choice == 1:
                pass
            else: 
                pass

    else:print("Bankamizin müsterisi oldugunuza emin misiniz?")
        
    
    
