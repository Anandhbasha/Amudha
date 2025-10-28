# from flask import Flask


# app = Flask(__name__)
# # router
# @app.route('/')
# # controller
# def index():
#     return "Hello"

# if __name__ == "__main__":
#     app.run(debug=True)



from flask import Flask,jsonify,request

app = Flask(__name__)

students = [
    {"id":1,"name":"arun","age":20,"courserName":"Java"},
    {"id":2,"name":"Ajay","age":21,"courserName":"Python"},
    {"id":3,"name":"Akash","age":20,"courserName":"MERN"}
]

# read 

@app.route('/students',methods=["GET"])
def get_students():
    return jsonify(students)


# add
@app.route('/students',methods=["POST"])
def add_student():
    new_student = request.get_json()
    students.append(new_student)
    return jsonify({"message":"Student added succesfully","data":students})

# update
@app.route('/stud/<int:id>',methods=["PUT"])
def update_student(id):
    for student in students:
        if student['id']==id:
            student.update(request.get_json())
            return jsonify({"message":"Updated Data succesfully","data":student})
    return jsonify({"message":"Student not found"})


# delete
@app.route('/stud/<int:id>',methods=["DELETE"])
def delete_student(id):
    for student in students:
        if student['id']==id:
            students.remove(student)
            return jsonify({"message":"Deleted Data succesfully","data":students})
    return jsonify({"message":"Student not found"})

if __name__ == "__main__":
    app.run(debug=True)