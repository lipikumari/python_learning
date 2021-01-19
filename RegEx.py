#Python RegEx
#A RegEx or regular expression is a sequence of characters that forms a search pattern
import re
txt="the school friend"
x = re.search("^the.*friend$", txt)
if x:
    print("yes, you got it")
else:
     print("Try again")
#findall() returns a list containing all matches.
import re
txt="Lipi loves fried rice"
x=re.findall("i",txt)
print(x)
#split()
import re
txt="once upon a time"
x=re.split("\s",txt)
print(x)
x=re.split("\s",txt,1)
print(x)
#Sub() function :- it replaces the matches with the text of your choice
x=re.sub("\s","time",txt)
print(x)
