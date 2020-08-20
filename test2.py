# Object-Oriented Programming oop
class Student: 
	 def __init__(self,name,age,grade):
		 self.name = name
		 self.age  = age
		 self.grade = grade #0-100 
		 
	 def get_grade(self):
		 return self.grade 

class Course:
    def __init__(self, name,max_students):
	    self.name = name
	    self.max_students = max_students
	    self.students = []
	    
    def add_student(self, student):
		if len(self.students) < self.max_students:
	         self.students.append(student)
	         #return true 
	              	                                                        
    def get_average_grade(self):
		value = 0
	    
	        for student in self.students: 
                  value += student.get_grade()
			
		return value / len(students)		    
 
s1 = Student("Bob",20,90)
s2 = Student("Jim",23,89)
s3 = Student("Sam",18,70)
print(s3)
print(s2)

course = Course("Science",2)
course.add_student(s1)
course.add_student(s2)
print(course)
