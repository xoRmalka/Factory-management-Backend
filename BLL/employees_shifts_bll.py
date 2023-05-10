from DAL.employees_shifts_dal import EmployeesShiftsDB
from BLL.shifts_bll import ShiftsBLL

shiftBLL = ShiftsBLL()


class EmployeesShiftsBLL:
    def __init__(self):
        self.__employees_shifts = EmployeesShiftsDB()

    def get_all_shifts(self):
        shifts = self.__employees_shifts.get_all_shifts()
        return shifts

    def get_by_shift_id(self, id):  # emp id
        shifts = self.__employees_shifts.get_by_shift_id(id)
        return shifts

    def get_emp_shifts(self, id):  # emp id
        shifts = self.__employees_shifts.get_all_emps_shifts(id)

        finalshifts = []
        for shift in shifts:
            id = int(shift['shift_id'])
            shift = shiftBLL.get_one_shift(id)
            finalshifts.append(shift)

        return finalshifts

    def get_not_in_shifts(self, id):
        empshifts = self.__employees_shifts.get_all_emps_shifts(id)
        shifts = shiftBLL.get_all_shifts()

        finalshifts = []

        for shift in empshifts:
            id = int(shift['shift_id'])
            shift = shiftBLL.get_one_shift(id)
            finalshifts.append(shift)

        employee_shift_ids = {shift['id'] for shift in finalshifts}

        shifts = [shift for shift in shifts if shift['id']
                  not in employee_shift_ids]

        if len(shifts) == 0:
            id = int(-2)
            return [{"date": 'This employee is on all shifts', "id": id}]
        return shifts

    def update_shift(self, id, obj):
        if (self.__employees_shifts.get_one_empshift(id)) is not None:
            self.__employees_shifts.update_empshift(id, obj)
            return "Updated!"

    def delete_emp_shifts(self, id):
        if (self.__employees_shifts.get_one_empshift(id)) is not None:
            self.__employees_shifts.delete_empshifts(id)
            return "Deleted!"

    def create_shift(self, obj):
        self.__employees_shifts.create_empshift(obj)
        return "Shift Created!"
