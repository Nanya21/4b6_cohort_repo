a=[1,2,3,4,5,6,7,8,9]
b=[]
# for i in a:
#     if i%2==0:
#         b.append(i)
# print(b)

# alternative_b=[i for i in a if i%2==0]
# print(alternative_b)

# a=[(0,'sheldon'),(1, 'penny')]
# for e in a:
    # print(e[1])
# for e in a:
#     print(e)

# a=[0,1,2]
# b=[2,4,6]
# c=[]
# for i in a:
#     for x in b:
#         c.append(i+x)
# print(c)

lis=[10,20,30,40]
list2=[100,200,300,400]
list2.reverse()
ab=list(zip(lis,list2))

for i,a in ab:
    print(i,a)



