class Department(object):
    def __init__(self,name,age):
        print("calling init from department class")
        self.name = name
        self.age = age

    def ShowDetails(self):
        print(f"name: {self.name},age:{self.age}")


class Students(Department):
    def __init__(self,name,age,Matric_no):
        print("calling init from the student class")
        super().__init__(name,age)
        self.matric_no =Matric_no

    def about(self):
        print("I am a student of this department")

    def ShowDetails_students(self):
        Department.ShowDetails(self)
        print(f"Matric Number: {self.matric_no}")



class Faculty(Department):
    def __init__(self,name,age,Identity_number):
        print("calling init from the faculty class")
        super().__init__(name,age)
        self.id_number = Identity_number

    def about(self):
        print("I am a lecturer in this department")

    def ShowDetails_faculty(self):
        Department.ShowDetails(self)
        print(f"Identity number: {self.id_number}")

#create student object
student_1 = Students("tofunmi", 24, 3912)
print(Students.mro())
student_1.ShowDetails_students()
student_1.about()

#create faculty object
faculty_1 = Faculty("Patrick Isibor", 50, 3345)
print(Faculty.mro())
faculty_1.ShowDetails_faculty()
faculty_1.about()