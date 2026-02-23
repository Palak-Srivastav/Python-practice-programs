# Program is to code using all important fundamentals learnt so far

students = []   # list to store student records

def add_student(name, marks):
    average = sum(marks) / len(marks)
    
    if average >= 75:
        result = "Distinction"
    elif average >= 35:
        result = "Pass"
    else:
        result = "Fail"
    
    student = {
        "name": name,
        "marks": marks,
        "average": average,
        "result": result
    }
    
    students.append(student)

def show_students():
    for s in students:
        print("\nName:", s["name"])
        print("Marks:", s["marks"])
        print("Average:", s["average"])
        print("Result:", s["result"])

# Adding students
add_student("Palak", [18,70,60])
add_student("Riya", [30, 40, 50])

show_students()
