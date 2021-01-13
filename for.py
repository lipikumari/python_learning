#python loops
#for loops
food=["rice","snacks","curry","loaf","samosa"]
for x in food:
    print(x)
#looping through a string
for x in "curry":
    print(x)
#break statement
food=["rice","snacks","curry","loaf","samosa"]
for x in food:
    if x=="loaf":
        break
    print(x)
#the continue statement
food=["rice","snacks","curry","loaf","samosa"]
for x in food:
    if x=="snacks":
        continue
    print(x)
#the range function
for x in range(4, 36, 4):
    print(x)
#else in for loop
for x in range(6):
    print(x)
else:
    print("lipi")
for x in range(6):
    if (x==3):
        break
        print(x)
    else:
        print("the interval")
#nested loops
veg=["aalu","began","palak","muli"]
nonveg=["lolipop","chicken kosa","kababs","biryani"]
for x in veg:
    for y in nonveg:
        print(x,y)
#pass statement
for x in [0,1,2]:
    pass
