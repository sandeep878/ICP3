class Employee:
    employee_count = 0
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.employee_count += 1
    def display_employee_info(self):
        print(f"Name: {self.name}, Family: {self.family}, Salary: {self.salary}, Department: {self.department}")
    def calculate_average_salary(employee_list):
        total_salary = sum(emp.salary for emp in employee_list)
        return total_salary / len(employee_list) if len(employee_list) > 0 else 0
class FullTimeEmployee(Employee):
    fulltime_employee_count = 0
    def __init__(self, name, family, salary, department, benefits):
        super().__init__(name, family, salary, department)
        self.benefits = benefits
        FullTimeEmployee.fulltime_employee_count += 1
    def display_fulltime_employee_info(self):
        super().display_employee_info()
        print(f"Benefits: {self.benefits}")
employee1 = Employee("Sandeep", "Father and Mother", 50000, "IT")
employee2 = Employee("Sanath", "Spouse and Kids", 60000, "business")
employee1.display_employee_info()
employee2.display_employee_info()
print(f"Total number of employees: {Employee.employee_count}")
fulltime_employee1 = FullTimeEmployee("vishwa", "Spouse and Kids", 85000, "Finance", "Health Insurance")
fulltime_employee2 = FullTimeEmployee("Kumar", "Spouse", 90000, "Dentist", "Provident fund")
fulltime_employee1.display_fulltime_employee_info()
fulltime_employee2.display_fulltime_employee_info()
print(f"Total number of employees: {Employee.employee_count}")
print(f"Total number of full-time employees: {FullTimeEmployee.fulltime_employee_count}")
employee_list = [employee1, employee2, fulltime_employee1, fulltime_employee2]
average_salary = Employee.calculate_average_salary(employee_list)
print(f"Average Salary: {average_salary}")