#Tuples in python:-A tuples is a collection which is ordered and unchangeable.tuples are written with round brackets.
#example
thistuple=("lipi" ,"alone" , "broken")                                    
print(thistuple)
#Acess Tuple items
print(thistuple[2])
#negative indexing
print(thistuple[-1])
#range of indexes
item=("hate", "abused" , "ignorance" , "alone" , "tired")
print(item[1:4])
#range of negative indexes
print(item[:-3])
#change tuple values
x=("litchi", "mango" , "onion" , "papaya", "potato")
y=list(x)
y[1]="hatemyself"
print(y)
#loop through a tuple
thistuple=("lipi" , "hate" ,"alone" ,"poetry")
for x in thistuple:
    print(x)
#check if item exists
    if "lipi" in thistuple:
        print("yes , lipi is in this tuple")
#tuple length
print(len(thistuple))
#add items :- tuples are unchangeable , so we can't add item in this.
#create  tuple with one item- to create one item we have to use coma after that item so python can recognize item is a tuple.
x=("lipi",)
print(type(x))
#remove item - we cant remove item in tuple
#Tuples are unchangeable, so you cant remove item from it , but you can permannentely delete this using del keyword.
thistuple=("lipi" , "sad" , "angry" , "hate")
#del thistuple
print(thistuple)
#join two tuples
tuple1=("i" , "hate" , "everyone" , "hateuall")
tuple2=("lipi" , "yiu" , "are" , "looser")
tuple3=tuple1+tuple2
print(tuple3)
#tuple constructor- it is possible to use tuple constructor to make a tuple
x=tuple(("lipi" , "lipi" , "lipi" , "lipi"))
print(x)
