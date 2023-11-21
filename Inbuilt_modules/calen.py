from calendar import *

#it produces month calendar...we need to give year and month as parameters
print(month(2022,1))

#to print entire specified year calender
print(calendar(2022,2,1,9))
#year
#width of the character
#line to line space (between days)
#column to column(between months)

#it gives how any no. of leap years are present in between given specifiedyears
print(leapdays(1980,2019))

#it check whether the given year is leap year or not and it produces boolean output
print(isleap(2023))