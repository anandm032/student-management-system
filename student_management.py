students_list = []

class Student:

    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def display(self):
        print("                 ")
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Marks:", self.marks)


while True:
    print("                ")
    print(" 1 = ADD STUDENTS")
    print("2= DISPLAY STUNDENTS")
    print("3= SEARCH THE ROLL NO")
    print("4 = EXIT")
    
    choise = int(input("enter the choice"))
    
    
    if choise==1:
        name = input("enter the name of the student")
        rollno = int(input("enter the roll no"))
        marks = int(input("enter the marks obtained"))

        student_obj=Student(name,rollno, marks)
        students_list.append(student_obj)
        
        
    elif choise==2:
        if len(students_list) == 0:
            print("No students found")

        else:
            for stu in students_list:
                stu.display()
    elif choise==3:
        search_roll = int(input("enter the rollnumber to search"))
        found = False
        for stud in students_list:
            if stud.rollno== search_roll:
                stud.display()
                found = True
        if found == False:
            print("student not found")
            
                
    elif choise==4:
        break
    else:
        print("input a valid choice")
        

        
