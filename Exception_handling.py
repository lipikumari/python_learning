#Exception handling in python
#try:
 #   print(x)
#except:
 #   print("an exception occured")
#Many Exception
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("something else went wrong")
#Else
try:
    print(x)
except:
    print("something else went wrong")
else:
    print("nothing went wrong")
#Finally
try:
    print(x)
except:
    print("something else went wrong")
finally:
    print("The try and except block is finished")
#Raise an exception
x=-1
if x<0:
    raise Exception("sorry,no numbers below zero")
