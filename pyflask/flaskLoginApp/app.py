from flask import Flask, request, redirect, url_for, flash, render_template, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = "amudha123"

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["databaseName"]
users_collection = db["tableName"]

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        userName = request.form["userName"]
        Password = request.form["Password"]

        existing_user = users_collection.find_one({"userName": userName})
        if existing_user:
            flash("Username already exists")
        else:
            users_collection.insert_one({"userName": userName, "Password": Password})
            flash("Registration successful! Please login.")
            return redirect(url_for("login"))

    return render_template("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        userName = request.form["userName"]
        Password = request.form["Password"]

        user = users_collection.find_one({"userName": userName, "Password": Password})
        if user:
            session["user"] = userName
            flash("Login successful!")
            return redirect(url_for('home'))
        else:
            flash("Invalid Username or Password")

    return render_template("login.html")

@app.route('/home')
def home():
    if 'user' in session:
        return render_template("home.html", user=session["user"])
    else:
        flash("Please login first")
        return redirect(url_for("login"))

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged out successfully")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
