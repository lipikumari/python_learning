#String formatting
#String format()
item=10
txt="the numbers of item{}"
print(txt.format(item))
txt="the numbers of items are {:.2f}"
print(txt.format(item))
#Multiple values
quantity = 345
price=789
txt="i want {} items  for {:.2f}"
print(txt.format(quantity,price))
#index numbers
quantity=3
itemno=6
price=123
txt=" I want {0} piece of item number {1} for {2:.2f} thousands"
print(txt.format(quantity,itemno,price))

