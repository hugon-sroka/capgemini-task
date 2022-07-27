class Employee:

    bonus = 1.05
    employees = []

    def __init__(self, emp_id ,first_name, last_name, age, departament, salary, bonus):
        self.emp_id = emp_id
        self.first_name=first_name
        self.last_name=last_name
        self.age = age
        self.departament = departament
        self.salary = salary
        self.bonus = bonus
        self.total_salary = bonus+salary
        Employee.employees.append(Employee)
        print(Employee.employees)



    def apply_bonus(self):
        'bonus has been applied'
        self.salary = int(self.pay*self.bonus)

    @classmethod
    def set_amount_bonus(cls, amt):
        cls.bonus=amt   ##

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name

    @fullname.deleter
    def fullname(self):
        print("Name deleted")
        self.first_name = None
        self.last_name = None

    def print_emp(self):
        for emp in self.employees:
            print(emp.fullname)









