class Employee:
  language = "Py" # This is a class attribute 
  salary = 1200000

  def getInfo(self):
    print(f"The language is {self.language}. The salary is {self.salary}")

  @staticmethod
  def greet ():
    print("Good Morning")


ankit = Employee()
ankit.language = "Javascript" #This is a instance attribute
print(ankit.salary, ankit.language)
# ankit.getInfo()
Employee.getInfo(ankit)
ankit.greet()