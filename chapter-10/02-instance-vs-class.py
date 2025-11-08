class Employee:
  language = "Py" # This is a class attribute 
  salary = 1200000


ankit = Employee()
ankit.language = "Javascript" #This is a instance attribute
print(ankit.salary, ankit.language)

