from flask import Blueprint, jsonify, request
from BLL.shifts_bll import ShiftsBLL

shifts = Blueprint("shifts", __name__)
shifts_bll = ShiftsBLL()


@shifts.route("/", methods=["GET"])
def get_all_shifts():
    return jsonify(shifts_bll.get_all_shifts())


@shifts.route("/get_shifts_with_employees", methods=["GET"])
def get_all_shifts_with_employees():
    return jsonify(shifts_bll.get_all_shifts_with_employees())


@shifts.route("<int:id>", methods=["GET"])
def get_one_shift(id):
    shift = shifts_bll.get_one_shift(id)
    if shift is None:
        return 'shift not found', 404
    return jsonify(shift)


@shifts.route("<int:id>", methods=["PUT"])
def update_shift(id):
    obj = request.json
    status = shifts_bll.update_shift(id, obj)
    if status is None:
        return 'Error updating shift', 500
    return jsonify(status)


@shifts.route("<int:id>", methods=["DELETE"])
def delete_shift(id):
    status = shifts_bll.delete_shift(id)
    if status is None:
        return 'Error deleting shift', 500
    return jsonify(status)


@shifts.route("/", methods=["POST"])
def create_shift():
    obj = request.json
    status = shifts_bll.create_shift(obj)
    return jsonify(status)
