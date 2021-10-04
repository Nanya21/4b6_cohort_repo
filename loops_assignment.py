import random
from string import digits
import time

account=''.join([random.choice(digits) for n in range(10)])


user_data={'7816365970':'1095'}
setup=True

while setup:
    action=input('To create your account number press a \nFor login press b \n>>')

    if action== 'a':
        for c in range (10000):
            account=''.join([random.choice(digits) for n in range(10)])
            print(account)
            pin=(input('any four digit number'))
            re_pine= (input('pls confirm pin'))
            if (len(pin) > 4) or (len(pin)< 4):
                print('pin length should be 4')
                break
            if pin!=re_pine:
                print('incorrect pin')
            else:
                user_data[account]=pin
                print('Account number and pin successfully created')
                break

    elif action=='b':
        account= input('please enter your account number \n>>')
        pin= input('Enter your pin \n>>')
         
        time.sleep(2)
        if account in user_data.keys():
            actual_pin=user_data.get(account)

            if actual_pin==pin:
                print('Login successful')
                if actual_pin==pin:
                    com=(input('Press d to deposit \nPress e to withdraw\nPress f to transfer \n>>'))
                    if com=='d':
                         print(input('how much do you want to deposit'))
                    elif com=='e':
                        print(input('Enter amount to be withdrawn'))
                    elif com=='f':
                        print(input('Enter amount to transfer'))
                else:
                    break
        else:
            print('incorrect login')
            continue

    
    

            



            
                