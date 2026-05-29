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
def load_students():
    file = open("student.txt","r")
    for line in file:
        name,rollno,marks = line.strip().split(",")
        student_ob = Student(name,int(rollno),int(marks))
        students_list.append(student_ob)
    file.close()
        
def save_students():
        file = open("student.txt", "w")
        for stun in students_list:
            file.write(f"{stun.name},{stun.rollno},{stun.marks}\n")
        file.close()
        
load_students()

while True:
    print("                ")
    print(" 1 = ADD STUDENTS")
    print("2= DISPLAY STUNDENTS")
    print("3= SEARCH THE ROLL NO")
    print("4= DELETE THE STUDENT")
    print("5= update the mark")
    print("6= SAVE THE DETAILS")
    print("7 = EXIT")
    
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
        delete_stu = int(input("enter the rollnumber to delete the student data"))
        found = False
        for studoc in students_list:
            if studoc.rollno== delete_stu:
                students_list.remove(studoc)
                found= True
                print("Student deleted successfully")
        if found== False:
                print("Student not found")
            
    elif choise==5:
        stu_roll = int(input("enter the student roll no to update"))
        stu_mark = int(input("enter the student new mark"))
        found = False
        for studo in students_list:
            if studo.rollno==stu_roll:
                studo.marks=stu_mark
                found= True
                print("Student MARK UPDATED successfully")
        if found== False:
                 print("Student not found")
    elif choise==6:
        save_students()
        print("students saved sucessfully")
                   
            
    elif choise==7:
        break
    else:
        print("input a valid choice")
        

        
