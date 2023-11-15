#printing string along with address
s1="hema"
print(s1,id(s1))

s1="latha"
print(s1)

#print string with format specifiers
name="sravani"
age=25
#print("{0} age is {1}",.format(name,age)) #SyntaxError: invalid syntax
print("%s age is %d" %(name,age))
print("{} age is {}" .format(name,age))

#index(),rindex(),find()
s="python is very easy and it is oop and it is interpreter"
print(s.index("easy"))
print(s.rindex("is")) #it produces occurence of last index value for specified string
print(s[5])
print(s.find("is")) #it produces the index value where it finds the specified value

#find length of string
print(len(s))

#indexing & slicing
s2="hemalatha"
print(s2[-1])
print(s2[5])
#print(s2[12]) #IndexError: string index out of range
print(s2[2:6])
print(s2[-3:])
print(s2[:-3])
print(s2[-5:-1])
print(s2[:]) #all letters in a string
print(s2[0:9:1])#accessing 0 to 8 index elements with order of 1.
print(s2[::-1])#reverse entire string

#concatination & repeating
s3="hema"
s4="latha"
print(s3+s4)
print(s3+" "+s4)
print(s3*3)
print((s3+" ")*3)

#split()
s="python is very easy and it is oop"
s1=s.split(" ",3) #it splits first 3 words and it produces list as output
#if not specify 3 means it splits entire string not 3 words
print(s1)#['python', 'is', 'very', 'easy and it is oop']
print(type(s1))#<class 'list'>
for i in s1:
    print(i)

#capitilize() $ title()
s4="hemAlatHa"
print(s4.capitalize()) #first letter converts into capital remaining all are small
print(s4.title()) #both perform same operations

#lower() & upper()
s5="heMaLaThA"
print(s5.upper())
print(s5.lower())

#count()
s="python is very easy and it is oop and it is interpreter"
substring="is"
print(s.count(substring))
print(s.count("and"))#it counts how many times that specified string present
print(s.count("is"))
print(s.count("x"))
print(s.count(" "))
print(s.count('a'))

#replace()
s="my name is hema"
print(s.replace("hema","latha"))

#join()
print(",".join("aeiou"))#join comma in between the letters
print(" ".join(["apple", "banana"])) #join space in between strings

#reverse string with space existence
print(" ".join(reversed("SAI")))
#or
s="SAI"
print(s[::-1])

#sort()
s="python is very easy"
s1=s.split(" ")#for sorting string we need to split it
print(s1)
s1.sort() #it got ascending order of alphabets
print(s1)
s1.sort(reverse=True)#it got descending order depends on alphabetically
print(s1)

#swapcase()
s="hemalatha"
print(s.swapcase())#if it is uppercase it prints into lowercase or vise versa
s="HEMALATHA"
print(s.swapcase())

#strip()
s=" durga "
print(s.strip(" "))#it removes whitespaces at begining and at the ending of the string
s="adurga"
print(s.strip('a'))#it removes a at ending and starting
print(s.lstrip('a'))#it removes a at starting but not end
print(s.rstrip('a'))#it removes a at end but not starting

#max() & min()
s="HEMALATHA"
s1="hemalatha"
print(max(s)) #it produces max alphabet in a  string
print(max(s1))
print(min(s)) #it produces min alphabet in a  string
print(min(s1))

#partition()
s="python is very easy and it is oop"
s1=s.partition("is") #it produces 3 partitions(before separator,separator and after the separator)
print(s1,type(s1))#tuple type it produces

#startswith() & endswith()
s="Hemalatha"
print(s.startswith('h')) #it is used to check the statement is true or false at starting
print(s.startswith('H'))
print(s.endswith('a')) #it is used to check the statement is true or false at ending
print(s.endswith('t'))

#isdigit() & isalpha() & isalnum()
s="12345"
print(s.isdigit())
s="12345a"
print(s.isdigit())
s="abcd"
print(s.isalpha())
s='abcd12'
print(s.isalpha())
s="abcd"
print(s.isalnum())
s="1234"
print(s.isalnum())
s="123abc"
print(s.isalnum())
s="$%#%"
print(s.isalnum())