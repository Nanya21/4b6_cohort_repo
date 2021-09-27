# T1=(False, True, 100)
# T2=(1,4,9)
# T3= T1+T2
# print(T3)
# del T2

# first='John'
# second = 'Bull'
# first, second = second, first
# print(first)


s ={'True', 'Born', 45, 'Water','John'}
# # s.remove("Johnson")
# # print(s)
# s.discard('Johnson')
# print(s)

u={'Mary','Tunde','Favour',50,'John'}
# a=s.union(u)
# print(a)
# s.update(u)
# print(s)

# a= u.pop()
# print(a)

# print(s.difference(u))
# print(u.difference(s))
# print(s.symmetric_difference(u))

# set1= {10,20,30,40,50}
# set2={30,40,50,60,70}
# set3=set1.intersection(set2)
# print(set3)

# a={10,20,30,40,50}
# b={30,40,50,60,70}
# c=a.union(b)
# print(c)

# a={10,20,30}
# b={20,40,50}
# a.difference_update(b)
# print(a)

# a={10,20,30,40,50}
# a.difference_update({10,20,30})
# print(a)

# c={10,20,30,40,50}
# d={30,40,50,60,70}
# f=c.symmetric_difference(d)
# print(f)

# a={10,20,30,40,50}
# b={30,40,50,60,70}
# a.intersection_update(b)
# print(a)


n=[20,30,25,0,-10,-15,-18]



positive= []
negative= []
zero= []
for a in n:
 if a > 0: 
     positive.append(a)
 elif a<0: 
     negative.append(a)
 else:
     zero.append(a)
#  print(positive)
#  print(negative)
#  print(zero)
 ratio_p=len(positive)/len(n)
 ratio_n=len(negative)/len(n)
 ratio_z=len(zero)/len(n)
#  print(ratio_p)
print("{:.6f}".format(ratio_p))
print("{:.6f}".format(ratio_n))
print("{:.6f}".format(ratio_z))
