##creating dictionary
d=dict({})
print(d)
print(type(d))
   #or
d={}
print(d)
print(type(d))

#adding items into dictionary
d={"name":"hema","age":24}
print(d)
d["gender"]="female"
print(d)
d["gender"]="male"
print(d)

#dictional within a dictionary as a value
d={"name":"hema","family":{"father":"raju","mother":"laxmi"},"age":24}
print(d)

#dont specify 2 similar keys in a dictionary
d={"name":"hema","age":24,"name":"latha"}
print(d)


#d={[1,2,3]:"list"}#TypeError: unhashable type: 'list'
#print(d)

#accessing values through keys
d={'name': 'hema', 'age': 24, 'gender': 'female'}
print(d["name"])
print(d.get("name"))

#copying one dictionary to another
d1=d.copy()
print(d1)

#accessing keys, values and items
print(d.items())#dict_items([('name', 'hema'), ('age', 24), ('gender', 'female')])
print(d.keys())#dict_keys(['name', 'age', 'gender'])
print(d.values())#dict_values(['hema', 24, 'female'])

#length of dictionary
print(len(d))#3

#membership in dictionary
print("name" in d)
print("hema" in d)# membership operator is only for keys not values

#print(d.pop())#TypeError: pop expected at least 1 argument, got 0
#print(d.pop("name")) #it poped  assigned keyword
#print(d)

#print(d.popitem())#it poped last item in dictionary
#print(d)
# d.clear()
# print(d)#{}

#updating dictionary
x={"father":"raju","mother":"laxmi"}
print(x)
d1.update(x)
print(d1)

#dictionary comprehension
new_dic={x:x**2 for x in range(10) if x**2 %2==0}
print(new_dic)#{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


#creating dictionary by taking user inputs at run time
d={}
n=5
for i in range(n):
    k=(input("enter alphabet:"))
    v=int(input("enter value"))
    d[k]=v
print(d)





