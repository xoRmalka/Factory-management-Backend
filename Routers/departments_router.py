from flask import Blueprint, jsonify, request
from BLL.departments_bll import DepartmentsBLL

departments = Blueprint("departments", __name__)
departments_bll = DepartmentsBLL()


@departments.route("/", methods=["GET"])
def get_all_departments():
    return jsonify(departments_bll.get_all_departments())


@departments.route("<int:id>", methods=["GET"])
def get_one_department(id):
    status = departments_bll.get_one_department(id)
    if status is None:
        return 'Department not found', 404
    return jsonify(status)


@departments.route("<int:id>", methods=["PUT"])
def update_department(id):
    obj = request.json
    status = departments_bll.update_department(id, obj)
    if status is None:
        return 'Error updating department', 500
    return jsonify(status)


@departments.route("<int:id>", methods=["DELETE"])
def delete_department(id):
    status = departments_bll.delete_department(id)
    if status is None:
        return 'Error deleting department', 500
    return jsonify(status)


@departments.route("/", methods=["POST"])
def create_department():
    obj = request.json
    status = departments_bll.create_department(obj)
    return jsonify(status)
