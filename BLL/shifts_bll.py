from DAL.shifts_dal import ShiftsDB


class ShiftsBLL:
    def __init__(self,):
        self.__shifts = ShiftsDB()

    def get_all_shifts(self):
        shifts = self.__shifts.get_all_shifts()
        return shifts

    def get_one_shift(self, id):
        shift_data = self.__shifts.get_one_shift(id)
        return shift_data

    def update_shift(self, id, obj):
        if (self.__shifts.get_one_shift(id)) is not None:
            self.__shifts.update_shift(id, obj)
            return "Updated!"

    def delete_shift(self, id):
        if (self.__shifts.get_one_shift(id)) is not None:
            self.__shifts.delete_shift(id)
            return "Deleted!"

    def create_shift(self, obj):
        self.__shifts.create_shift(obj)
        return "Shift Created!"

    def get_all_shifts_with_employees(self):
        from BLL.employees_shifts_bll import EmployeesShiftsBLL
        from BLL.employees_bll import EmployeesBLL

        employeesShiftsBLL = EmployeesShiftsBLL()
        employeesBLL = EmployeesBLL()

        shifts = self.__shifts.get_all_shifts()
        for shift in shifts:

            id = int(shift['id'])
            emps_in_shift = employeesShiftsBLL.get_by_shift_id(id)

            empsinshift = []
            for emp in emps_in_shift:
                id = int(emp['employee_id'])
                emp = employeesBLL.get_one_employee(id)
                empsinshift.append(
                    {"first_name": emp["first_name"], "last_name": emp["last_name"], "employee_id": emp["id"]})
            shift["empsinshift"] = empsinshift

        return shifts
