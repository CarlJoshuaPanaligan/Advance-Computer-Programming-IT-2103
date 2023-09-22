name = input("Enter your father's name: ")
birthplace = input("Enter your father's birthplace: ")
birthday = input("Enter your father's birthday: ")
birthyear = int(input("Enter your father's birthyear: "))

age = 2023 - birthyear

print(name + " is " + str(age) + " years old and lives in " + birthplace + ". His birthday is on " + birthday)

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
