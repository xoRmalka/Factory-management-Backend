from flask import Blueprint, jsonify, request
from BLL.employees_bll import EmployeesBLL

employees = Blueprint("employees", __name__)
employees_bll = EmployeesBLL()


@employees.route("/", methods=["GET"])
def get_all_employees():
    return jsonify(employees_bll.get_all_employees())


@employees.route("<int:id>", methods=["GET"])
def get_one_employee(id):
    employee = employees_bll.get_one_employee(id)
    if employee is None:
        return 'Employee not found', 404
    return jsonify(employee)


@employees.route("<int:id>", methods=["PUT"])
def update_employee(id):
    obj = request.json
    status = employees_bll.update_employee(id, obj)
    if status is None:
        return 'Error updating employee', 500
    return jsonify(status)


@employees.route("<int:id>", methods=["DELETE"])
def delete_employee(id):
    status = employees_bll.delete_employee(id)
    if status is None:
        return 'Error deleting employee', 500
    return jsonify(status)


@employees.route("/", methods=["POST"])
def create_employee():
    obj = request.json
    status = employees_bll.create_employee(obj)
    return jsonify(status)
