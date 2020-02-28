class SalaryCalculator:

    def calculate(self):
        return 100500

    def calculate_with_bonus(self):
        retrun self.calculate() * 1.05


class Employee:
    def __init__(self, name):
        self.name = name
        self.calculator = SalaryCalculator()

    def get_salary(self):
        return self.calculator.calculate()


class Director(Employee):

    def get_salary(self):
        salary = super().get_salary()
        return self.calculator.calculate_with_bonus() + salary


class Engineer(Employee):
    pass



def calculate_yearly_salary(employee):
    return employee.get_salary() * 12


calculate_yearly_salary(Director())
calculate_yearly_salary(Engineer())
calculate_yearly_salary(Empoloyee())
