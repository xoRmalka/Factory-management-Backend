from pymongo import MongoClient
from bson import ObjectId


class DepartmentsDB:
    def __init__(self):
        self.__client = MongoClient("localhost", 27017)
        self.__db = self.__client["FactoryDB"]
        self.__collection = self.__db["Departments"]

    def get_all_departments(self):
        departments = list(self.__collection.find({}))
        return departments

    def get_one_department(self, id):
        department = self.__collection.find_one({"id": id})
        return department

    def update_department(self, id, obj):
        self.__collection.update_one({"id": id}, {"$set": obj})

    def delete_department(self, id):
        self.__collection.delete_one({"id": id})

    def create_department(self, obj):
        self.__collection.insert_one(obj)
