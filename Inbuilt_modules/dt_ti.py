# import datetime
# print(datetime.datetime.now())
       #or

from datetime import *

# print(datetime.now())

x=datetime.now()
print(x)
print(x.time())
print(x.date())

print(x.strftime('%A')) #fullform of weekday
print(x.strftime('%a')) #shortform of weekday
print(x.strftime('%B')) #fullform of month
print(x.strftime('%b')) #shortform of month
print(x.strftime('%Y')) #fullform of year
print(x.strftime('%y')) #shortform of year





