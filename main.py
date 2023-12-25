
from bank import Bank, ATM 
from constants import TransactionType
from transaction import BalanceInquiry,CashDeposit,Withdraw,Transfer, ChangePin

from datetime import datetime

##DAtabase'in Kurulumu


bank = Bank(name = "YildizBank" , bank_code = "1")
atm1 = ATM(id = 1 , location = "Istanbul")
screen1 = atm1.get_screen()
keypad1 = atm1.get_keypad()
printer1 = atm1.get_printer()






###Kullanıcı Arayüzü Prototipi

while True:
    screen1.show_message("\n")
    print("Yildiz Teknik Üniversitesi ATM \n")

    card_no = input(print("Lütfen Kartinizi Yerleştiriniz(Kart Numaranizi Giriniz) \n"))
    
    card_pin = int(input(print("Kartinizin şifresini giriniz")))

    customer_in_question = atm1.find_customer_by_card_number(card_number= card_no)

    if customer_in_question: ##Sorgulanan customer db'de var ise
        
        if atm1.authenticate_user(pin= card_pin , customer= customer_in_question): ##  auth işlemi gerçekleşirse transaction kısmına geçilebilir
            
            
            screen1.show_message("Dogrulama Basarili \n")
            
            for transaction_type in TransactionType:
                screen1.show_message(f"{transaction_type.value}. {transaction_type.name.replace('_', ' ')}") ##menünün konsola yazdırılması

            
            
            selected_transaction = keypad1.get_input("Lütfen yapmak istediğiniz işlemi seçiniz") #Transaction'ın seçilmesi


            if(selected_transaction == 1): ## Bakiye Inquery
                
                atm1.make_transaction(transaction = BalanceInquiry( account_id=customer_in_question.get_account().get_account_number() , creation_date= datetime.today().date()),
                                       customer=customer_in_question)
                screen1.show_message("Kart veriliyor... \n")
                screen1.show_message("Lütfen kartinizi alin")

            if(selected_transaction == 2): ## Para Yatırma
                amount = int(input("Yatirmak istediginiz miktari giriniz \n"))
                screen1.show_message("Banknotlar kontrol ediliyor... \n")
                atm1.make_transaction(transaction = CashDeposit(amount=amount, account_id=customer_in_question.get_account().get_account_number(), creation_date= datetime.today().date()) , customer=customer_in_question)
                screen1.show_message("Kart veriliyor... \n")
                screen1.show_message("Lütfen kartinizi alin")
            
            
            if(selected_transaction == 3):
                pass

            

            if(selected_transaction == 4): ## Para Çekme
                while True: ## Yetersiz bakiye durumunda kullanıcının para çekme menüsüne dönmesi için while döngüsü tanımlandı.
                    screen1.show_message("Çekmek istediginiz miktari seciniz \n")
                    screen1.show_message("1 - 20$ \n 2 - 40$ \n 3 - 100$ \n 4 - Custom Amount \n 5 - Cancel") ## Withdraw tipinin seçilmesi
                    withdraw_type = keypad1.get_input("Lütfen menüden istediğiniz işlemi seçiniz")
                    curr_balance = customer_in_question.get_account().get_total_balance()
                    flag = 0 ##If statementların kısaltılması için flag değişkeni tanımlanmıştır
                    if(withdraw_type == 1 and curr_balance >= 20 ): ## Custom withdraw - 20$
                        atm1.make_transaction(transaction = Withdraw(amount=20, account_id=customer_in_question.get_account().get_account_number() ,creation_date= datetime.today().date()) ,
                                               customer=customer_in_question)
                        flag += 1
                        screen1.show_message("Kart veriliyor... \n")
                        screen1.show_message("Lütfen kartinizi alin") 
                        break

                    elif(withdraw_type == 2 and curr_balance >= 40): ## Custom withdraw - 40$
                        atm1.make_transaction(transaction = Withdraw(amount=40, account_id=customer_in_question.get_account().get_account_number() ,creation_date= datetime.today().date()) , 
                                              customer=customer_in_question)
                        flag += 1
                        screen1.show_message("Kart veriliyor... \n")
                        screen1.show_message("Lütfen kartinizi alin") 
                        break
                    elif(withdraw_type == 3 and curr_balance >= 100): ## Custom withdraw - 100$
                        atm1.make_transaction(transaction = Withdraw(amount=100, account_id=customer_in_question.get_account().get_account_number() ,creation_date= datetime.today().date()) ,
                                               customer=customer_in_question)
                        flag += 1 
                        screen1.show_message("Kart veriliyor... \n")
                        screen1.show_message("Lütfen kartinizi alin")
                        break

                    elif(withdraw_type == 4): ## Kullanıcı tarafından girilen amount
                        custom_miktar = int(input("Cekmek istediginiz miktari giriniz"))
                        if(custom_miktar <= curr_balance):
                            atm1.make_transaction(transaction = Withdraw(amount=custom_miktar, account_id=customer_in_question.get_account().get_account_number() ,creation_date= datetime.today().date()) ,
                                                   customer=customer_in_question)
                            flag += 1 
                            screen1.show_message("Kart veriliyor... \n")
                            screen1.show_message("Lütfen kartinizi alin")
                            break

                    elif(withdraw_type == 5):
                        screen1.show_message("Kart veriliyor... \n")
                        screen1.show_message("Lütfen kartinizi alin")
                        break
                            
                    if(flag == 0):
                        screen1.show_message("Yetersiz Bakiye \n")
                        screen1.show_message("Yeni bir miktar seçin \n")
                        continue   

            if(selected_transaction == 5): ##Para Transferi
                while True: ## Yetersiz bakiye için tanımlanan while döngüsü.
                    
                    amount_to_be_sent = keypad1.get_input("Lütfen göndermek istediğiniz miktari girin")

                    if(amount_to_be_sent > customer_in_question.get_account().get_total_balance()):
                        choice = keypad1.get_input("Yetersiz bakiye.\n 1-Karti ver \n 2- Başka bir miktar gir")
                        if(choice == 1):
                            screen1.show_message("Kartiniz veriliyor... \n")
                            screen1.show_message("Lütfen kartinizi alin") 
                            break
                        if(choice == 2): continue
                    
                    else:

                        while True: ## yanlış account number için while döngüsü tanımlanması.

                            destination_account_number = keypad1.get_input("Hedef hesap numarisini girin") ## Doğru amount girildikten sonra destination account sorgulanabilir.
                            if atm1.find_customer_by_account_number(destination_account_number):
                                atm1.make_transaction(transaction = Transfer(sending_account_number=customer_in_question.get_account().get_account_number() , 
                                                                                             destination_account_number=destination_account_number, amount=amount_to_be_sent,creation_date= datetime.today().date()), 
                                                                                             customer=customer_in_question)
                                screen1.show_message("Kartiniz veriliyor... \n")
                                screen1.show_message("Lütfen kartinizi alin") 
                                break

                            else:
                                choice = keypad1.get_input("Girdiginiz hesap bulunamadi. \n 1- Karti Ver \n 2 - Yeni hesap numarasi gir")
                                if choice == 1:
                                    screen1.show_message("Kartiniz veriliyor... \n")
                                    screen1.show_message("Lütfen kartinizi alin") 
                                    break
                                if choice == 2:continue

                                    
                    break

            if selected_transaction == 6:
                new_pin = keypad1.get_input("Yeni 4 haneli yeni bir şifre girin")
                atm1.make_transaction(transaction = ChangePin(new_pin= new_pin,account_id=customer_in_question.get_account().get_account_number() , creation_date = datetime.today().date()) , customer= customer_in_question)
                screen1.show_message("Kartiniz veriliyor... \n")
                screen1.show_message("Lütfen kartinizi alin.")  
                   

        else: 
            screen1.show_message("Yanliş Şifre Girdiniz")
            screen1.show_message("1 - Tekrar Dene \n 2- Karti Ver")
            choice = keypad1.get_input("Lütfen yapmak istediğiniz işlemi seçin")
            if choice == 1:
                pass
            else: 
                pass

    else:print("Bankamizin müsterisi oldugunuza emin misiniz?")
        
    
    
