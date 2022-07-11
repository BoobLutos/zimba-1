from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Ye nze aliko!!!"

@app.route("/hihi/")
def who():
    return "who the hell are you?"

@app.route("/hihi/<username>")
def greet(username):
    return f"Hi there, {username}!"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)