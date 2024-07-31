def is_eligible(math, physics, chemistry):
    total_all_subjects = math + physics + chemistry
    total_math_physics = math + physics
    
    return (math >= 60 and physics >= 50 and chemistry >= 40 and total_all_subjects >= 200) or total_math_physics >= 150

def process_applications(students):
    eligible_students = []

    for student in students:
        name = student['name']
        math = student['math']
        physics = student['physics']
        chemistry = student['chemistry']
        
        if is_eligible(math, physics, chemistry):
            eligible_students.append(name)

    return eligible_students

n = int(input("Enter the number of students: "))
students = []

for _ in range(n):
    name = input("Enter the name of the student: ")
    math = int(input(f"Enter the marks in Mathematics for {name}: "))
    physics = int(input(f"Enter the marks in Physics for {name}: "))
    chemistry = int(input(f"Enter the marks in Chemistry for {name}: "))
    
    students.append({'name': name, 'math': math, 'physics': physics, 'chemistry': chemistry})

eligible_students = process_applications(students)

if eligible_students:
    print("Eligible students are:")
    for student in eligible_students:
        print(student)
else:
    print("No students are eligible for admission.")
