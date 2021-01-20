#Python scope
#A variable is only available from inside the region it is created.this is called scope.
#Local scope
def myfunc():
    x=675
    print(x)

myfunc()
#function inside function
def myfunc():
    x=908
    def innerfunc():
        print(x)
    innerfunc()
myfunc()
#Global scope
x=378
def myfunc():
    print(x)
myfunc()
print(x)
#Naming variables
x=456
def myfunc():
    x=899
    print(x)
myfunc()
print(x)
#Global keyword
def myfunc():
    global x
    x=890
myfunc()
print(x)
#another ex of global keyword
x=450
def myfunc():
    global x
    x=678
myfunc()
print(x)
