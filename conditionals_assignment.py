from string import ascii_letters, ascii_uppercase, ascii_lowercase, digits
from typing import Any
import random
a=(list(ascii_lowercase))
b=(list(ascii_uppercase))
c=(list(digits))
d=('$','#','@')
output=a+b+c


user=input('please create a password: ')

if len(user)>16:
    print('invalid, maximum length is 16')
elif len(user)<6:
    print('invalid, minimum length is 6')
elif user in output:
    print('valid password')
elif user in d:
    True
else:
    print('''Invalid password, password must contain uppercase, 
    lowercase, digit and special characters '@','#','$''')


     
# x=int(input('x:'))
# y=int(input('y: '))
# z=int(input('z:'))
# a= int(x+y+z<=180)

# if x+y+z!=180:
#     print('it is  not a triangle')
# elif x==y==z:
#     print('it is an equilateral triangle')
# elif x==y or x==z or y==z:
#     print('it is an isosceles triangle') 
# else:
#     print('it is a scalene triangle')


# dictlist=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# sort_dictlist=sorted(dictlist, key=lambda x: x['color'])
# print(sort_dictlist)