from flask import Flask, render_template
# from router.user_router import user_router 

app = Flask(__name__)
# app.secret_key = "amudha123"  # required for sessions & flash messages

# app.register_blueprint(user_router, url_prefix="/user")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)