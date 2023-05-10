from flask import Flask
import json
from flask_cors import CORS
from bson import ObjectId


from Routers.departments_router import departments
from Routers.employees_router import employees
from Routers.shifts_router import shifts
from Routers.employees_shifts_router import employeesshifts


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


app = Flask(__name__)
app.json_encoder = JSONEncoder

CORS(app)


app.register_blueprint(departments, url_prefix="/departments")
app.register_blueprint(employees, url_prefix="/employees")
app.register_blueprint(shifts, url_prefix="/shifts")
app.register_blueprint(employeesshifts, url_prefix="/employeesshifts")


app.run()
