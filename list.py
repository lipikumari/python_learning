#Python list- A list is a collection which is ordered and changeable. in python list are written with square brackets.
#examples
list=["i" , "hate" , "myself"]
print(list)
#Acess item
print(list[1])
#negative indexing
print(list[-2])
#range of indexes
item=["lipi" , "looser" , "hate" ,"i" ,"hste" ,"myself"]
print(item[1:5])
print(item[:3])
#range of negative indexes
print(item[-1:-4])
#change item value
item[4]="love"
print(item)
#loop through a item
x="lipi" in item
print(x)
for x in item:
    print(x)
#check if item exist
if "lipi" in item:
    print("you are here")
if "hate" in item:
    print("yes , hate belongs to item")
#list length
print(len(item))
#add item :-we can add item using append().
item.append("kumari")
print(item)
#To add an item at specified place we use insert().
item.insert(1,"prince")
print(item)
#Remove item :- we can remove item using remove() method.
item.remove("prince")
print(item)
#pop() method use to remove specified index.
item.pop()
print(item)
#del keyword
#del item[1]
#print(item)
#del item
#print(item)
#clear
list=["lipi" , "kumari" , "thakur" , "btech"]
list.clear()
print(list)
#make a copy of list using copy()
list=["lipi" , "kumari"]
item=list.copy()
print(item)
#make a copy of list with the list() method
#lst=["lipi" , "lipi" , "lipi"]
#item=list(lst)
#print(item)
#join two list
list1=["lipi" , "kumari" , "a" , "c"]
list2=[1,2 ,3,4]
list3=list1+list2
print(list3)
#extend
list1.extend(list2)
print(list1)
