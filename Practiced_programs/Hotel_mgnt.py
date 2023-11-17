import re
print("welcome to Taj hotels")
customer_name=input("enter customer name: ")
print("how can i help you {}".format(customer_name))
benifits='''
             room
             power
             food
        '''

details={"room":2000,"power":500,"food":1000}
n=0
while n<3:
    choose=input("enter input as 1 to choose benifits")
    if choose=='1':
        print(benifits)
    else:
        s=str(details)
        a=s.replace("{" , "")
        b=a.replace("}" , "")
        c=b.replace("," , "\n")
        print(c)
        n+=1

print("sorry no more attempts!")
choice=input("enter which one u need")
if choice=="room" or "power" or "food":
    print("do registration process")
    num=input("enter the number:")
    match=re.fullmatch("\d{3}-\d{3}-\d{4}",num)
    if(match==None):
        print("enter valid mobile number")

    else:
        days=int(input("how many days u want to stay"))
        memders=input("how many members want to stay")
print("Thanks for your response")
print("have a nice day!")

