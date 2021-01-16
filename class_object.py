#python class and objects
#create a class
class Lipi:
    x=4
print(Lipi)
#create a object
c1=Lipi()
print(c1.x)
#the _init_()function
class Student:
    def __init__(self,name,age):
        self .name =name
        self.age =age
s1=Student("Lipi",20)
print(s1.name)
print(s1.age)
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
