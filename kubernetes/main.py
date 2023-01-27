from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

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
    app.run(host="0.0.0.0", port=1010, debug=True)
