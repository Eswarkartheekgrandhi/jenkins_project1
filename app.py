from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    numbers = request.args.get("numbers", "")

    if not numbers:
        return "Usage: ?numbers=10,20,30"

    nums = [int(x) for x in numbers.split(",")]
    total = sum(nums)

    return f"Sum = {total}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)