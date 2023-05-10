from flask import Blueprint, jsonify, request
from BLL.employees_shifts_bll import EmployeesShiftsBLL

employeesshifts = Blueprint("employeesshifts", __name__)
employees_shifts_bll = EmployeesShiftsBLL()


@employeesshifts.route("/", methods=["GET"])
def get_all_shifts():
    return jsonify(employees_shifts_bll.get_all_shifts())


@employeesshifts.route("/add_shift/<int:id>", methods=["GET"])
def get_not_in_shifts(id):
    shift = employees_shifts_bll.get_not_in_shifts(id)

    if shift is None:
        return 'shift not found', 404

    return jsonify(shift)


@employeesshifts.route("/get_by_shift_id/<int:id>", methods=["GET"])
def get_by_shift_id(id):
    shifts = employees_shifts_bll.get_by_shift_id(id)

    if shifts is None:
        return 'shift not found', 404

    return jsonify(shifts)


@employeesshifts.route("<int:id>", methods=["GET"])
def get_emp_shifts(id):
    shift = employees_shifts_bll.get_emp_shifts(id)

    if shift is None:
        return 'shift not found', 404
    return jsonify(shift)


@employeesshifts.route("<int:id>", methods=["PUT"])
def update_shift(id):
    obj = request.json
    status = employees_shifts_bll.update_shift(id, obj)
    if status is None:
        return 'Error updating shift', 500
    return jsonify(status)


@employeesshifts.route("<int:id>", methods=["DELETE"])
def delete_shift(id):
    status = employees_shifts_bll.delete_emp_shifts(id)
    if status is None:
        return 'Error deleting shift', 500
    return jsonify(status)


@employeesshifts.route("/", methods=["POST"])
def create_shift():
    obj = request.json
    status = employees_shifts_bll.create_shift(obj)
    return jsonify(status)
