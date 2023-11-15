#creating list
l=[2,3,4,5,6]
print(l)

#accessing list elements through index
l=[2,"hema",3,"sai",[5,"latha",3],6,8]
print(l[2])
print(l[-2])
print(l[-3])
print(l[4][1])
print(l[-3][-2])

#access list elements through slicing
l=[2,"hema",3,"sai",5,"latha",31,6,8]
print(l[2:5])
print(l[:5])
print(l[:])
print(l[3:])
print(len(l))

#concatinate lists
print([1,2]+[3,4]+[5,6])

#multiple of lists or repeating of lists
print(["Python is a easy lang"]*3)

#membership in list
print(2 in [1,2,3,4,5])

a=[1,2,0,3,8]
print(all(a)) #print true if 0 is not there in list else false
print(any(a)) #print true if any pne of the element is true else false
print(list(enumerate(a)))#along index value it prints [(0, 1), (1, 2), (2, 0), (3, 3), (4, 8)]

#adding elements in a list
lis=[1,3,3,4,5,6]
lis[1]=2 #replace with new number through indexing
print(lis)
lis.insert(2,0) #inserting number with indexing
print(lis)
lis.append(10) #adding element at the end of list
print(lis)
lis.extend([20,30,40])#it adds more number of elements as a list at the end of existing list
print(lis)

#removing elements in a list
lis.remove(0) #0 value (not 0 as a index here) will be deleted
print(lis)
lis.pop(2) #3rd index value will be deleted
print(lis)
lis.clear() #it clear entire list elements
print(lis) #[]

#sort the elements in a list
l=[2,6,9,4,3,5,7,1]
l.sort()#ascending
print(l)
l.sort(reverse=True) #descending
print(l)

#copy elements in one list to another list
l1=[10,20,30,40,50]
l2=l1.copy()
l1[1]=100
print(l1)
print(l2)
print(id(l1))#both l1 and l2 have different ids
print(id(l2))

#count() and index() operations in list
l=[10,20,30,10,20,10,10,20,10,20]
print(l.count(10)) #how many times 10 will be there in a list
print(l.count(100))#it got 0 as output because 100 is no there in list
print(l.index(30))# it gives index value of 30
#print(l.index(2))#ValueError: 2 is not in list

#list creation by accepting values at run time
l1=[]
n=int(input("enter the no. of elements"))
for i in range(n):
    i=int(input("enter the value"))
    l1.append(i)
print(l1)


#list comprehension - it is used when you want to create a new list based on the values of an existing list.

lis=[1,2,3,4,5]
new_lis=[i*5 for i in lis]
print(new_lis)

even_lis=[i for i in range(20) if i%2==0]
print(even_lis)



