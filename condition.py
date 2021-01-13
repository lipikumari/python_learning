#Python condition
#if statement
a=100
b=70
if(a>b):
    print("a is greater than b")
#elif
a=33
b=33
if(b>a):
    print("b is greater than a ")
elif(a==b):
    print("a is equal to b")
#else
a=332
b=100
if(b>a):
    print("b is greatewr than a")
elif(a==b):
    print("a is equal to b")
else:
    print("a is greater than b")
#short hand if
a=90
n=89
if a>n: print("a is greater than n")
#short hand if else
a=80
b=9
print("Lipi") if(b>a) else print("Deepayan")
#And keyword
a=90
b=70
c=900
if a>b and c>a:
    print("a is greater than b and c is greater than a")
#or keyword
a=90
b=40
c=450
if a>b or a>c:
    print("At least one of the condition should be true")
#Nested if
a=90
if a>19:
    print("Above 19")
    if a>20:
        print("Above 20")
    else:
        print("something")
#pass
a=79
b=80
if b>a:
    pass
