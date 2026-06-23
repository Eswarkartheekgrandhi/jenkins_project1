from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/sum')
def sum_numbers():

    a = int(request.args.get("a",0))
    b = int(request.args.get("b",0))

    return jsonify({
        "a":a,
        "b":b,
        "sum":a+b
    })

if __name__ == "__main__":
    app.run()