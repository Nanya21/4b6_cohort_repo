# from string import ascii_letters, ascii_uppercase, ascii_lowercase, digits
# from typing import Any
# import re
# import random
# import time

# user2=input('what is your email:')

# a=(list(ascii_lowercase))
# b=(list(ascii_uppercase))
# c=(list(digits))
# d=('$','#','@')

# user=input('please create a password: ')

# if len(user)>16:
#     print('invalid, maximum length is 16')
# elif len(user)<6:
#     print('invalid, minimum length is 6')
# elif not any(char in a for char in user):
#     print('invalid password')
# elif not any(char in d for char in user):
#     print('invalid password')
# elif not any(char in b for char in user):
#     print('invalid password')
# elif not any(char in c for char in user):
#     print('invalid password')
# else:
#     print('valid password')

# database={}
# database.update({user2:user})
# print(database)


# # print('You have successfully created your account, please go to login page to login')
# # login=input('Enter yout email:')
# # login2=input('Enter your password:')

# # for a in database:
# #     if login==login2:
#         print('valid')




     
x=int(input('x:'))
y=int(input('y: '))
z=int(input('z:'))

if x==y==z:
    print('it is an equilateral triangle')
elif x==y or x==z or y==z:
    print('it is an isosceles triangle') 
else:
    print('it is a scalene triangle')


dictlist=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
sort_dictlist=sorted(dictlist, key=lambda x: x['color'])
print(sort_dictlist)

x=10
while x>0:
    print(x)
    x-=1

x=True
while x:
    print('I am a boy')

    x=False