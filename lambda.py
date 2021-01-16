#Python Lambda
x=lambda a:a+100
print(x(55))

#multiple argument
x=lambda a,b:a*b
print(x(7,8))
x=lambda a,b,c:(a+b)*c
print(x(8,2,9))
def myfunc(n):
    return lambda a:a*n
mydoubler= myfunc(2)
print(mydoubler(11))
