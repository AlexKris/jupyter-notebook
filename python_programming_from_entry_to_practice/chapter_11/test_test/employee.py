class Employee:
    
    def __init__(self, first_name, last_name, age):
        self.employee_first_name = first_name
        self.employee_last_name = last_name
        self.employee_age = age
        self.employee_salary = 0

    def give_raise(self, salary=None):
        """年薪增加5000美元"""
        if salary:
            self.employee_salary += salary
        else:
            self.employee_salary += 5000