name = input("Enter student name: ")
math = float(input("Enter Math grade: "))
phys = float(input("Enter Physics grade: "))
pyth = float(input("Enter Python grade: "))


avg = (math + phys + pyth) / 3


if avg >= 90:
    scholarship = 35000
else:
    scholarship = 0

gpa_score = avg / 25


print("====================================")
print("        STUDENT REPORT CARD         ")
print("====================================")
print("Student :", name)
print("Math :", math)
print("Physics :", phys)
print("Python :", pyth)
print("------------------------------------")

print("Average :", round(avg, 2))
if avg>=90:    
    print("Letter grade : A")
elif avg>=75:
    print("Letter grade : B")
elif avg>=60:
    print("Letter grade : C")
elif avg>=50:
    print("Letter grade : D")
else:
    print("Letter grade : F")
    
print("Scholarship granted:", avg >= 90)
print("====================================")



grades = [math,phys,pyth]
subjects = ["Math","Physic","Python"]

for i in range(3):
    if grades[i] >= 90:
        print(subjects[i],":",grades[i],"→","Excellent")
    elif grades[i] >= 75:
        print(subjects[i],":",grades[i],"→","Good")
    elif grades[i] >= 60:
        print(subjects[i],":",grades[i],"→","Satisfactory")
    else:
        print(subjects[i],":",grades[i],"→","Fail")
print("====================================")

print("Name uppercase:", name.upper())
print("Name lowercase:", name.lower())
print("Name length:", len(name))
print("Name uppercase:", name.replace(name[0],"*",1))