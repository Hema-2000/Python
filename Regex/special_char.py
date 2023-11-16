import re
#quatifiers
#match=re.finditer("a","abaabaaab") #it gives all occurences of patteren
#match=re.finditer("a+","abaabaaab") #it gives 1 or more occurences
#match=re.finditer("a*","abaabaaab")#it gives all indeces but group of a's
#match=re.finditer("a?","abaabaaab")#it also gives all indeces but single a's
#match=re.finditer("a{2}","abaabaaab")#it gives only 2 a's
#match=re.finditer("a{2,3}","abaabaaab")#it gives min 2 max 3
#for m in match:
#      print(m.start(),"......",m.group())



#predifined character classes
#match=re.finditer("\s","a7Sb @k 9#Az")#it gives indeces for space characters
#match=re.finditer("\S","a7Sb @k 9#Az")#it gives without spaces
#match=re.finditer("\d","a7Sb @k 9#Az")#it gives 0-9 digits
#match=re.finditer("\D","a7Sb @k 9#Az")#it gives without digits remaining all
#match=re.finditer("\w","a7Sb @k 9#Az")#it gives alpanumeric characters including lower and upper characters
#match=re.finditer("\W","a7Sb @k 9#Az")#it gives special characters and spaces
# match=re.finditer(".","a7Sb @k 9#Az")#it finds each and every character in a string
# for m in match:
#       print(m.start(),"......",m.group())



#character class
#match=re.finditer("[abc]","a7Sb@k9#Az")#it prints a,b,and c
#match=re.finditer("[^abc]","a7Sb@k9#Az")#it prints without a,b,c
#match=re.finditer("[a-z]","a7Sb@k9#Az")#it prints small alphabets only
#match=re.finditer("[A-Z]","a7Sb@k9#Az")#it prints upper alphabets only
#match=re.finditer("[0-9]","a7Sb@k9#Az")#it print 0-9 digits only
#match=re.finditer("[a-zA-Z]","a7Sb@k9#Az")#it print both lower and upper case letters
#match=re.finditer("[a-zA-Z0-9]","a7Sb@k9#Az")#it prints alphabets and digits
#match=re.finditer("[^a-zA-Z0-9]","a7Sb@k9#Az")#it printsonly special characters and spaces
# for m in match:
#       print(m.start(),"......",m.group())


# match=re.findall('\d',"i have 23 mangoes")#['2', '3']
# match=re.findall('\d+',"i have 23 mangoes")#['23']
# match=re.findall('\d{2}',"i have 23 apples 2 bananas and 300 grapes")#['23', '30']
# match=re.findall('\d{2,3}',"i have 23 apples 2 bananas and 300 grapes")#['23', '300']
#match=re.findall('\d+',"i have 23 apples 2 bananas and 300 grapes")#['23', '2', '300']
#print(match)




