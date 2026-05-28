students_list = []

class student:

    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Marks:", self.marks)


name = input("enter the name of the student")
rollno = int(input("enter the roll no"))
marks = int(input("enter the marks obtained"))
student=student(name,rollno, marks)
students_list.append(student)

for student in students_list:
    student.display()
