# my_list=['this', True, 'student', 45,66.43]
# newlist=my_list.copy()
# print(newlist)


samplelist=['Red', 'Green', 'white', 'Black', 'pink', 'yellow']
first=samplelist.pop(0)
last= samplelist.pop(-2)
last_=samplelist.pop(-1)
print(samplelist)


# colorlist=['Red', 'Green', 'white','Yellow']
# user= input('Welcome, what is your favorite color: ')
# colorlist.append(user)
# print(colorlist)

list1=[10,20,[300,400,[5000,6000],500],30,40]
ab=list1[2]
abc=ab[2]
c=7000
abc.append(c)
print(list1)