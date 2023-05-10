from DAL.departments_dal import DepartmentsDB


class DepartmentsBLL:
    def __init__(self):
        self.__departments = DepartmentsDB()

    def get_all_departments(self):
        departments = self.__departments.get_all_departments()
        return departments

    def get_one_department(self, id):
        department_data = self.__departments.get_one_department(id)
        return department_data

    def update_department(self, id, obj):
        if (self.__departments.get_one_department(id)) is not None:
            self.__departments.update_department(id, obj)
            return "Updated!"

    def delete_department(self, id):
        if (self.__departments.get_one_department(id)) is not None:
            self.__departments.delete_department(id)
            return "Deleted!"

    def create_department(self, obj):
        self.__departments.create_department(obj)
        return "Department Created!"
