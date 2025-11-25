from flask import render_template,redirect,url_for,request,session,flash
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["Newone"]
user = db["NewTable"]

def user_login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user_acc = user.find_one({"email":email,"password":password})

        if user_acc in user:
            session["user_acc"]= email
            flash("user login successfull")
            return redirect(url_for("user_router.user_dashboard"))
        else:
            flash("invalid username and password")
            return render_template("user_login.html")
    return render_template("user_login.html")