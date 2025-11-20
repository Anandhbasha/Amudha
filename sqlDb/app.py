from flask import Flask,render_template
import mysql.connector

app = Flask(__name__)

def dbConnect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = "Newone"
    )
    
@app.route('/')
def dbRead():
    conn = dbConnect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM staff")
    row = cur.fetchall()
    conn.close()
    return render_template("index.html",row =row)

@app.route('/add')
def addUser():
    conn = dbConnect()
    cur = conn.cursor()
    cur.execute("INSERT INTO staff (name,course,city,salary)values(%s,%s,%s,%s)",('raja','Design','erode','8000'))
    conn.commit()
    conn.close()
    return "Inserted Successfully"

if __name__=="__main__":
    app.run(debug=True)