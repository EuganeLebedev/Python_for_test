class SelaryCalculator:
    def calculate(self):
        return 100500

    def calculate_with_bonus(self):
        return self.calculate() * 1.05

class Employee:
    def __init__(self, name):
        self.name = name

        def get_selart(self):
            return self.calculator.calculate()

class Director(Employee):
    def get_selary(self):
        salary = super().get_selary()
        return self.calculator.calculate_with_bonus() + salary

class Engineer(Employee):
    pass


def calculate_year_salary(employee):
    return employee.get_salary() * 12


calculate_year_salary(Director())
calculate_year_salary(Engineer())
calculate_year_salary(Employee())
