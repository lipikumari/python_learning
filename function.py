#creating a function
def my_function():
    print("Hello my function")
#calling a function
def my_functio():
    print("hello my functio")
my_functio()
#argument
def my_function(fname):
    print(fname+"Kumari")

my_function("Lipi")
my_function("prachi")
my_function("lusi")
#number of arguments
def my_function(fname , lname):
    print(fname + "  "+ lname)
my_function("Lipi","kumari")
#arbitary arguments(*args)
def my_function(*kids):
    print("the younger kid is "+ kids[4])
my_function("Lipi","cutee","prachi","kundu","deep")
#keyword arguments (key=value)
def my_function(child1,child3,child2):
    print("my cutest child is " +child2 )
my_function(child1="lipi" , child2="cutee",child3="dodgo")
#arbitary keyword arguments , **kwargs
def my_function(**kid):
    print("his lname is " + kid["lname"])
my_function(fname="Lipi" , lname="thakur")
#default parameter value
def my_function(country="India"):
    print("my country is "+ country)
my_function("USA")
my_function()
my_function("Nepal")
my_function("China")
#passing a list as an argument
def my_function(food):
    for x in food:
        print(x)
fruits=["litchi","orange","apple"]
my_function(fruits)
#return values
def my_function(x):
    return x*5
my_function(9)
print(my_function(7))
#pass statement
def my_function():
    pass
#recursion
def tri_recursion(k):
    if(k>0):
        result=k+tri_recursion(k-1)
        print(result)
    else:
        result=0
    return result
print("\nRecursion example results")
tri_recursion(8)
