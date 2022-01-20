import datetime as dt
import calendar as cal
from datetime import timedelta 


x=int(input("your year:"))
y=int(input("your month:"))
z=int(input("your day:"))

cal1=cal.calendar(x)
print(cal1)



inputdate=dt.date(x,y,z)
today=inputdate.today()
timedelta=today-inputdate
weekday=inputdate.weekday()
while True:
    if weekday==0:
        w="Monday"
        break
    elif weekday==1:
        w="Tuesday"
        break
    elif weekday==2:
        w="Wednesday"
        break
    elif weekday==3:
        w="Thursday"
        break
    elif weekday==4:
        w="Friday"
        break
    elif weekday==5:
        w="Saturday"
        break
    elif weekday==6:
        w="Sunday"
        break
if x%4==0:
    print(x,"is leap year")
else :
    print(x,"is not leap year")
print("today is",w)
print("today`s date is",today)
print(timedelta)
