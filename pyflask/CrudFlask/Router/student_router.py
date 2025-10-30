from flask import request,Blueprint,jsonify
from Controller.student_controller import get_all,add_student,delete_student,update_student

student_stats = Blueprint("student_stats",__name__)

@student_stats.route('/add',methods=["POST"])
def add():
    data = request.json
    res = add_student(data)
    return jsonify(res)

@student_stats.route('/read',methods=["GET"])
def get():
    res = get_all()
    return jsonify(res)

@student_stats.route('/update/<id>',methods=["PUT"])
def update(id):
    data = request.json
    res = update_student(id,data)
    return jsonify(res)

@student_stats.route('/delete/<id>',methods=["DELETE"])
def delete(id):
    res = delete_student(id)
    return jsonify(res)