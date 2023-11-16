import re #to working with regular expressions

#compile() & finditer()
data="abaabbcaccaabcaa"
pattern=re.compile("aa") #compile function is used to compile the pattern
count=0
match=pattern.finditer(data) #finditer func is used to find the match for given pattern
for i in match:
    count+=1
    print(i.start(),".....",i.end(),".....",i.group()) #it gives start and end indexes along with matched group
print("occurence of pattern in a data: ",count)



#or symbol & findall()
pattern=r'girls|boys' #it search for girls as well as boys
match=re.findall(pattern,"they have birth to 2 girls ")#['girls']
match=re.findall(pattern,"they have 2 girls and 2 boys")#['girls', 'boys']
print(match)


#split()
pattern=r'\s'
num=re.split(pattern,"python is a interpreted language")
#when space is identifies then it split that word as a element in list
print(num)#['python', 'is', 'a', 'interpreted', 'language']
print("no. of items in a string: ",len(num))



#'.' have special function i.e., it finds every character in a string except newline
#to blame the compiler we used escape sequence as \
l = re.split("\.", "www.durgasoft.com")
print(l)
for t in l:
    print(t)



#sub()
pattern = r'newdelhi'
str1= "i like newdelhi the most"
new_str = re.sub(pattern, 'Delhi', str1)#substitute the newword in place of old word
print(str1) #we cant change the string because it is immutable
print(new_str)


#sub() & subn()
s=re.sub("[a-z]","#","a7b9c5k8z")
print(s)
s=re.subn("[a-z]","#","a7b9c5k8z")#it tells how many times it gets substituted
print("how many times it gets replaced",s[1])



#ignorecase()
s="Learning Python is Very Easy"
m=re.search("EASY$",s,re.IGNORECASE)#it ignores if it may be in lower or uppercase
if m != None:
    print("Target String Ends with Easy")
else:
    print("Target String Not Ends with Easy")


#match()
s="lion is king of forest"
pattern=input("enter the pattern")
match=re.match(pattern,s)#it find only the pattern is present at starting or not
if match!=None:
    print("the match is available at starting")
    print("start index: ",match.start(), "and", match.end())
else:
    print("match is not available at starting")



pattern = r'^[A-Za-z]+\d+$'
#it means pattern should starts with [A-Za-z] here +denotes any no. of alphabets
#pattern should ends with digits here +denotes any no. of digits
#^ means pattern starts with and $ means pattern ends with
string = 'hello123'
if re.match(pattern, string):
    print('pattern matched!')
else:
    print('pattern not matched.')


#fullmatch()
s="lion is king of forest"
pattern=input("enter the pattern")
match=re.fullmatch(pattern,s)#it check the entire string is matched or not
if match!=None:
    print("the complete string is matched ")
else:
    print("complete string is not matched")



#search()
s="lion is king of forest"
pattern=input("enter the pattern")
match=re.search(pattern,s) #it search the pattern with in entire string
if match!=None:
    print("the match is available ina string")
    print("for the first occurence of pattern ,start index: ",match.start(), "and", match.end())
else:
    print("pattern is not available")



















