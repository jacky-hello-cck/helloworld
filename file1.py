//This a demo file refences from Youtube : object oriented programming python

class Dog:
	  def __init__(self,name,age):
		  self.name = name
		  self.age  = age
		  
		  def add_one(self,x):
			  return x + 1
		  
		  def get_age(self):
			  return self.age
			  
          def bark(self): 
              print("bark")  
              
          def get_name(self): 
			  return self.name      
      
d = Dog("hello",27)

print(d.name)
print(type(d))
d.bark()
print(d.age)

d2 = Dog("water",25)
print(d2)
print(d2.name)
