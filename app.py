from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Sum App Running"

@app.route("/sum/<int:a>/<int:b>")
def add(a, b):
    return f"Sum = {a + b}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)