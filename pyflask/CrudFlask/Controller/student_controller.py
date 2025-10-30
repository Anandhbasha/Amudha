from bson import ObjectId
from db import get_db

db = get_db()

collection = db["NewTable"]

# Helper function
def serialize_doc(doc):
    doc['_id'] = str(doc['_id'])
    return doc

# read
def get_all():
    students = [serialize_doc(s) for s in collection.find()]
    return students

# create
def add_student(data):
    result = collection.insert_one(data)
    return result.inserted_id

# update
def update_student(student_id,data):
    result = collection.update_one({"_id":ObjectId(student_id)},{"$set":data})
    if result.matched_count>0:
        return {"message":"Student data updated successfully"}
    return {"message":"Student not found"}

# delete
def delete_student(student_id):
    result = collection.delete_one({"_id":ObjectId(student_id)})
    if result.deleted_count>0:
        return{"message":"Deleted successfully"}
    return{"message":"Not found"}