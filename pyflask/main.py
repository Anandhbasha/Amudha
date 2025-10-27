from flask import Flask

# server
app = Flask(__name__)

# router
@app.route('/home')
# controller
def index():
    return ("Hello")

if __name__ == "__main__":
    app.run(debug=True)