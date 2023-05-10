from pymongo import MongoClient
from bson import ObjectId


class EmployeesDB:
    def __init__(self):
        self.__client = MongoClient("localhost", 27017)
        self.__db = self.__client["FactoryDB"]
        self.__collection = self.__db["Employees"]

    def get_all_employees(self):
        employees = list(self.__collection.find({}))
        return employees

    def get_one_employee(self, id):
        employee = self.__collection.find_one({"id": id})
        return employee

    def update_employee(self, id, obj):
        self.__collection.update_one({"id": id}, {"$set": obj})

    def delete_employee(self, id):
        self.__collection.delete_one({"id": id})

    def create_employee(self, obj):
        self.__collection.insert_one(obj)
