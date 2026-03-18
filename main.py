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
print("GPA :", round(gpa_score, 2))
print("Scholarship :", scholarship, "KZT")
print("====================================")

print("Scholarship granted:", avg >= 90)
print("Perfect score:", avg == 100)