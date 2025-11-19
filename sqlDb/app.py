from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

def init_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="newone"
    )
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS staff(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            course VARCHAR(50),
            city VARCHAR(50),
            mobile VARCHAR(20),
            salary VARCHAR(20)
        )
    """)

    # Insert data
    cursor.execute("""
        INSERT INTO staff (name, course, city, mobile, salary)
        VALUES (%s, %s, %s, %s, %s)
    """, ("Kannan", "python", "CBE", "8541548744", "25000"))

    conn.commit()
    conn.close()

init_db()


@app.route('/')
def home():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="newone"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM staff")
    data = cursor.fetchall()
    conn.close()

    return render_template("index.html", list=data)


if __name__ == "__main__":
    app.run(debug=True)