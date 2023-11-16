import re


# name="John age is 23 and Hema age is 24 and Nishitha age is 26 and Suma age is 27"
# l=re.findall("[A-Z]\w+|\d+",name)
# print(l)
# # ['John', '23', 'Hema', '24', 'Nishitha', '26', 'Suma', '27']
# print(len(l))
# d={}
# for i in range(0,len(l),2):
#     d[l[i]]=l[i+1]
# print(d)#{'John': '23', 'Hema': '24', 'Nishitha': '26', 'Suma': '27'}


#to check valid number or not
# pattern= "^\d{3}-\d{3}-\d{4}$"
# ph_no=input("enter the number")
# match=re.match(pattern,ph_no)
# if match!=None:
#     print("valid mobile number")
# else:
#     print("invalid mobile number")


#findall returns empty list for no match case
#search will return None for no match case


#it splits only only space word because flag value is mentioned
# txt = "The rain in Spain"
# x = re.split("\s", txt, 1)#['The', 'rain in Spain']
# print(x)

#it replaces only first 2 spaces because flag is mentioned
# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2) #The9rain9in Spain
# print(x)

#below search() returns object
# txt = "The rain in Spain"
# x = re.search("ai", txt) #<re.Match object; span=(5, 7), match='ai'>
# print(x)


# txt="tajmahal is my fav@rate place"
# search=re.search("\w+@\w+",txt)
# if search!=None:
#     print(search.group())
# else:
#     print(not found)


#program to remove empty strings
#multiline string
# s="aas dfr sw\
# gd he ns\n fds"
# pattern="\s" #removing empty spaces
# replace=''
# new_str=re.sub(pattern,replace,s,1)#it replace only 1st space
# new_str=re.sub(pattern,replace,s)
# str=re.subn(pattern,replace,s)#('aasdfrswgdhensfds', 6) it gives how many times it gets replace
# print(new_str)
# print(str)


# string = '39801 356, 2102 1111'
# pattern = '(\d{3}) (\d{2})'
# match = re.search(pattern, string) #801 35 using search
# # match = re.match(pattern, string) #not match using match
# if match:
#   print(match.group())
# else:
#   print("pattern not found")


#to identify valid mobile number
# pattern="[7-9]\d{9}"
# num=input("enter the number")
# res=re.fullmatch(pattern,num)
# if res!=None:
#   print("mobile num is valid")
# else:
#   print("invalid mobile number")



#to check valid gmail or not

# mail=input("enter the gmail")
# res=re.fullmatch("\w[a-zA-Z0-9._]*@gmail[.]com",mail)
# if res!=None:
#   print("valid mail id")
# else:
#   print("invalid mail id")


mailid=input("Enter Mail id:")
m=re.fullmatch("\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*",mailid)
if m!=None:
  print("valid")
else:
  print("not valid")
