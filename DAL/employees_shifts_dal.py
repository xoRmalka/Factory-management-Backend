from pymongo import MongoClient
from bson import ObjectId


class EmployeesShiftsDB:
    def __init__(self):
        self.__client = MongoClient("localhost", 27017)
        self.__db = self.__client["FactoryDB"]
        self.__collection = self.__db["EmployeeShift"]

    def get_all_shifts(self):
        shifts = list(self.__collection.find({}))
        return shifts

    def get_by_shift_id(self, id):
        shifts = list(self.__collection.find({'shift_id': id}))
        return shifts

    def get_all_emps_shifts(self, id):
        shifts = list(self.__collection.find({'employee_id': id}))
        return shifts

    def get_one_empshift(self, id):
        shift = self.__collection.find_one({"id": id})
        return shift

    def update_empshift(self, id, obj):
        self.__collection.update_one({"id": id}, {"$set": obj})

    def delete_empshifts(self, id):
        self.__collection.delete_many({'employee_id': id})

    def create_empshift(self, obj):
        self.__collection.insert_one(obj)
