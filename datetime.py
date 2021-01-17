#Python Datetime
#current date and time
import datetime
x=datetime.datetime.now()
print(x)
#date output
import datetime
x=datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))
#creating date objects
import datetime
x=datetime.datetime(2021,1,17)
print(x)
#The strftime() method
import datetime
x=datetime.datetime(2021,2,17)
print(x.strftime("%B"))
