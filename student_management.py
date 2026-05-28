students_list = []

class Student:

    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Marks:", self.marks)


s1 = Student("ANAND", 720923243008, 96)
s2 = Student("Rahul", 720923243009, 87)

students_list.append(s1)
students_list.append(s2)

for student in students_list:
    student.display()
