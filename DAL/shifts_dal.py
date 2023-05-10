from pymongo import MongoClient
from bson import ObjectId


class ShiftsDB:
    def __init__(self):
        self.__client = MongoClient("localhost", 27017)
        self.__db = self.__client["FactoryDB"]
        self.__collection = self.__db["Shifts"]

    def get_all_shifts(self):
        shifts = list(self.__collection.find({}))
        return shifts

    def get_one_shift(self, id):
        shift = self.__collection.find_one({"id": id})
        return shift

    def update_shift(self, id, obj):
        self.__collection.update_one({"id": id}, {"$set": obj})

    def delete_shift(self, id):
        self.__collection.delete_one({"id": id})

    def create_shift(self, obj):
        self.__collection.insert_one(obj)
