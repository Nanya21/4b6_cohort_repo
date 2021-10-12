import random
from string import digits
import time
import ast




user_data={}
setup=True
transaction={}

while setup:
    action=input('To create your account number press a \nFor login press b \n>>').lower()

    if action== 'a':
        name= input('Enter your name\n>>')
        pin=(input('Enter any four digit number\n>>'))
        re_pine= (input('Confirm your pin\n>>'))
        a=['0']
        a.extend([random.choice(digits) for n in range (9)])
        account=''.join(a)
        data=[('name',name),('pin', pin),('balance',0)]
        #create empty transaction

        transaction[account]=[]
       
        if (len(pin) > 4) or (len(pin)< 4):
            print('pin length should be 4')
        elif pin!=re_pine:
                print('incorrect pin')
                break

        
        user_data[account]={}
        user_data[account].update(data)
        datae=open('user.txt', 'a') 
        datae.write(f"{user_data}\n")
        print(user_data)

        def reading(first):
            with open('user.txt','r') as datae:
                a= datae.read()
                user_data=ast.literal_eval(a)


        print(f"Hi {name},Your account has been succesfully created. Yout account number is {account}. And your current account balance is NGN0.\n Please login to perform other tranascations.")
        
        next= input('Enter d to do something else or any other key to quit. \n').lower()
        if next=='d':
            continue
        else: 
            break

    elif action=='b':
        account= input('please enter your account number \n>>')
        acctname= user_data.get(account,False)
        print(f"Welcome {acctname.get('name')},")
        
        login=True
        while login:
            pin= input('Enter your pin \n>>')
            time.sleep(2)
            acct=user_data.get(account, False)
            if acct and acct.get('pin')==pin:
                action_b=input("""press d for deposit\npress w for withdrawal\npress t for transfer\npress g to check account balance\npress s for transaction details
          press any other key to quit\n>>""").lower()
            else:
                print('Please enter a valid account number and pin')
                break
    
    
            if action_b=='d':
                amount=float(input('Enter amount to be deposited.\n>>'))
                acct['balance']+=amount
                print('Deposit successful')

                # save transaction detail

                trans_data={
                        'amount':amount,
                        'trans_type':'Credit',
                        'transaction':'Deposit'
                    }

                transaction[account].append(trans_data)
                con=input("Do you want to perfom another transaction, press y to continue and any other key to quit\n>>")

                if con=='y':
                    continue
                else:
                    break
            elif action_b=='w':
                amount=float(input('Enter amount to be withdrawn.\n>>'))
                if amount>= acct.get('balance',0):
                    time.sleep(2)
                    print('Insufficient funds')
                else:
                    acct['balance']-=amount
                    print('Please take yout cash.')
                    # save transaction detail

                    trans_data={
                        'amount':amount,
                        'trans_type':'Debit',
                        'transaction':'Withdrawal'
                    }

                    transaction[account].append(trans_data)
                con=input("Do you want to perfom another transaction, press y to continue and any other key to quit")
                if con=='y':
                    continue
                else:
                    break
                    
            elif action_b=='t':
                amount=float(input('Enter amount to transfer\n>>'))
                recipient_acct= input('Enter beneficiary account number\n>>')

                recipient=user_data.get(recipient_acct, False)
                if recipient:
                    if amount>=acct.get('balance',0):
                        print('Insufficient funds')
                    elif recipient:
                        acct['balance']-=amount
                        recipient['balance']+=amount
                        print('Transfer Successful')
                        # save transaction detail

                    trans_data={
                        'amount':amount,
                        'trans_type':'Debit',
                        'transaction':'Withdrawal'
                    }

                    transaction[account].append(trans_data)

                    # save transaction detail

                    beneficiary_data={
                        'amount':amount,
                        'trans_type':'Debit',
                        'transaction':'Withdrawal'
                    }

                    transaction[recipient_acct].append(beneficiary_data)
                        
                else:
                    print('Invalid account number')
                con=input("Do you want to perfom another transaction, press y to continue and any other key to quit\n>>")
                if con=='y':
                    continue
                else:
                    break
                        
            elif action_b=='g':
                bal=acct.get('balance')
                print(f"Your account balance is {bal}")
                con=input("Do you want to perfom another transaction, press y to continue and any other key to quit\n>>")
                if con=='y':
                    continue
                else:
                    break
            elif action_b=='s':
                if len(transaction[account])>0:
                    previous_data=transaction[account][-5:]
                    print('Here is your last 5 transactions')
                    for a in previous_data:
                        print('Amount:',a['amount'])
                        print('transaction type: ', a['trans_type'])
                        print('transaction:', a['transaction'])
                

                con=input("Do you want to perfom another transaction, press y to continue and any other key to quit")
                if con=='y':
                    continue
                else:
                    break
            else:
                break
    

   


            



    
    

            



            
                