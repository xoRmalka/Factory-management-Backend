from DAL.employees_dal import EmployeesDB


class EmployeesBLL:
    def __init__(self):
        self.__employees = EmployeesDB()

    def get_all_employees(self):
        departments = self.__employees.get_all_employees()
        return departments

    def get_one_employee(self, id):
        employee_data = self.__employees.get_one_employee(id)

        return employee_data

    def update_employee(self, id, obj):
        if (self.__employees.get_one_employee(id)) is not None:
            self.__employees.update_employee(id, obj)
            return "Updated!"

    def delete_employee(self, id):
        if (self.__employees.get_one_employee(id)) is not None:
            self.__employees.delete_employee(id)
            return "Deleted!"

    def create_employee(self, obj):
        self.__employees.create_employee(obj)
        return "Employee Created!"
