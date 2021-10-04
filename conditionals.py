# shoppinglist=(input('what was the price of the items you bought: '))
# items=(shoppinglist.split(','))
# print(items)
# fun=list(map(lambda string: int(string), items))
# print(sum(fun))
# print(sum(fun)/len(fun))


# li=[1,2,3,4,5]
# sqr=lambda i: i**2
# obj=list(map(lambda i:i**2,li))
# print(obj)

# c=['002','014','029']
# p=[2000,4000,2015]
# d=dict(zip(c,p))
# a=list(zip(c,p))
# # print(d)
# # print(a)
# print(list(enumerate(c)))

# mylist=[2,3,5,7,8,20,4,1,9]
# o=list(filter(lambda a:a%2!=0,mylist))
# print(o)

# import time
# user=input('Enter your name:\n>')
# print('creating account, please wait...')
# time.sleep(3)
# print('.')
# time.sleep(2)
# print('.')
# time.sleep(1)
# print('Almost there...')
# time.sleep(2)
# print(f"Welcome {user}, your account has been created")

# import random
# mylist=[2,3,5,3,1,55,7,4]
# random.shuffle(mylist)
# print(mylist)
# print(random.sample(mylist,3))
# random.seed(2)
# print(random.randrange(3,10))

# from datetime import datetime
# print(datetime.now())

# date=datetime.now()
# print(datetime.strftime(date,'%A,%d %B %Y'))

# def random_nums(n):
#     return [random.randrange(n) for i in range(n)]


# print('Welcome to this game')
# listofnumbers=[96,60,55,67,65,57,82,52,16,91,60,46,70,1,6]
# choice= int(input(f"Guess number from:\n{listofnumbers}\n>>"))
# random.shuffle(listofnumbers)

# com_choice=random.choice(listofnumbers)

# if choice==com_choice:
#     print('You win')
# else:
#     print('E be like say you no win. sorry')

# import time
# import random

# mercyville= input('Welcome to Mercyville, \nRules are pretty simple, All you need do is choose between the following options:,\nRock, paper or scissors\nI know right*winks*, \n Kindly pick your username:')
# mercyville2=input('kindly choose your option: ').title()

# gamelist=['Rock','Paper','Scissors']
# random.shuffle(gamelist)
# com_choice=random.choice(gamelist)
# print(com_choice)

# if com_choice==mercyville2:
#     print('awwn, it is a tie')
# elif com_choice==gamelist[0] and mercyville2==gamelist[2]:
#     time.sleep(2)
#     print('oops, you lose')
# elif com_choice==gamelist[1] and mercyville2==gamelist[0]:
#     time.sleep(2)
#     print('oops, you lose')
# elif com_choice==gamelist[2] and mercyville2==gamelist[1]:
#     time.sleep(2)
#     print('oops, you lose')
# elif com_choice==gamelist[1]and mercyville2==gamelist[0]:
#     time.sleep(2)
#     print('you win, yaay')
# elif com_choice==gamelist[2] and mercyville==gamelist[0]:
#     time.sleep(2)
#     print('You win, yaay')
# elif com_choice==gamelist[1] and mercyville2==gamelist[2]:
#     time.sleep(2)
#     print('You win, yaay')
# else:
#     time.sleep(2)
#     print('incorrect input, pls choose between Rock, Paper and Scissors')
    
# print(f"Hey {mercyville}, \nWould you like to play again?\n")
answer=input('Yes or No')