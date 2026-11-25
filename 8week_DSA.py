class Employee:
    
    company = "Google"
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+ "."+last+"@company.com"
        
    def full_name(self):
        return f'{self.first} {self.last}'

# emp_1 = Employee("John", "Mensah" , 6000)


class CSQ_Lib(Employee):
    def __init__(self, first, last, pay):
        Employee.__init__(self, first, last, pay)

new_employ = CSQ_Lib("Kofi", "Bono", 900)
print(new_employ.full_name())
print(new_employ.email)

