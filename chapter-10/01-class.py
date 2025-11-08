class Employee:
  language = "Py" # This is a class attribute 
  salary = 1200000


ankit = Employee()
ankit.name = "Ankit" #This is a instance attribute
print(ankit.name, ankit.salary, ankit.language)

rohan = Employee()
rohan.name = "Rohan Zoro Robinson"
print(rohan.name, rohan.salary, rohan.language)

# Here name is object attribute and salary and language are class attributes as they directly belong to the class