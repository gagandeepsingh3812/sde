from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["college"]
collection = db["student"]

if collection.count_documents({}) == 0:
    collection.insert_many([
        {"_id": 1, "Rno": 101, "Marks": 30},
        {"_id": 2, "Rno": 102, "Marks": 75},
        {"_id": 3, "Rno": 103, "Marks": 95},
        {"_id": 4, "Rno": 104, "Marks": 65}
    ])

for student in collection.find({"Marks": {"$gt": 80}}):
    print(student)

client.close()