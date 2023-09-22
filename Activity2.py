english = int(input("Enter grades for ENGLISH: "))
filipino = int(input("Enter grades for FILIPINO: "))
science = int(input("Enter grades for SCIENCE: "))
math = int(input("Enter grades for MATH: "))
ap = int(input("Enter grades for ARALING PANLIPUNAN: "))
pe = int(input("Enter grades for PHYSICAL EDUCATION: "))

sum = english + filipino + science + math + ap + pe
average = sum / 6
result = round(average, 2)

print("Your average is: " + str(result))
