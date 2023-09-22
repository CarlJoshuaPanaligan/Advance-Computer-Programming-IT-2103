name = input("Enter your father's name: ")
birthplace = input("Enter your father's birthplace: ")
birthday = input("Enter your father's birthday: ")
birthyear = int(input("Enter your father's birthyear: "))

age = 2023 - birthyear

print(name + " is " + str(age) + " years old and lives in " + birthplace + ". His birthday is on " + birthday)
