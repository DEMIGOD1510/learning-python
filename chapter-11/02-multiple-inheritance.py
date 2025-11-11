class Employee:
  company = "ITC"
  name = "defalt anme"
  def show(self):
    print(f"The name is {self.name} and the salary is {self.company}")

class Coder:
  language = "python"
  def printLanguage(self):
    print(f"Out of all the language here is your language: {self.language}")



class Programmer(Employee, Coder):
  company = "ITC Infotech"
  def showlanguage(self):
   print(f"The name is {self.company} and he is good with {self.language}")

a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showlanguage()

