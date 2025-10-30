from flask import Flask
from Router.student_router import student_stats

app = Flask(__name__)

app.register_blueprint(student_stats,url_prefix="/api")

if __name__ =="__main__":
    app.run(debug=True)