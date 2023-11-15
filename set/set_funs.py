#creating sets
s={}
print(type(s)) #<class 'dict'>
s=set()
print(s,type(s))#set() <class 'set'>

#add(),update()
s={1,2,3,4}
s.add(5)
print(s)
s.update(["hema",7,8,"latha"])
print(s)

#discard(),remove(),clear(),pop(),del()
s.discard(100)
print(s)
s.discard("latha")
print(s)
#s.remove(100)#KeyError: 100
s.remove("hema")
print(s)
s.pop() #we cant expect which element in set will be poped
print(s)
s.clear()
print(s)
#del s
#print(s) #NameError: name 's' is not defined

#set functions
A={1,2,3,4,5}
B={4,5,6,7,8}
print(A|B)
print(A.union(B))
print(A&B)
print(A.intersection(B))
print(A-B)
print(A.difference(B))
print(B-A)
print(A^B)
print(A.symmetric_difference(B))

#len(), max(),min(),sum()
s={1,2,3,4,5}
print(len(s))
print(id(s))
print(max(s))
print(min(s))
print(sum(s))
print(sum(s,8))

#membership operator
print(5 in s)
print(10 in s)

#copying of sets
x=s.copy()
print(x)

#x={2,5,"hello",[1,2,3]} #TypeError: unhashable type: 'list'
#print(x)#set elements must be immutable


s={1,2,3,0}
print(all(s))
print(any(s))
print(list(enumerate(s)))

#seet functions
s1={1,2,3,4}
s2={3,4}
print(s2.issubset(s1))
print(s1.issubset(s2))
print(s2.issuperset(s1))
print(s1.issuperset(s2))

#set creation by accepting values from run time
s=set()
n=5
for i in range(n):
    i=int(input("enter value:"))
    s.add(i)
print(s)