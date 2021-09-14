# print("beautiful" + " city")
# name = 'ifunaya'
# print(name[3])
# print(name[-4])

# name = 'Ifunaya'; surname = ' Ekoh'
# fullname= 'Ifunaya Ekoh'
# print(name+ surname)
# print(fullname [-4:])
# new_string= 'blue sky'
# print(new_string[2:5])
# print(new_string[: 5])
# print(new_string[2:])
# print(new_string[2:8:2])

# name = "Naya"
# price= 30
# # print("Welcome {}".format(name))
# print(f"Welcome {name}")
# print(f'{price}')

# name= input('Tell us who you are: ')
# # print(name)
# print("Welcome {}. You have just signed in".format(name))

# name= input('Hello: ')
# age= int(input('what is your age: '))
# # print("Welcome {}". format(name))

# year=(2021-age)

# # print(year)
# print("welcome {}. You were born in {}". format(name,year))


# name = input('what is your name: ')
# print("Welcome {}.\nYou have just signed in. \n\tSigned\n\tManagement".format(name.title()))

# name= "John.pdf".lower()
# # print(name.startswith('t'))
# print(name.endswith('pdf'))

# fullname='Ifunaya Mercy Ekoh'
# namelist= fullname.split()
# print(namelist)
# print(namelist[2])

# word_list= ['Desmond', 'Nnebue', 'chu']

# joined= ''.join(word_list)
# Ajoin= " ".join(word_list)
# print(joined)
# print(Ajoin)

# name="I am a boy"
# namesplit= name.split()
# newname= "-".join(namesplit)
# print(newname)
# word='I am a boy'
# word= word.replace(' ', '-')
# print(word)


user= input('what do you need: \n>')
Question_1= '''I hope life treats you kind and i hope you have all you've dreamed of in life
above all, i wish you good health and happiness in your life and a blissful life
I hope life is good to you as you've been good to me in life, I hope you have
reasons to smile in life and be happy in life. Have a long and healthy life'''.lower()
a= (Question_1.count(user))
print(f'{a} found')
word= Question_1.replace(user, user.upper())
print(word)

