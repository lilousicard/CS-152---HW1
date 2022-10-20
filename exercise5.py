#CS152 Fall 2022
#Lilou Sicard-Noel
#014122082
#Homework assignment 1
#Exercise 5

class Person:
	def __init__(self, fname, lname, age):
		self.firstname = fname
		self.lastname = lname
		self.age = age
	def can_consume_alcohol(self):
		return self.age >= 21

	def getFirstName(self):
		return self.firstname

	def getLastName(self):
		return self.lastname

class Student(Person):
	def __init__(self, fname, lname, age,gpa,status):
		super().__init__(fname, lname,age)
		self.gpa = gpa
		self.status = status

	def get_name(self):
		fn = self.getFirstName
		ln = self.getLastName
		return fn+ln

if __name__ == '__main__':
	studentList = [
		Student("Mike","Smith",21,3.7,"Senior"),
		Student("Larry","Mushroom",19,2.1,"Sophomore"),
		Student("Marry","Wolf",22,3.2,"Senior"),
		Student("Tommy","Tree",20,3.5,"Sophomore"),
		Student("Laura","Tall",21,3.1,"Junior"),
		Student("Amy","Paris",18,3.9,"Freshman")]

	answer = 0
	for s in studentList:
		if s.age>=21:
			answer+=1
	print("Out of "+str(len(studentList))+" students "+str(answer)+" are legal to consume alcohol")



