import random

# brac= [1, 27, 20, 20, 17, 12, 32, 28, 25, 22, 20, 48, 26, 21,]
# print(brac)
# summ=sum(brac)
# n=len(brac)
# meann=summ/n
# print(meann)

# def mean_of_brac(a):
#     summ=sum(a)
#     b=len(a)
#     meann=(summ/b)
#     return meann
 


# def median_of_brac(b):
#     a=len(b)
#     b.sort()
#     if a %2==0:
#         m1=b[a//2]
#         m2=b[a//2-1]
#         m=(m1+m2)/2
#         return m
#     else:
#         m=b[a//2]
#         return m

# def VAR(c):
#     summ=sum(c)
#     b=len(c)
#     meann=(summ/b)
#     dev=[(a - meann) ** 2 for a in c]
#     var= sum(dev)/b
#     return var

# def S_D(c):
#     summ=sum(c)
#     b=len(c)
#     meann=(summ/b)
#     a= [(a - meann) ** 2 for a in c]
#     c=sum(a)/b
#     s_d=c**0.5
#     return s_d




# print(mean_of_brac(brac))
# print(median_of_brac(brac))
# print(VAR(brac))
# print(S_D(brac))

# def Modee(b):
#     a={}
#     for i in b:
#         if i in a.keys():
#             a[i]+=1
#         else:
#             a[i]=1
#     max_key= max(a, key=a.get)
#     return max_key

# print(Modee(brac))

# def prime(a):
#     if a <= 1:
#         return False
#     if a==2:
#         return True

#     for i in range(2,a):
#         if a % i==0:
#             return False
#     return True
# def primee(b):
#     return list(filter(lambda x:prime(x),b))

# print(primee(brac))


myfile=open('merci.txt', mode='r')
# myfile.write('\nI am beautiful\nI am special\n I am great')
#or
#it can also be written with writelines and that option requires a list 
# myfile.writeline(['This is lovely\n','I am tall'])

texts=myfile.read()
print(texts)